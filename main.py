import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        self.conn = sqlite3.connect("coffee.sqlite")
        self.cursor = self.conn.cursor()

        self.load_data()

    def load_data(self):
        self.cursor.execute("SELECT * FROM coffee")
        data = self.cursor.fetchall()

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(7)

        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Название", "Степень обжарки", "Молотый/в зернах", "Описание вкуса", "Цена", "Объем упаковки"]
        )

        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget.setItem(row_num, col_num, item)

    def closeEvent(self, event):
        self.conn.close()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
