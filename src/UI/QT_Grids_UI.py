# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_Grids.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 600)
        self.graphUsuario = QtWidgets.QGraphicsView(Form)
        self.graphUsuario.setGeometry(QtCore.QRect(10, 40, 480, 480))
        self.graphUsuario.setObjectName("graphUsuario")
        self.graphMejor = QtWidgets.QGraphicsView(Form)
        self.graphMejor.setGeometry(QtCore.QRect(530, 40, 480, 480))
        self.graphMejor.setObjectName("graphMejor")
        self.btnProx = QtWidgets.QPushButton(Form)
        self.btnProx.setGeometry(QtCore.QRect(280, 540, 48, 48))
        self.btnProx.setObjectName("btnProx")
        self.btnAnt = QtWidgets.QPushButton(Form)
        self.btnAnt.setGeometry(QtCore.QRect(170, 540, 48, 48))
        self.btnAnt.setObjectName("btnAnt")
        self.lblUsuario = QtWidgets.QLabel(Form)
        self.lblUsuario.setGeometry(QtCore.QRect(200, 525, 47, 13))
        self.lblUsuario.setObjectName("lblUsuario")
        self.lblMejor = QtWidgets.QLabel(Form)
        self.lblMejor.setGeometry(QtCore.QRect(750, 525, 47, 13))
        self.lblMejor.setObjectName("lblMejor")
        self.lineUsuario = QtWidgets.QLineEdit(Form)
        self.lineUsuario.setGeometry(QtCore.QRect(220, 520, 32, 20))
        self.lineUsuario.setReadOnly(True)
        self.lineUsuario.setObjectName("lineUsuario")
        self.lineMejor = QtWidgets.QLineEdit(Form)
        self.lineMejor.setGeometry(QtCore.QRect(770, 520, 32, 20))
        self.lineMejor.setReadOnly(True)
        self.lineMejor.setObjectName("lineMejor")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnProx.setText(_translate("Form", "→"))
        self.btnAnt.setText(_translate("Form", "←"))
        self.lblUsuario.setText(_translate("Form", "K = "))
        self.lblMejor.setText(_translate("Form", "K = "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
