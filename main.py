import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QMessageBox


class AddEditCoffeeForm(QDialog):
    def __init__(self, parent=None, coffee_id=None):
        super().__init__(parent)
        uic.loadUi("addEditCoffeeForm.ui", self)

        self.coffee_id = coffee_id
        self.parent = parent

        self.saveButton.clicked.connect(self.save_data)
        self.cancelButton.clicked.connect(self.close)

        if self.coffee_id:
            self.load_data()

    def load_data(self):
        self.parent.cursor.execute("SELECT * FROM coffee WHERE id = ?", (self.coffee_id,))
        data = self.parent.cursor.fetchone()

        self.nameInput.setText(data[1])
        self.roastLevelInput.setText(data[2])
        self.grindTypeInput.setCurrentText(data[3])
        self.tasteDescriptionInput.setText(data[4])
        self.priceInput.setText(str(data[5]))
        self.packageVolumeInput.setText(str(data[6]))

    def save_data(self):
        name = self.nameInput.text()
        roast_level = self.roastLevelInput.text()
        grind_type = self.grindTypeInput.currentText()
        taste_description = self.tasteDescriptionInput.text()
        price = float(self.priceInput.text())
        package_volume = float(self.packageVolumeInput.text())

        if self.coffee_id:
            self.parent.cursor.execute(
                "UPDATE coffee SET name = ?, roast_level = ?, grind_type = ?, taste_description = ?, price = ?, "
                "package_volume = ? WHERE id = ?",
                (name, roast_level, grind_type, taste_description, price, package_volume, self.coffee_id)
            )
        else:
            self.parent.cursor.execute(
                "INSERT INTO coffee (name, roast_level, grind_type, taste_description, price, package_volume) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (name, roast_level, grind_type, taste_description, price, package_volume)
            )

        self.parent.conn.commit()
        self.parent.load_data()
        self.close()


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        self.conn = sqlite3.connect("coffee.sqlite")
        self.cursor = self.conn.cursor()

        self.load_data()

        self.addButton.clicked.connect(self.open_add_form)
        self.editButton.clicked.connect(self.open_edit_form)

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

    def open_add_form(self):
        form = AddEditCoffeeForm(self)
        form.exec()

    def open_edit_form(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Ошибка", "Выберите запись для редактирования.")
            return

        coffee_id = int(self.tableWidget.item(selected_row, 0).text())

        form = AddEditCoffeeForm(self, coffee_id)
        form.exec()

    def closeEvent(self, event):
        self.conn.close()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
