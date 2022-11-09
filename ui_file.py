from pathlib import Path


def open_database():
    # сохраняем базу в директорию пользователя
    db_folder = Path.home()
    db_folder = db_folder / f'{1234}'
    print(str(db_folder))


open_database()
