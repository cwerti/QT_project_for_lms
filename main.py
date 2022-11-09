import sys
import sqlite3
from PIL import Image
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QTextEdit, QLineEdit, QTableWidget, \
    QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from PyQt5 import uic
import datetime as dt
import xlsxwriter
import numpy as np
from pathlib import Path

Q = QPushButton

appStyle = """
QMainWindow{
background-color: darkgray;
}
"""


def save_in_dir(file):  # сохраняем в директорию пользователя
    db_folder = Path.home()
    db_folder = db_folder / f'{file}'
    return str(db_folder)


def date_from_int(date):
    date = int(''.join(date.split('-')))
    return date


def int_from_date(date, lens=False):
    temp = str(date)
    if lens is False:
        date = temp[:4] + '-' + temp[4:6] + '-' + temp[6:]
    else:
        date = temp[:2] + '-' + temp[4:6] + '-' + temp[6:]
    return date


def add_db(sum, date, category, coment):
    con = sqlite3.connect("./projeckt_db.sqlite")
    date = date_from_int(date)
    con.execute("""
    CREATE TABLE IF NOT EXISTS spending_DB(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    sum      INTEGER,
    date     INTEGER,
    category STRING,
    coments  STRING  DEFAULT ('Коментарий не указан') 
    );
    """)
    cur = con.cursor()
    ins = f"""INSERT INTO spending_DB (sum, date, category, coments) VALUES ({sum}, '{date}', '{category}', '{coment}')"""
    count = cur.execute(ins)
    con.commit()
    cur.close()


def create_diag(labels, sizes):
    size = np.array(sizes)
    size = size / size ** 0.7
    fig1, ax1 = plt.subplots(frameon=False)
    ax1.pie(size, labels=labels,
            wedgeprops={'width': 0.4, 'ls': '--', 'lw': 2, 'edgecolor': "black"})
    ax1.axis('equal')
    name_file = save_in_dir('saved_figure.png')
    fig1.savefig(name_file, dpi=600)


class Notification(QWidget):
    next: QPushButton

    def __init__(self):
        super().__init__()
        self.init_ui()

    def enter(self):
        main.show()
        self.hide()

    def init_ui(self):
        uic.loadUi('alert.ui', self)
        self.setFixedSize(self.size())
        self.next.clicked.connect(self.enter)


class DbInQT(QMainWindow):
    table: QTableWidget
    saving: QPushButton

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.titles = None
        self.con = sqlite3.connect("films_db.sqlite")
        self.data_in_table = []

    def init_ui(self):
        uic.loadUi('table.ui', self)
        self.setFixedSize(self.size())
        self.update_redult()
        self.table.itemChanged.connect(self.item_changed)
        self.saving.clicked.connect(self.save_results)

        # self.table.setColumnCount(5)
        # self.table.setRowCount(2)
        # self.table.setItem(1, 1, QTableWidgetItem('wqewqr'))

    def update_redult(self):
        con = sqlite3.connect("./projeckt_db.sqlite")
        cur = con.cursor()
        data = cur.execute(f"""SELECT * FROM spending_DB """).fetchall()
        self.table.setColumnCount(5)
        self.table.setRowCount(len(data))
        for row, (id, price, date, category, coments) in enumerate(data):
            values = (id, price, date, category, coments)
            for i in range(5):
                self.table.setItem(row, i, QTableWidgetItem(str(values[i])))

    def item_changed(self, item: QTableWidgetItem):
        con = sqlite3.connect("./projeckt_db.sqlite")
        cur = con.cursor()
        data = cur.execute(f"""SELECT * FROM spending_DB """).fetchall()
        self.id = []
        for row, (id, price, date, category, coments) in enumerate(data):
            self.id.append(id)
        self.titles = [description[0] for description in cur.description]
        self.data_in_table = self.data_in_table + [self.id[item.row()], self.titles[item.column()], item.text()]
        print(self.data_in_table)

    def save_results(self):
        for i in range(0, len(self.data_in_table), 3):
            con = sqlite3.connect("./projeckt_db.sqlite")
            cur = con.cursor()
            data = cur.execute(f"""UPDATE spending_DB SET 
            {self.data_in_table[i + 1]} = '{self.data_in_table[i + 2]}' WHERE id = {int(self.data_in_table[i])}""").fetchall()
            con.commit()
            cur.close()


class GraphDate(QWidget):
    generate: QPushButton
    label_for_graph: QLabel
    left_date: QLineEdit
    right_date: QLineEdit
    home: QPushButton

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        uic.loadUi('graph.ui', self)
        self.left_date.setText(str(dt.date.today()))
        self.right_date.setText(str(dt.date.today()))
        self.left = self.left_date.text()
        self.right = self.right_date.text()
        self.graph()
        self.generate.clicked.connect(self.graph)
        self.home.clicked.connect(self.go_to_home)

    def save_pix(self):
        name_file = save_in_dir('graph.png')
        im = Image.open(name_file)
        im2 = im.resize((621, 461))
        im2.save(name_file)
        self.pixmap = QPixmap(name_file)
        self.label_for_graph.setPixmap(self.pixmap)

    def date_from_db(self, left=0, right=30000000):
        left = date_from_int(left)
        right = date_from_int(right)
        con = sqlite3.connect("./projeckt_db.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT date FROM spending_DB WHERE date >= ? and date <= ?""",
                             (left, right)).fetchall()
        date = []
        for i in result:
            date.append(int_from_date(i[0], lens=True))
        summa = []
        for i in result:
            res = cur.execute(f"""SELECT SUM(sum) FROM spending_DB WHERE date = '{i[0]}'""").fetchall()
            summa.append(res[0][0])
        return summa, date

    def graph(self):
        self.left = self.left_date.text()
        self.right = self.right_date.text()
        summa, date = self.date_from_db(self.left, self.right)
        summa = np.array(summa)
        fig, ax = plt.subplots()
        ax.bar(date, summa, width=0.1)
        ax.set_facecolor('seashell')
        fig.set_facecolor('floralwhite')
        name_file = save_in_dir('graph.png')
        fig.savefig(name_file, dpi=600)
        self.save_pix()

    def go_to_home(self):
        main.diag_all_time()
        main.last_category_output()
        main.last_day_output()
        main.last_coment_output()
        main.show()
        self.hide()


class DateChoise(QWidget):
    date: QTextEdit
    next: QPushButton

    def __init__(self):
        super().__init__()
        self.init_ui()

    def choise_date(self):
        self.day = self.date.toPlainText()
        date_mas = list(map(int, self.day.split('-')))
        self.date_out = str(dt.date(date_mas[0], date_mas[1], date_mas[2]))
        self.date.setText(self.date_out)

    def farther(self):
        self.choise_date()
        self.hide()

    def cout(self):
        return self.date.toPlainText()

    def init_ui(self):
        uic.loadUi('date_change.ui', self)
        self.date.setText(str(dt.date.today()))
        self.setFixedSize(self.size())
        self.next.clicked.connect(self.farther)


class InputWind(QWidget):
    eat: QPushButton
    car: QPushButton
    chill: QPushButton
    other: QPushButton
    fem: QPushButton
    credit: QPushButton
    worse: QPushButton
    podar: QPushButton
    today: QPushButton
    yesterday: QPushButton
    the_day_before_yesterday: QPushButton
    another_day: QPushButton
    coments: QTextEdit
    summa: QTextEdit
    next: QPushButton

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.date_choice = DateChoise()

    def category_choice(self):
        self.category = None
        button = QApplication.instance().sender()
        self.category = button.text()

    def date_choice_today(self):
        self.day = dt.date.today()

    def date_choice_yesterday(self):
        self.day = dt.date.today() - dt.timedelta(days=1)

    def choise_the_day_before_yesterday(self):
        self.day = dt.date.today() - dt.timedelta(days=2)

    def date_choice_another_day(self):
        self.date_choice.show()
        self.date_choice.setStyleSheet(appStyle)
        self.day = None

    def date_check(self):
        self.today.clicked.connect(self.date_choice_today)
        self.yesterday.clicked.connect(self.date_choice_yesterday)
        self.the_day_before_yesterday.clicked.connect(self.choise_the_day_before_yesterday)
        self.another_day.clicked.connect(self.date_choice_another_day)

    def category_check(self):
        self.eat.clicked.connect(self.category_choice)
        self.chill.clicked.connect(self.category_choice)
        self.other.clicked.connect(self.category_choice)
        self.fem.clicked.connect(self.category_choice)
        self.credit.clicked.connect(self.category_choice)
        self.worse.clicked.connect(self.category_choice)
        self.podar.clicked.connect(self.category_choice)
        self.car.clicked.connect(self.category_choice)

    def coment_check(self):
        self.coment = self.coments.toPlainText()

    def sum_check(self):
        self.sum = int(self.summa.toPlainText())

    def add_db_QT(self):
        self.sum_check()
        self.coment_check()
        if self.day == None:
            self.day = self.date_choice.cout()
        self.day = str(self.day)
        add_db(self.sum, self.day, self.category, self.coments.toPlainText())

        main.diag_all_time()
        main.last_category_output()
        main.last_day_output()
        main.last_coment_output()
        main.show()
        self.hide()

    def init_ui(self):
        uic.loadUi('123.ui', self)
        self.setFixedSize(self.size())
        self.category_check()
        self.date_check()
        self.next.clicked.connect(self.add_db_QT)


class MainWind(QMainWindow):
    main: QWidget
    label: QLabel
    add: QPushButton
    day: QPushButton
    all: QPushButton
    month: QPushButton
    week: QPushButton
    last_date: QLabel
    last_category: QLabel
    inform: QLabel
    data_to_excel: QPushButton
    label_4: QLabel
    graph: QPushButton
    btn_lst_trans: QPushButton

    def category_from_db(self, left=0, right=30000000):
        con = sqlite3.connect("./projeckt_db.sqlite")
        cur = con.cursor()
        mn = set()
        result = cur.execute("""SELECT category FROM spending_DB WHERE date >= ? and date <= ?""",
                             (left, right)).fetchall()
        for elem in result:
            mn.add(elem[0])
        con.close()
        return list(mn)

    def sum_from_db(self, left=0, right=30000000):
        con = sqlite3.connect("./projeckt_db.sqlite")
        cur = con.cursor()
        sum_db_data = []
        category = self.category_from_db()
        for it in category:
            result = cur.execute(f"""SELECT sum FROM spending_DB WHERE category = '{it}' and date >= ? and date <= ?""",
                                 (left, right)).fetchall()
            sum = 0
            for it in result:
                sum += (it[0])
            if sum != 0:
                sum_db_data.append(sum)
        return sum_db_data

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.input_wind = InputWind()
        self.notif = Notification()
        self.input_graph = GraphDate()
        self.table = DbInQT()

    def diag_all_time(self):
        labels = self.category_from_db()
        sizes = self.sum_from_db()
        self.save_pix(labels, sizes)

    def diag_in_day(self):
        left = date_from_int(str(dt.datetime.now().date()))
        right = date_from_int(str(dt.datetime.now().date()))
        labels = self.category_from_db(left, right)
        sizes = self.sum_from_db(left, right)
        self.save_pix(labels, sizes)

    def diag_in_weak(self):
        left = date_from_int(str(dt.datetime.now().date() - dt.timedelta(weeks=1)))
        right = date_from_int(str(dt.datetime.now().date()))
        labels = self.category_from_db(left, right)
        sizes = self.sum_from_db(left, right)
        self.save_pix(labels, sizes)

    def diag_in_month(self):
        left = date_from_int(str(dt.datetime.now().date() - dt.timedelta(days=30)))
        right = date_from_int(str(dt.datetime.now().date()))
        labels = self.category_from_db(left, right)
        sizes = self.sum_from_db(left, right)
        self.save_pix(labels, sizes)

    def save_pix(self, labels, sizes):
        create_diag(labels, sizes)
        name_file = save_in_dir("saved_figure.png")
        im = Image.open(name_file)
        im2 = im.resize((621, 461))
        im2.save(name_file)
        self.pixmap = QPixmap(name_file)
        self.label.setPixmap(self.pixmap)

    def last_category_output(self):
        con = sqlite3.connect("./projeckt_db.sqlite")
        cur = con.cursor()
        i_num = cur.execute(f"""SELECT MAX(id) FROM spending_DB """).fetchall()
        result = cur.execute(f"""SELECT * FROM spending_DB WHERE id = '{i_num[0][0]}'""").fetchall()
        self.last_category.setText(result[-1][-2])
        self.last_category.setAlignment(Qt.AlignCenter)
        self.last_category.setStyleSheet("background-color: rgb(103, 103, 108);")

    def last_day_output(self):
        con = sqlite3.connect("./projeckt_db.sqlite")
        cur = con.cursor()
        i_num = cur.execute(f"""SELECT MAX(id) FROM spending_DB """).fetchall()
        result = cur.execute(f"""SELECT * FROM spending_DB WHERE id = '{i_num[0][0]}'""").fetchall()
        result_st = str(result[-1][-3])
        year, month, day = str(result_st[:4]), str(result_st[4:6]), str(result_st[6:])
        self.last_date.setText(year + '-' + month + '-' + day)
        self.last_date.setAlignment(Qt.AlignCenter)
        self.last_date.setStyleSheet("background-color: rgb(103, 103, 108);")

    def last_coment_output(self):
        con = sqlite3.connect("./projeckt_db.sqlite")
        cur = con.cursor()
        i_num = cur.execute(f"""SELECT MAX(id) FROM spending_DB """).fetchall()
        result = cur.execute(f"""SELECT * FROM spending_DB WHERE id = '{i_num[0][0]}'""").fetchall()
        result_st = str(result[-1][-1])
        self.label_4.setText(result_st)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setStyleSheet("background-color: rgb(59, 49, 93);")

    def db_to_excel(self):
        con = sqlite3.connect("./projeckt_db.sqlite")
        cur = con.cursor()
        data = cur.execute(f"""SELECT * FROM spending_DB """).fetchall()
        workbook = xlsxwriter.Workbook('Суммы.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(0, 0, 'id')
        worksheet.write(0, 1, 'price')
        worksheet.write(0, 2, 'date')
        worksheet.write(0, 3, 'category')
        worksheet.write(0, 4, 'coments')
        for row, (id, price, date, category, coments) in enumerate(data):
            worksheet.write(row + 1, 0, id)
            worksheet.write(row + 1, 1, price)
            worksheet.write(row + 1, 2, int_from_date(date))
            worksheet.write(row + 1, 3, category)
            worksheet.write(row + 1, 4, coments)
        workbook.close()
        self.notif.show()

    def db_show(self):
        main.hide()
        self.table.show()

    def init_ui(self):
        uic.loadUi('test.ui', self)
        self.diag_all_time()
        self.add.clicked.connect(self.next)
        self.setFixedSize(self.size())
        self.setWindowTitle("Калькулятор расходов")
        self.btn_lst_trans.clicked.connect(self.db_show)
        self.day.clicked.connect(self.diag_in_day)
        self.all.clicked.connect(self.diag_all_time)
        self.week.clicked.connect(self.diag_in_weak)
        self.month.clicked.connect(self.diag_in_month)
        self.data_to_excel.clicked.connect(self.db_to_excel)
        self.graph.clicked.connect(self.graph_data)
        self.last_category_output()
        self.last_day_output()
        self.last_coment_output()

    def graph_data(self):
        self.input_graph.show()
        main.hide()

    def next(self):
        self.input_wind.show()
        main.hide()
        self.input_wind.setStyleSheet(appStyle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWind()
    main.setStyleSheet(appStyle)
    main.show()
    sys.exit(app.exec_())
