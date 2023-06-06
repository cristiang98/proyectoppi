import sys

from PyQt5.QtCore import Qt
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
        self.setWindowTitle("Sofos R.P.H")
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

        self.horizontal3 = QHBoxLayout()
        self.horizontal3.setContentsMargins(300, 0, 0, 0)
        # titulo
        self.titulo = QLabel(self)
        self.titulo.setText("Parqueadero")
        self.titulo.setFont(QFont('VAG_ROUNDED.ttf', 20))
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setStyleSheet('background-color: transparent; color: black; padding: 10px;')
        self.horizontal3.addWidget(self.titulo)

        self.labelPorcentaje = QLabel()
        self.labelPorcentaje.setStyleSheet('background-color: transparent;'
                                           'color: black;')
        self.labelPorcentaje.setFont(QFont('fonts/VAG_ROUNDED.ttf', 12))

        self.horizontal3.addWidget(self.labelPorcentaje)
        self.vertical.addLayout(self.horizontal3)

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

        # creacion layout horizontal botones
        self.horizontal = QHBoxLayout()

        # Boton volver

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(100)
        self.botonVolver.setFixedHeight(40)
        self.botonVolver.setStyleSheet('background-color: #2F4F4F;'
                                       'color: #FFFFFF;'
                                       'padding: 5px;'
                                       'border-radius:10px;')

        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        self.horizontal.addWidget(self.botonVolver)
        self.vertical.addLayout(self.horizontal)
        self.vertical.addSpacing(30)

        # layout horizontal para el icono sendero verde
        self.horizontal2 = QHBoxLayout()

        # icono de sendero verde
        self.icon_sendero = QLabel()
        self.imagen2 = QPixmap('imagenes/imagen_sendero_verde.png')
        self.icon_sendero.setStyleSheet('background-color: transparent;')
        self.icon_sendero.setPixmap(self.imagen2)
        self.icon_sendero.setScaledContents(True)
        self.icon_sendero.setFixedSize(50, 50)
        self.horizontal2.addWidget(self.icon_sendero)
        self.vertical.addLayout(self.horizontal2)

        self.loadButtonStates()
        self.actualizarEtiquetaPorcentaje()
        self.fondo.setLayout(self.vertical)

    def metodo_botonVolver(self):
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
            print(self.boton.text())
        else:
            button.setStyleSheet("background-color: green;")

        # Guardar el estado de los botones en el archivo visitantes
        button_states = "".join("1" if button.isChecked() else "0" for button in self.botones)
        with open("datos/estados.txt", "w") as file:
            file.write(button_states)

        self.actualizarEtiquetaPorcentaje()
