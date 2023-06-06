import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QTabWidget, QLabel, QHBoxLayout, \
    QLineEdit, QPushButton, QMessageBox, QFormLayout, QApplication, QGridLayout


# from ingreso_datos import Ingreso_datos


class Modulo_parqueadero(QMainWindow):
    def __init__(self, anterior):
        super().__init__()

        self.ventanaAnterior = anterior

        # hacemos la ventana
        # caracteristicas de la ventana
        self.setWindowTitle("Parqueadero")
        self.ancho = 900
        self.alto = 700
        self.resize(self.ancho, self.alto)
        self.setWindowIcon(QIcon('imagenes/sophos.jpeg'))

        # centramos la ventana
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # bloquear dimensiones
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # creamos la ventana de fondo
        self.fondo = QLabel(self)

        self.fondo.setStyleSheet('background-color: qlineargradient(spread:pad, x1:0.71, y1:0.176045, x2:0.393, '
                                 'y2:0.643091, stop:0.159091 rgba(172, 172, 172, 255), stop:0.835227 rgba(210, 210, '
                                 '210, 255));')

        self.setCentralWidget(self.fondo)

        # Definimos el layout que vamos a usar
        self.vertical = QVBoxLayout()

        self.horizontal1 = QHBoxLayout()
        self.horizontal1.setContentsMargins(0, 0, 50, 0)
        self.botonanterior = QPushButton(icon=QIcon('imagenes/anterior.png'))
        self.botonanterior.setStyleSheet('border-radius: 100px;'
                                         'background-color: transparent;'
                                         'margin-left:20px;')
        self.botonanterior.setFixedSize(50, 40)
        self.botonanterior.setIconSize(QSize(30, 30))
        self.botonanterior.clicked.connect(self.accion_botonAnterior)

        # ahora creamos los letreros (Qlabel())
        self.letrero1 = QLabel(self)
        self.letrero1.setText("Parqueadero")
        self.letrero1.setFont(QFont('VAG_ROUNDED.ttf', 20))

        self.letrero1.setStyleSheet('background-color: transparent;'
                                    ' color: black; '
                                    'padding: 10px;'
                                    'margin-left: 100px;')




        self.labelPorcentaje = QLabel()
        self.labelPorcentaje.setStyleSheet('background-color: transparent;'
                                           'color: black;'
                                           'margin-left: 50px;')
        self.labelPorcentaje.setFont(QFont('fonts/VAG_ROUNDED.ttf', 12))

        # icono de sendero verde
        self.icon_sendero = QLabel()
        self.imagen2 = QPixmap('imagenes/imagen_sendero_verde.png')
        self.icon_sendero.setStyleSheet('background-color: transparent;')
        self.icon_sendero.setPixmap(self.imagen2)
        self.icon_sendero.setScaledContents(True)
        self.icon_sendero.setFixedSize(50, 50)

        self.horizontal1.addSpacing(30)

        self.horizontal1.addWidget(self.botonanterior)
        self.horizontal1.addWidget(self.letrero1)
        self.horizontal1.addWidget(self.labelPorcentaje)
        self.horizontal1.addWidget(self.icon_sendero)
        self.vertical.addLayout(self.horizontal1)

        self.grid = QGridLayout()

        self.botones = []

        cont = 1
        c = 14
        f = 5

        for i in range(c):
            for j in range(f):
                self.boton = QPushButton(f"Celda {cont}")
                self.boton.setStyleSheet('background-color: green;')
                self.boton.setFixedWidth(110)
                self.boton.setFixedHeight(25)
                self.boton.setCheckable(True)
                self.boton.clicked.connect(self.changeColor)
                self.grid.addWidget(self.boton, i, j)
                self.botones.append(self.boton)
                cont = cont + 1

        self.vertical.addLayout(self.grid)

        self.vertical.addSpacing(30)

        self.loadButtonStates()
        self.actualizarEtiquetaPorcentaje()
        self.fondo.setLayout(self.vertical)

    def accion_botonAnterior(self):
        self.hide()
        self.ventanaAnterior.show()

    def actualizarEtiquetaPorcentaje(self):
        cantidad_verde = sum(not button.isChecked() for button in self.botones)
        cantidad_rojo = len(self.botones) - cantidad_verde
        cantidad_total = len(self.botones)
        if cantidad_total > 0:
            porcentaje_verde = (cantidad_verde / cantidad_total) * 100
            porcentaje_rojo = (cantidad_rojo / cantidad_total) * 100
        else:
            porcentaje_verde = 0
            porcentaje_rojo = 0
        self.labelPorcentaje.setText(f"Disponible: {porcentaje_verde:.2f}%\nOcupado: {porcentaje_rojo:.2f}%")

    def loadButtonStates(self):
        try:
            with open("datos/estados.txt", "r") as file:
                button_states = file.read().strip()

            for i, button in enumerate(self.botones):
                if button_states[i] == "1":
                    button.setStyleSheet("background-color: red;")
                    button.setChecked(True)
        except FileNotFoundError:
            pass

    def changeColor(self):
        button = self.sender()
        if button.isChecked():
            button.setStyleSheet("background-color: red;")
        else:
            button.setStyleSheet("background-color: green;")

        # Guardar el estado de los botones en el archivo visitantes
        button_states = "".join("1" if button.isChecked() else "0" for button in self.botones)
        with open("datos/estados.txt", "w") as file:
            file.write(button_states)

        self.actualizarEtiquetaPorcentaje()
