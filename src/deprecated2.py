import datetime
import os
import sys
#import logging
#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
from archivo import Archivo
from datos import Datos
from core import vecinos
from core import distancia
from core import prediccion
from core import predecirClase
from core import predecirClaseConCalidad

from copy import deepcopy

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem

from matplotlib import pyplot
from matplotlib import colors
import matplotlib.patches as mpatches

from QT_Main_UI import *

import random
from math import sqrt

from hilos import Worker
from hilos import WorkerSignals

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QRunnable, QThreadPool,pyqtSlot, pyqtSignal

#from PyQt5.QtGui import *
#from PyQt5.QtWidgets import *
#from PyQt5.QtCore import *

import time

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        #Inicializando botones y esas weas
        self.threadpool = QThreadPool()
        
        self.txtTest.setReadOnly(True)
        self.txtMejorK.setReadOnly(True)
        self.lineElementos.setReadOnly(True)
        self.lineClases.setReadOnly(True)
        self.labelTest_2.setText(str(30))
        self.spinEntrenamiento.setValue(70)
        self.spinKUsuario.setValue(10)
        self.groupBox.setEnabled(False)
        self.radioCuadrado.setChecked(True)
        self.radioElbow.setChecked(True)
        self.btnDetener.setEnabled(False)
        self.barraProgreso.setEnabled(False)

        self.comboSeparador.addItems([';',',','Tab','Espacio'])

        self.separadores = {',':',',';':';','Tab':'\t','Espacio':' '}

        self.porcentajeEntrenamiento = 70
        self.porcentajeTest = 30

        self.diccionario = {}
        self.datos = None
        self.resultadosTestMetodo = list()
        self.resultadosTestUsuario = list()

        #fecha = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        self.colores = list()
        self.ladoDeUnCuadrado = 0.5
        self.numero_de_divisiones = 70 #El video mostraba ~68
        self.kDeTest = 1

        self.label_2.setText('No se ha seleccionado ningún archivo')

        self.abrirDataset.clicked.connect(self.abrirArchivo)

        self.btnTestUsuario.clicked.connect(self.testearModeloUsuario)
        self.btnGraficoUsuario.clicked.connect(self.graficarUsuario)
        self.btnTestMetodo.clicked.connect(self.testearModeloMetodo)
        self.btnGraficoMetodo.clicked.connect(self.graficarMetodo)

        self.btnPredecirPunto.clicked.connect(self.predecirPunto)
        
        self.spinEntrenamiento.valueChanged.connect(self.cambiarPorcentajes)

        #Inicializar widgets
    def progress_fn(self,n):
        self.barraProgreso.setValue(n)
    def execute_this_fn(self, progress_callback):
        for n in range(0, 5):
            time.sleep(1)
            progress_callback.emit(n*100/4)
            
        return "Done."
    def print_output(self, s):
        print('')
        
    def finTestMetodo(self):
        for resultado in self.resultadosTestMetodo:
            self.txtMejorK.insertPlainText("Con K = " + str(resultado[0]) + ", la eficacia fue de " + "{:.2f}".format(resultado[1]) + "% \n")
    def finTestUsuario(self):
        for resultado in self.resultadosTestUsuario:
            self.txtTest.insertPlainText("Con K = " + str(resultado[0]) + ", la eficacia fue de " + "{:.2f}".format(resultado[1]) + "% \n")

    #☺def recurring_timer(self):
        #self.counter +=1
        #self.l.setText("Counter: %d" % self.counter)

    def hiloTestearModeloMetodo(self,progress_callback):
        puntosDeEntrenamiento = self.datos.obtenerDatosEntrenamiento(self.porcentajeEntrenamiento)
        puntosDeTest = self.datos.obtenerDatosTest(self.porcentajeEntrenamiento)

        self.resultadosTestMetodo = list()
        aciertos = 0
        totalElementos = 0
        k = self.kDeTest
        total = len(puntosDeTest)
        for puntoDeTest in puntosDeTest:
            loskvecinos = vecinos(puntosDeEntrenamiento,puntoDeTest,k)
            claseDelPunto = prediccion (puntoDeTest,loskvecinos)
            totalElementos = totalElementos + 1
            if (claseDelPunto==puntoDeTest[-1]):
                aciertos = aciertos + 1
            progreso = totalElementos
            n = int((progreso*100)/total)
            progress_callback.emit(n)
        porcentajeDeAciertos = (aciertos / totalElementos) * 100
        self.resultadosTestMetodo.append((k,porcentajeDeAciertos))
    
    def testearModeloMetodo(self):
        self.txtMejorK.clear()
        self.barraProgreso.setValue(0)
        self.kDeTest = self.obtenerMejorK()
        worker = Worker(self.hiloTestearModeloMetodo) # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.finTestMetodo)
        worker.signals.progress.connect(self.progress_fn)
        # Execute
        self.threadpool.start(worker) 
    def hiloTestearModeloUsuario(self,progress_callback):
        puntosDeEntrenamiento = self.datos.obtenerDatosEntrenamiento(self.porcentajeEntrenamiento)
        puntosDeTest = self.datos.obtenerDatosTest(self.porcentajeEntrenamiento)

        self.resultadosTestUsuario = list()
        k = self.obtenerValorDeK()+1
        for i in range(1,k + 1):
            aciertos = 0
            totalElementos = 0
            #TODO: mostrar en una tabla los resultados, por ejemplo
            #clasesPredichas = list()
            #clasesReales = list()
            for puntoDeTest in puntosDeTest:
                loskvecinos = vecinos(puntosDeEntrenamiento,puntoDeTest,i)
                claseDelPunto = prediccion (puntoDeTest,loskvecinos)
                totalElementos = totalElementos + 1
                if (claseDelPunto==puntoDeTest[-1]):
                    aciertos = aciertos + 1
            porcentajeDeAciertos = (aciertos / totalElementos) * 100
            self.resultadosTestUsuario.append((i,porcentajeDeAciertos))
            #self.progress_fn(i,k)
            n = int((i*100)/k)
            progress_callback.emit(n)
        #for resultado in resultados:
            #self.txtTest.insertPlainText("Con K = " + str(resultado[0]) + ", la eficacia fue de " + "{:.2f}".format(resultado[1]) + "% \n")
            #TODO: esto no debería pasar porque están en hilos distintos
        #self.archivo.datosDeEntrenamiento(self.porcentajeEntrenamiento)
        #pyplot.plot(self.archivo.datosEntrenamientoX,self.archivo.datosEntrenamientoY,'go')
        #pyplot.show()
    def testearModeloUsuario(self):
        self.txtTest.clear()
        self.barraProgreso.setValue(0)
        worker = Worker(self.hiloTestearModeloUsuario) # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.finTestUsuario)
        worker.signals.progress.connect(self.progress_fn)
        # Execute
        self.threadpool.start(worker)  
        
    def predecirPunto(self):
        self.txtTest.clear()

        mipunto = list()
        mipunto.append(float(self.linePuntoX.text()))
        mipunto.append(float(self.linePuntoY.text()))
        
        #puntosDeEntrenamiento = self.datos.obtenerDatosEntrenamiento(self.porcentajeEntrenamiento)
        #puntosDeTest = self.datos.obtenerDatosTest(self.porcentajeEntrenamiento)
        for i in range(1,11):
            loskvecinos = vecinos(self.datos.datosCompletos,mipunto,i)
            #print("Para " + str(i) + " vecinos sus vecinos más cercanos son:")
            #print(loskvecinos)
            claseDelPunto = prediccion (mipunto,loskvecinos)
            #print("La clase predicha fue " + claseDelPunto)
            self.txtTest.insertPlainText("Con " +str(i) + " vecinos, la clase predicha fue " + claseDelPunto + "\n")
        #self.archivo.datosDeEntrenamiento(self.porcentajeEntrenamiento)
        #pyplot.plot(self.archivo.datosEntrenamientoX,self.archivo.datosEntrenamientoY,'go')
        #pyplot.show()      
    def cambiarPorcentajes(self):
        self.porcentajeEntrenamiento = self.spinEntrenamiento.value()
        self.porcentajeTest = 100 - self.spinEntrenamiento.value()
        self.labelTest_2.setText(str(self.porcentajeTest))

    def cambiarKUsuario(self):
        self.valorDeK = self.spinKUsuario.value()

    def abrirArchivo(self):
        options = QFileDialog.Options()
        ruta_de_archivo, _ = QFileDialog.getOpenFileName(self, "Abrir Dataset", "",
                                                 "Archivos de texto (*.txt);; Archivos CSV (*.CSV)", options=options)
        if ruta_de_archivo:
            self.label_2.setText(ruta_de_archivo)
            self.archivo = Archivo(ruta_de_archivo)
            self.archivo.abrir(self.separadores[self.comboSeparador.currentText()])
            self.groupBox.setEnabled(True)
            self.btnDetener.setEnabled(True)
            self.barraProgreso.setEnabled(True)
            self.txtTest.clear()
            self.txtMejorK.clear()

            self.valorDeK = 7

            #print("datos del archivo")
            #print(self.archivo.datos)
            self.datos = Datos()

            self.datos.generar(deepcopy(self.archivo.datos))

            #print("datos del archivo")
            #print(self.archivo.datos)

            self.tableWidget.setColumnCount(self.archivo.numcolumnas)
            self.tableWidget.setRowCount(self.archivo.numfilas)
            self.tableWidget.setHorizontalHeaderLabels(self.archivo.columnas)
            self.lineClases.setText(str(self.datos.obtenerNumeroDeClases()))
            self.lineElementos.setText(str(self.datos.obtenerCantidad()))

            
            for fila in range(self.archivo.numfilas):
                for columna in range(self.archivo.numcolumnas):
                    self.tableWidget.setItem(fila, columna, QTableWidgetItem((self.archivo.datos[fila][columna])))

        else:
            self.label_2.setText("No se ha seleccionado ningún archivo")
            self.groupBox.setEnabled(False)
            self.btnDetener.setEnabled(False)
            self.barraProgreso.setEnabled(False)
    def obtenerValorDeK(self):
        return int(self.spinKUsuario.value())
    def obtenerMejorK(self):
        if (self.radioRaiz.isChecked()):
            return self.calcularKRaiz()
        else:
            return self.calcularKElbow()

    def calcularKRaiz(self):
        k = int(sqrt(self.datos.obtenerCantidad()))
        if (((k % 2) == 0) and (((self.datos.obtenerNumeroDeClases())%2)==0)):
            k = k + 1
        return k

    def finCalcularKElbow(self):
        self.txtMejorK.insertPlainText("Se ha detectado un k óptimo igual a " + str(self.kDeTest) + "\n ------------- \n")
    def progresoCalcularKElbow(self,n):
        self.txtMejorK.insertPlainText('Analizando K = ' + str(n) + "\n")
    def calcularKElbow(self):
        self.txtMejorK.clear()
        worker = Worker(self.hiloCalcularKElbow) # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.finCalcularKElbow)
        worker.signals.progress.connect(self.progresoCalcularKElbow)
        # Execute
        self.threadpool.start(worker) 
    def hiloCalcularKElbow(self,progress_callback):
        puntosDeEntrenamiento = self.datos.obtenerDatosEntrenamiento(self.porcentajeEntrenamiento)
        puntosDeTest = self.datos.obtenerDatosTest(self.porcentajeEntrenamiento)

        self.resultadosTestMetodo = list()
        aciertos = 0
        totalElementos = 0
        k = 1
        mejorK = 1
        fin = False
        mejorValor = 0
        j = 0

        while (not fin):
            progress_callback.emit(k)
            aciertos = 0
            totalElementos = 0
            for puntoDeTest in puntosDeTest:
                loskvecinos = vecinos(puntosDeEntrenamiento,puntoDeTest,k)
                claseDelPunto = prediccion (puntoDeTest,loskvecinos)
                totalElementos = totalElementos + 1
                if (claseDelPunto==puntoDeTest[-1]):
                    aciertos = aciertos + 1
            porcentajeDeAciertos = (aciertos / totalElementos) * 100
            self.resultadosTestMetodo.append((k,porcentajeDeAciertos))
            if (porcentajeDeAciertos>mejorValor):
                mejorValor = porcentajeDeAciertos
                mejorK = k
                j = 0
            else:
                j = j + 1
            if ((j>10) or (porcentajeDeAciertos==100) or (k>30)):
                fin = True
            else:
                k = k + 1           
        #for resultado in resultados:
            #self.txtMejorK.insertPlainText("Con K = " + str(resultado[0]) + ", la eficacia fue de " + "{:.2f}".format(resultado[1]) + "% \n")
        self.kDeTest = mejorK
        return mejorK
    def obtenerRejilla(self):
        return (self.checkRejilla.isChecked())
    def insertarGrid(self,grafico,ejes,limiteInferiorX,limiteSuperiorX,limiteInferiorY,limiteSuperiorY,k,salto):
        #¶coordenadas = list()
        cuadrados = []
        x = limiteInferiorX
        y = limiteInferiorY
        random.seed(datetime.datetime.now())

        xDePrueba = x + self.ladoDeUnCuadrado/2
        yDePrueba = y + self.ladoDeUnCuadrado/2
        while(y<limiteSuperiorY):
            x = limiteInferiorX
            xDePrueba = x + self.ladoDeUnCuadrado/2
            while(x<limiteSuperiorX):
                clase = predecirClase(self.datos.datosCompletos,(xDePrueba,yDePrueba),k)
                color = self.diccionario[clase]
                cuadrado = mpatches.Rectangle((x,y),self.ladoDeUnCuadrado,self.ladoDeUnCuadrado,angle = 0.0,color=color, alpha=0.4,linewidth=0)
                #grafico.patches.extend([pyplot.Rectangle((x,y),saltoDelCuadrado,saltoDelCuadrado,
                                  #fill=True, color=color, alpha=0.5, zorder=1000,
                                  #transform=grafico.transFigure, figure=grafico)])
                cuadrados.append(cuadrado)
                ejes.add_patch(cuadrado)
                x = x + self.ladoDeUnCuadrado
                xDePrueba = x + self.ladoDeUnCuadrado/2
            y = y + self.ladoDeUnCuadrado
            yDePrueba = y + self.ladoDeUnCuadrado/2
        #for c in cuadrados:
            #print(str(c) + "/n")
    def insertarCirculos(self,grafico,ejes,limiteInferiorX,limiteSuperiorX,limiteInferiorY,limiteSuperiorY,k,salto):
        #coordenadas = list()
        cuadrados = []
        x = limiteInferiorX
        y = limiteInferiorY
        random.seed(datetime.datetime.now())

        xDePrueba = x + self.ladoDeUnCuadrado/2
        yDePrueba = y + self.ladoDeUnCuadrado/2
        while(y<limiteSuperiorY):
            x = limiteInferiorX
            xDePrueba = x + self.ladoDeUnCuadrado/2
            while(x<limiteSuperiorX):
                clase = (predecirClaseConCalidad(self.datos.datosCompletos,(xDePrueba,yDePrueba),k))[0]
                calidad = (predecirClaseConCalidad(self.datos.datosCompletos,(xDePrueba,yDePrueba),k))[1]
                calidad = ((self.ladoDeUnCuadrado/2)*(calidad))
                color = self.diccionario[clase]
                cuadrado = mpatches.Circle((x+(self.ladoDeUnCuadrado/2),y+(self.ladoDeUnCuadrado/2)),radius=calidad,color=color, alpha=0.4,linewidth=0)
                #grafico.patches.extend([pyplot.Rectangle((x,y),saltoDelCuadrado,saltoDelCuadrado,
                                  #fill=True, color=color, alpha=0.5, zorder=1000,
                                  #transform=grafico.transFigure, figure=grafico)])
                cuadrados.append(cuadrado)
                ejes.add_patch(cuadrado)
                x = x + self.ladoDeUnCuadrado
                xDePrueba = x + self.ladoDeUnCuadrado/2
            y = y + self.ladoDeUnCuadrado
            yDePrueba = y + self.ladoDeUnCuadrado/2
        #for c in cuadrados:
            #print(str(c) + "/n")
    def graficarMetodo(self):
        k = self.obtenerMejorK()
        self.graficarDataset(k)
    def graficarUsuario(self):
        k = self.obtenerValorDeK()
        self.graficarDataset(k)

    def graficarDataset(self,k):
        valorDeSeparacionX = (self.datos.maxX()-self.datos.minX())*0.1
        valorDeSeparacionY = (self.datos.maxY()-self.datos.minY())*0.1
        limiteInferiorX = self.datos.minX() - valorDeSeparacionX
        limiteSuperiorX =self.datos.maxX() + valorDeSeparacionX
        limiteInferiorY = self.datos.minY() - valorDeSeparacionY
        limiteSuperiorY =self.datos.maxY() + valorDeSeparacionY
        pyplot.clf()
        grafico = pyplot.figure(figsize=(8,8))
        ax = grafico.add_subplot()
        ax.plot(limiteInferiorX,limiteInferiorY)
        ax.set_aspect(1)
        if(len(self.datos.clases)>9):
            self.colores = colors.CSS4_COLORS
        else:
            self.colores = colors.TABLEAU_COLORS
        
        #divisionX = (self.datos.maxX() + valorDeSeparacionX - self.datos.minX() + valorDeSeparacionY) / (self.numero_de_divisiones)
        #divisionY = (self.datos.maxY() + valorDeSeparacionY - self.datos.minY() + valorDeSeparacionY) / (self.numero_de_divisiones)
        #print(divisionX)
        pyplot.xlim(limiteInferiorX,limiteSuperiorX)
        pyplot.ylim(limiteInferiorY,limiteSuperiorY)

        xDelBucle = limiteInferiorX
        yDelBucle = limiteInferiorY
        
        if(self.obtenerRejilla()):
            while(xDelBucle<limiteSuperiorX):
                pyplot.axvline(x = xDelBucle,linestyle = '-',marker = ",",linewidth=0.2)
                xDelBucle = xDelBucle + self.ladoDeUnCuadrado
            while(yDelBucle<limiteSuperiorY):
                pyplot.axhline(y = yDelBucle,linestyle = '-',marker = ",",linewidth=0.2)
                yDelBucle = yDelBucle + self.ladoDeUnCuadrado

        self.diccionario = {}
        i = 0
        lista = list(self.colores.items())
        for clase in self.datos.clases:
            self.diccionario[clase] = lista[i][0]
            i = i + 1
        for punto in self.datos.datosCompletos:
            pyplot.plot(punto[0],punto[1],marker = '.',color = self.diccionario[punto[2]])
        if (self.radioCuadrado.isChecked()==True):
            self.insertarGrid(grafico,ax,limiteInferiorX,limiteSuperiorX,limiteInferiorY,limiteSuperiorY,k,self.ladoDeUnCuadrado)
        else:
            self.insertarCirculos(grafico,ax,limiteInferiorX,limiteSuperiorX,limiteInferiorY,limiteSuperiorY,k,self.ladoDeUnCuadrado)
        #Crear cuadrados
        
        grafico.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
