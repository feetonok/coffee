# Form implementation generated from reading ui file 'UI/addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddEditCoffeeForm(object):
    def setupUi(self, AddEditCoffeeForm):
        AddEditCoffeeForm.setObjectName("AddEditCoffeeForm")
        AddEditCoffeeForm.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(AddEditCoffeeForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nameInput = QtWidgets.QLineEdit(parent=AddEditCoffeeForm)
        self.nameInput.setObjectName("nameInput")
        self.verticalLayout.addWidget(self.nameInput)
        self.roastLevelInput = QtWidgets.QLineEdit(parent=AddEditCoffeeForm)
        self.roastLevelInput.setObjectName("roastLevelInput")
        self.verticalLayout.addWidget(self.roastLevelInput)
        self.grindTypeInput = QtWidgets.QComboBox(parent=AddEditCoffeeForm)
        self.grindTypeInput.setObjectName("grindTypeInput")
        self.grindTypeInput.addItem("")
        self.grindTypeInput.addItem("")
        self.verticalLayout.addWidget(self.grindTypeInput)
        self.tasteDescriptionInput = QtWidgets.QLineEdit(parent=AddEditCoffeeForm)
        self.tasteDescriptionInput.setObjectName("tasteDescriptionInput")
        self.verticalLayout.addWidget(self.tasteDescriptionInput)
        self.priceInput = QtWidgets.QLineEdit(parent=AddEditCoffeeForm)
        self.priceInput.setObjectName("priceInput")
        self.verticalLayout.addWidget(self.priceInput)
        self.packageVolumeInput = QtWidgets.QLineEdit(parent=AddEditCoffeeForm)
        self.packageVolumeInput.setObjectName("packageVolumeInput")
        self.verticalLayout.addWidget(self.packageVolumeInput)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saveButton = QtWidgets.QPushButton(parent=AddEditCoffeeForm)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.cancelButton = QtWidgets.QPushButton(parent=AddEditCoffeeForm)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(AddEditCoffeeForm)
        QtCore.QMetaObject.connectSlotsByName(AddEditCoffeeForm)

    def retranslateUi(self, AddEditCoffeeForm):
        _translate = QtCore.QCoreApplication.translate
        AddEditCoffeeForm.setWindowTitle(_translate("AddEditCoffeeForm", "Добавить/Редактировать кофе"))
        self.nameInput.setPlaceholderText(_translate("AddEditCoffeeForm", "Название сорта"))
        self.roastLevelInput.setPlaceholderText(_translate("AddEditCoffeeForm", "Степень обжарки"))
        self.grindTypeInput.setItemText(0, _translate("AddEditCoffeeForm", "Молотый"))
        self.grindTypeInput.setItemText(1, _translate("AddEditCoffeeForm", "В зернах"))
        self.tasteDescriptionInput.setPlaceholderText(_translate("AddEditCoffeeForm", "Описание вкуса"))
        self.priceInput.setPlaceholderText(_translate("AddEditCoffeeForm", "Цена"))
        self.packageVolumeInput.setPlaceholderText(_translate("AddEditCoffeeForm", "Объем упаковки"))
        self.saveButton.setText(_translate("AddEditCoffeeForm", "Сохранить"))
        self.cancelButton.setText(_translate("AddEditCoffeeForm", "Отмена"))
