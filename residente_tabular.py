import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QTableWidgetItem, QTableWidget, QScrollArea

from consulta_datos import Consulta_datos
from lista_residente import Residente
from usuarios import Usuarios


class Residente_tabular(QMainWindow):
    def __init__(self, anterior):
        super().__init__()

        self.Anterior = anterior
        # creacion de la ventana
        self.setWindowTitle("Lista de residentes")
        self.setWindowIcon(QtGui.QIcon('imagenes/sophos.jpeg'))
        self.ancho = 800
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)
        self.fondo.setStyleSheet('background-color: qlineargradient(spread:pad, x1:0.71, y1:0.176045, x2:0.393, '
                                 'y2:0.643091, stop:0.159091 rgba(172, 172, 172, 255), stop:0.835227 rgba(210, 210, '
                                 '210, 255)); '
                                 '')

        self.setCentralWidget(self.fondo)

        # creacion de layout horizontal para la distribucion

        self.vertical = QVBoxLayout()

        # creacion de layout horizontal para la distribucion
        self.vertical = QVBoxLayout()

        self.file = open('datos/residente.txt', 'rb')
        self.usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')
            lista = linea.split(";")

            if linea == '':
                break

            u = Residente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6]
            )

            self.usuarios.append(u)
        self.file.close()

        self.numeroUsuarios = len(self.usuarios)
        self.contador = 0

        # hacemos los labels informativos
        self.letrero1 = QLabel()
        self.letrero1.setText("Lista de Residentes")
        self.letrero1.setFont(QFont("VAG_ROUNDED.ttf", 20))
        self.letrero1.setStyleSheet('color: black;'
                                    'background-color: transparent;')
        self.letrero1.setAlignment(Qt.AlignCenter)
        self.vertical.addWidget(self.letrero1)

        self.vertical.addSpacing(100)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet('background-color: white;')

        # para crear la tabla para que se vean de forma tabular
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(7)

        # definimos los numeros de colimnas que tendra la tabla

        self.tabla.setColumnWidth(0, 150)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 150)
        self.tabla.setColumnWidth(4, 150)
        self.tabla.setColumnWidth(5, 150)
        self.tabla.setColumnWidth(6, 150)

        self.tabla.setHorizontalHeaderLabels(["Nombre",
                                              "Cédula",
                                              "Celular",
                                              "Correo",
                                              "Apartamento",
                                              "Placa",
                                              "Celda"
                                              ])

        self.tabla.setRowCount(self.numeroUsuarios)

        for u in self.usuarios:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.nombreCompleto))
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.cedula))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.celular))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.apartamento))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.placa))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.celda))

            self.contador += 1

        self.scrollArea.setWidget(self.tabla)
        self.vertical.addWidget(self.scrollArea)

        self.vertical.addStretch()

        # creacion layout horizontal botones
        self.horizontal = QHBoxLayout()


        # Boton volver

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(100)
        self.botonVolver.setFixedHeight(40)
        self.botonVolver.setStyleSheet('background-color: #2F4F4F;'
                                       'color: #FFFFFF;'
                                       'padding: 5px;'
                                       'border-radius:10px')

        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        # Se agrega el boton al layout vertical

        self.horizontal.addWidget(self.botonVolver)
        self.vertical.addLayout(self.horizontal)

        self.vertical.addSpacing(30)

        # layout horizontal para el icono sendero verde
        self.horizontal2 = QHBoxLayout()

        # icono de sendero verde
        self.icon_sendero = QLabel()
        self.imagen2 = QPixmap('imagenes/imagen_sendero_verde.jpg')
        self.icon_sendero.setPixmap(self.imagen2)
        self.icon_sendero.setScaledContents(True)
        self.icon_sendero.setFixedSize(50, 50)
        self.horizontal2.addWidget(self.icon_sendero)
        self.vertical.addLayout(self.horizontal2)

        self.fondo.setLayout(self.vertical)

    def metodo_botonVolver(self):
        self.hide()
        self.Anterior.show()
