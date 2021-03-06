from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 235)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.add_button.clicked.connect(Dialog.accept)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавить элемент"))
        self.label_2.setText(_translate("Dialog", "Название"))
        self.label_5.setText(_translate("Dialog", "Год выпуска"))
        self.label_4.setText(_translate("Dialog", "Жанр"))
        self.label_3.setText(_translate("Dialog", "Длина"))
        self.error.setText(_translate("Dialog", "error"))
        self.add_button.setText(_translate("Dialog", "Добавить"))


class DialogAdd(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)