# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dop.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.photo = QtWidgets.QLabel(Form)
        self.photo.setText("")
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.photo.setObjectName("photo")
        self.verticalLayout.addWidget(self.photo)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setIndent(-1)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.tilr = QtWidgets.QLabel(Form)
        self.tilr.setText("")
        self.tilr.setAlignment(QtCore.Qt.AlignCenter)
        self.tilr.setObjectName("tilr")
        self.verticalLayout.addWidget(self.tilr)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.year = QtWidgets.QLabel(Form)
        self.year.setText("")
        self.year.setAlignment(QtCore.Qt.AlignCenter)
        self.year.setObjectName("year")
        self.verticalLayout.addWidget(self.year)
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.genre = QtWidgets.QLabel(Form)
        self.genre.setText("")
        self.genre.setAlignment(QtCore.Qt.AlignCenter)
        self.genre.setObjectName("genre")
        self.verticalLayout.addWidget(self.genre)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "????????????????"))
        self.label_5.setText(_translate("Form", "??????????"))
        self.label_4.setText(_translate("Form", "?????? ??????????????"))
        self.label.setText(_translate("Form", "????????"))
