# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 90, 1261, 571))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 15, 241, 31))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setObjectName("label_2")
        self.grupoVerDatos = QtWidgets.QGroupBox(self.groupBox)
        self.grupoVerDatos.setGeometry(QtCore.QRect(800, 120, 451, 441))
        self.grupoVerDatos.setObjectName("grupoVerDatos")
        self.tableWidget = QtWidgets.QTableWidget(self.grupoVerDatos)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 431, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.linePuntoX = QtWidgets.QLineEdit(self.groupBox)
        self.linePuntoX.setGeometry(QtCore.QRect(940, 10, 61, 31))
        self.linePuntoX.setObjectName("linePuntoX")
        self.linePuntoY = QtWidgets.QLineEdit(self.groupBox)
        self.linePuntoY.setGeometry(QtCore.QRect(1010, 10, 61, 31))
        self.linePuntoY.setObjectName("linePuntoY")
        self.btnPredecirPunto = QtWidgets.QPushButton(self.groupBox)
        self.btnPredecirPunto.setGeometry(QtCore.QRect(940, 50, 131, 31))
        self.btnPredecirPunto.setObjectName("btnPredecirPunto")
        self.grupoArmarGrid = QtWidgets.QGroupBox(self.groupBox)
        self.grupoArmarGrid.setGeometry(QtCore.QRect(290, 10, 501, 111))
        self.grupoArmarGrid.setObjectName("grupoArmarGrid")
        self.checkRejilla = QtWidgets.QCheckBox(self.grupoArmarGrid)
        self.checkRejilla.setGeometry(QtCore.QRect(10, 20, 101, 17))
        self.checkRejilla.setObjectName("checkRejilla")
        self.radioCirculo = QtWidgets.QRadioButton(self.grupoArmarGrid)
        self.radioCirculo.setGeometry(QtCore.QRect(240, 20, 161, 17))
        self.radioCirculo.setObjectName("radioCirculo")
        self.radioCuadrado = QtWidgets.QRadioButton(self.grupoArmarGrid)
        self.radioCuadrado.setGeometry(QtCore.QRect(240, 40, 241, 17))
        self.radioCuadrado.setObjectName("radioCuadrado")
        self.checkRA = QtWidgets.QCheckBox(self.grupoArmarGrid)
        self.checkRA.setGeometry(QtCore.QRect(10, 40, 171, 17))
        self.checkRA.setObjectName("checkRA")
        self.checkCelda = QtWidgets.QCheckBox(self.grupoArmarGrid)
        self.checkCelda.setGeometry(QtCore.QRect(10, 60, 171, 17))
        self.checkCelda.setObjectName("checkCelda")
        self.lineCelda = QtWidgets.QLineEdit(self.grupoArmarGrid)
        self.lineCelda.setGeometry(QtCore.QRect(190, 60, 31, 20))
        self.lineCelda.setObjectName("lineCelda")
        self.grupoTest = QtWidgets.QGroupBox(self.groupBox)
        self.grupoTest.setGeometry(QtCore.QRect(10, 120, 781, 441))
        self.grupoTest.setObjectName("grupoTest")
        self.grupoTestMetodo = QtWidgets.QGroupBox(self.grupoTest)
        self.grupoTestMetodo.setGeometry(QtCore.QRect(320, 80, 461, 351))
        self.grupoTestMetodo.setObjectName("grupoTestMetodo")
        self.txtMejorK = QtWidgets.QPlainTextEdit(self.grupoTestMetodo)
        self.txtMejorK.setGeometry(QtCore.QRect(10, 100, 441, 241))
        self.txtMejorK.setObjectName("txtMejorK")
        self.radioElbow = QtWidgets.QRadioButton(self.grupoTestMetodo)
        self.radioElbow.setGeometry(QtCore.QRect(10, 20, 221, 17))
        self.radioElbow.setObjectName("radioElbow")
        self.radioRaiz = QtWidgets.QRadioButton(self.grupoTestMetodo)
        self.radioRaiz.setGeometry(QtCore.QRect(10, 40, 211, 17))
        self.radioRaiz.setObjectName("radioRaiz")
        self.btnGraficoMetodo = QtWidgets.QPushButton(self.grupoTestMetodo)
        self.btnGraficoMetodo.setGeometry(QtCore.QRect(230, 60, 210, 31))
        self.btnGraficoMetodo.setObjectName("btnGraficoMetodo")
        self.btnTestMetodo = QtWidgets.QPushButton(self.grupoTestMetodo)
        self.btnTestMetodo.setGeometry(QtCore.QRect(10, 60, 210, 31))
        self.btnTestMetodo.setObjectName("btnTestMetodo")
        self.grupoTestUsuario = QtWidgets.QGroupBox(self.grupoTest)
        self.grupoTestUsuario.setGeometry(QtCore.QRect(10, 80, 301, 351))
        self.grupoTestUsuario.setObjectName("grupoTestUsuario")
        self.btnTestUsuario = QtWidgets.QPushButton(self.grupoTestUsuario)
        self.btnTestUsuario.setGeometry(QtCore.QRect(10, 60, 131, 31))
        self.btnTestUsuario.setObjectName("btnTestUsuario")
        self.txtTest = QtWidgets.QPlainTextEdit(self.grupoTestUsuario)
        self.txtTest.setGeometry(QtCore.QRect(10, 100, 281, 241))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtTest.setFont(font)
        self.txtTest.setObjectName("txtTest")
        self.spinKUsuario = QtWidgets.QSpinBox(self.grupoTestUsuario)
        self.spinKUsuario.setGeometry(QtCore.QRect(160, 20, 42, 22))
        self.spinKUsuario.setMinimum(1)
        self.spinKUsuario.setMaximum(10)
        self.spinKUsuario.setObjectName("spinKUsuario")
        self.labelKTest = QtWidgets.QLabel(self.grupoTestUsuario)
        self.labelKTest.setGeometry(QtCore.QRect(10, 20, 131, 31))
        self.labelKTest.setObjectName("labelKTest")
        self.btnGraficoUsuario = QtWidgets.QPushButton(self.grupoTestUsuario)
        self.btnGraficoUsuario.setGeometry(QtCore.QRect(150, 60, 141, 31))
        self.btnGraficoUsuario.setObjectName("btnGraficoUsuario")
        self.labelTest = QtWidgets.QLabel(self.grupoTest)
        self.labelTest.setGeometry(QtCore.QRect(10, 50, 171, 16))
        self.labelTest.setObjectName("labelTest")
        self.labelTest_2 = QtWidgets.QLabel(self.grupoTest)
        self.labelTest_2.setGeometry(QtCore.QRect(190, 50, 51, 21))
        self.labelTest_2.setObjectName("labelTest_2")
        self.labelEntrenamiento = QtWidgets.QLabel(self.grupoTest)
        self.labelEntrenamiento.setGeometry(QtCore.QRect(10, 20, 171, 21))
        self.labelEntrenamiento.setObjectName("labelEntrenamiento")
        self.spinEntrenamiento = QtWidgets.QSpinBox(self.grupoTest)
        self.spinEntrenamiento.setGeometry(QtCore.QRect(190, 20, 42, 22))
        self.spinEntrenamiento.setMinimum(1)
        self.spinEntrenamiento.setMaximum(99)
        self.spinEntrenamiento.setObjectName("spinEntrenamiento")
        self.btnComparacion = QtWidgets.QPushButton(self.grupoTest)
        self.btnComparacion.setGeometry(QtCore.QRect(480, 10, 291, 71))
        self.btnComparacion.setObjectName("btnComparacion")
        self.labelElementos = QtWidgets.QLabel(self.groupBox)
        self.labelElementos.setGeometry(QtCore.QRect(20, 60, 121, 21))
        self.labelElementos.setObjectName("labelElementos")
        self.labelClases = QtWidgets.QLabel(self.groupBox)
        self.labelClases.setGeometry(QtCore.QRect(20, 90, 111, 16))
        self.labelClases.setObjectName("labelClases")
        self.lineElementos = QtWidgets.QLineEdit(self.groupBox)
        self.lineElementos.setGeometry(QtCore.QRect(170, 60, 111, 20))
        self.lineElementos.setObjectName("lineElementos")
        self.lineClases = QtWidgets.QLineEdit(self.groupBox)
        self.lineClases.setGeometry(QtCore.QRect(170, 90, 113, 20))
        self.lineClases.setObjectName("lineClases")
        self.abrirDataset = QtWidgets.QPushButton(self.centralwidget)
        self.abrirDataset.setGeometry(QtCore.QRect(10, 10, 151, 41))
        self.abrirDataset.setObjectName("abrirDataset")
        self.comboSeparador = QtWidgets.QComboBox(self.centralwidget)
        self.comboSeparador.setGeometry(QtCore.QRect(60, 50, 100, 20))
        self.comboSeparador.setObjectName("comboSeparador")
        self.labelSeparador = QtWidgets.QLabel(self.centralwidget)
        self.labelSeparador.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.labelSeparador.setObjectName("labelSeparador")
        self.barraProgreso = QtWidgets.QProgressBar(self.centralwidget)
        self.barraProgreso.setGeometry(QtCore.QRect(870, 60, 231, 31))
        self.barraProgreso.setProperty("value", 0)
        self.barraProgreso.setObjectName("barraProgreso")
        self.lblCargaTexto = QtWidgets.QLabel(self.centralwidget)
        self.lblCargaTexto.setGeometry(QtCore.QRect(270, 10, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblCargaTexto.setFont(font)
        self.lblCargaTexto.setObjectName("lblCargaTexto")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNuevo_Proyecto = QtWidgets.QAction(MainWindow)
        self.actionNuevo_Proyecto.setObjectName("actionNuevo_Proyecto")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Dataset"))
        self.label.setText(_translate("MainWindow", "Ruta"))
        self.label_2.setText(_translate("MainWindow", "No se ha seleccionado ningún dataset"))
        self.grupoVerDatos.setTitle(_translate("MainWindow", "Datos"))
        self.btnPredecirPunto.setText(_translate("MainWindow", "Predecir clase del punto"))
        self.grupoArmarGrid.setTitle(_translate("MainWindow", "Parámetros de gráfico"))
        self.checkRejilla.setText(_translate("MainWindow", "Dibujar rejilla"))
        self.radioCirculo.setText(_translate("MainWindow", "Círculos (método alternativo)"))
        self.radioCuadrado.setText(_translate("MainWindow", "Cuadrados (método propuesto por la cátedra)"))
        self.checkRA.setText(_translate("MainWindow", "Activar relación de aspecto 1:1"))
        self.checkCelda.setText(_translate("MainWindow", "Tamaño de celda personalizado"))
        self.grupoTest.setTitle(_translate("MainWindow", "Testear precisión"))
        self.grupoTestMetodo.setTitle(_translate("MainWindow", "Método para estimar K"))
        self.radioElbow.setText(_translate("MainWindow", "Método del Codo (Elbow)"))
        self.radioRaiz.setText(_translate("MainWindow", "Método de la raíz cuadrada"))
        self.btnGraficoMetodo.setText(_translate("MainWindow", "Visualizar Gráfico con K calculado"))
        self.btnTestMetodo.setText(_translate("MainWindow", "Calcular K y Testear modelo"))
        self.grupoTestUsuario.setTitle(_translate("MainWindow", "K definido por el usuario"))
        self.btnTestUsuario.setText(_translate("MainWindow", "Testear Modelo"))
        self.labelKTest.setText(_translate("MainWindow", "Valor máximo de K"))
        self.btnGraficoUsuario.setText(_translate("MainWindow", "Visualizar Gráfico con máx K"))
        self.labelTest.setText(_translate("MainWindow", "Porcentaje de Test"))
        self.labelTest_2.setText(_translate("MainWindow", "TextLabel"))
        self.labelEntrenamiento.setText(_translate("MainWindow", "Porcentaje de Entrenamiento"))
        self.btnComparacion.setText(_translate("MainWindow", "Comparar gráficos"))
        self.labelElementos.setText(_translate("MainWindow", "Cantidad de elementos"))
        self.labelClases.setText(_translate("MainWindow", "Cantidad de clases"))
        self.abrirDataset.setText(_translate("MainWindow", "Abrir Dataset"))
        self.labelSeparador.setText(_translate("MainWindow", "Separador"))
        self.lblCargaTexto.setText(_translate("MainWindow", "Generando gráficos\n"
"Esta operación podría tardar. Por favor espere..."))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNuevo_Proyecto.setText(_translate("MainWindow", "Abrir Dataset"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
