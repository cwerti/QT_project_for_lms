# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '123.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main1(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(615, 829)
        self.label = QtWidgets.QLabel(main)
        self.label.setGeometry(QtCore.QRect(110, 0, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.summa = QtWidgets.QTextEdit(main)
        self.summa.setGeometry(QtCore.QRect(0, 40, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.summa.setFont(font)
        self.summa.setDocumentTitle("")
        self.summa.setAcceptRichText(True)
        self.summa.setObjectName("summa")
        self.eat = QtWidgets.QPushButton(main)
        self.eat.setGeometry(QtCore.QRect(60, 170, 81, 81))
        self.eat.setStyleSheet("background-color: rgb(255, 32, 35);")
        self.eat.setObjectName("eat")
        self.car = QtWidgets.QPushButton(main)
        self.car.setGeometry(QtCore.QRect(210, 170, 81, 81))
        self.car.setStyleSheet("background-color: rgb(119, 255, 46);")
        self.car.setObjectName("car")
        self.fem = QtWidgets.QPushButton(main)
        self.fem.setGeometry(QtCore.QRect(360, 170, 81, 81))
        self.fem.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.fem.setObjectName("fem")
        self.podar = QtWidgets.QPushButton(main)
        self.podar.setGeometry(QtCore.QRect(500, 170, 81, 81))
        self.podar.setStyleSheet("background-color: rgb(53, 161, 255);")
        self.podar.setObjectName("podar")
        self.credit = QtWidgets.QPushButton(main)
        self.credit.setGeometry(QtCore.QRect(60, 280, 81, 81))
        self.credit.setStyleSheet("background-color: rgb(53, 161, 255);")
        self.credit.setObjectName("credit")
        self.chill = QtWidgets.QPushButton(main)
        self.chill.setGeometry(QtCore.QRect(210, 280, 81, 81))
        self.chill.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.chill.setObjectName("chill")
        self.worse = QtWidgets.QPushButton(main)
        self.worse.setGeometry(QtCore.QRect(360, 280, 81, 81))
        self.worse.setStyleSheet("background-color: rgb(255, 32, 35);")
        self.worse.setObjectName("worse")
        self.other = QtWidgets.QPushButton(main)
        self.other.setGeometry(QtCore.QRect(500, 280, 81, 81))
        self.other.setStyleSheet("background-color: rgb(119, 255, 46);")
        self.other.setObjectName("other")
        self.today = QtWidgets.QPushButton(main)
        self.today.setGeometry(QtCore.QRect(20, 440, 151, 71))
        self.today.setStyleSheet("background-color: rgb(255, 247, 0);")
        self.today.setObjectName("today")
        self.yesterday = QtWidgets.QPushButton(main)
        self.yesterday.setGeometry(QtCore.QRect(190, 440, 141, 71))
        self.yesterday.setStyleSheet("background-color: rgb(202, 42, 255);")
        self.yesterday.setObjectName("yesterday")
        self.the_day_before_yesterday = QtWidgets.QPushButton(main)
        self.the_day_before_yesterday.setGeometry(QtCore.QRect(360, 440, 141, 71))
        self.the_day_before_yesterday.setStyleSheet("background-color: rgb(255, 166, 166);")
        self.the_day_before_yesterday.setObjectName("the_day_before_yesterday")
        self.another_day = QtWidgets.QPushButton(main)
        self.another_day.setGeometry(QtCore.QRect(520, 440, 71, 71))
        self.another_day.setStyleSheet("background-color: rgb(131, 255, 197);")
        self.another_day.setObjectName("another_day")
        self.coments = QtWidgets.QTextEdit(main)
        self.coments.setGeometry(QtCore.QRect(10, 620, 601, 61))
        self.coments.setObjectName("coments")
        self.next = QtWidgets.QPushButton(main)
        self.next.setGeometry(QtCore.QRect(180, 720, 241, 51))
        self.next.setStyleSheet("background-color: rgb(144, 240, 147);")
        self.next.setObjectName("next")
        self.label_3 = QtWidgets.QLabel(main)
        self.label_3.setGeometry(QtCore.QRect(90, 110, 451, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(main)
        self.label_4.setGeometry(QtCore.QRect(90, 380, 451, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(main)
        self.label_5.setGeometry(QtCore.QRect(70, 560, 451, 51))
        self.label_5.setObjectName("label_5")
        self.error = QtWidgets.QLabel(main)
        self.error.setGeometry(QtCore.QRect(10, 789, 601, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.error.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.error.setFont(font)
        self.error.setObjectName("error")

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Form"))
        self.label.setText(_translate("main", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Введите сумму транкзакции:</span></p></body></html>"))
        self.summa.setHtml(_translate("main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.eat.setText(_translate("main", "еда"))
        self.car.setText(_translate("main", "Трансопрт"))
        self.fem.setText(_translate("main", "Семья"))
        self.podar.setText(_translate("main", "Подарки"))
        self.credit.setText(_translate("main", "Кредит"))
        self.chill.setText(_translate("main", "Развлечения"))
        self.worse.setText(_translate("main", "Вредные привычки"))
        self.other.setText(_translate("main", "Другое"))
        self.today.setText(_translate("main", "Сегодня"))
        self.yesterday.setText(_translate("main", "Вчера"))
        self.the_day_before_yesterday.setText(_translate("main", "позавчера"))
        self.another_day.setText(_translate("main", "другая"))
        self.next.setText(_translate("main", "Добваить"))
        self.label_3.setText(_translate("main", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Нажмите на нужную вам категорию</span></p></body></html>"))
        self.label_4.setText(_translate("main", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Нажмите на нужную вам дату</span></p></body></html>"))
        self.label_5.setText(_translate("main", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Введите коментарий</span></p></body></html>"))
        self.error.setText(_translate("main", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))