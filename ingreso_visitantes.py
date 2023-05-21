import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QTabWidget, QLabel, QHBoxLayout, \
    QLineEdit, QPushButton, QMessageBox, QFormLayout, QApplication


#from ingreso_datos import Ingreso_datos


class Ingreso_visitantes(QMainWindow):
    def __init__(self, anterior):
        super().__init__()

        self.ventanaAnterior = anterior

        # hacemos la ventana
        # caracteristicas de la ventana
        self.setWindowTitle("Sofos R.P.H")
        self.ancho = 450
        self.alto = 350
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

        # titulo
        self.titulo = QLabel(self)
        self.titulo.setText("Ingreso de Visitantes")
        self.titulo.setFont(QFont('VAG_ROUNDED.ttf', 20))
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setStyleSheet('background-color: transparent; color: black; padding: 10px;')
        self.vertical.addWidget(self.titulo)
        self.vertical.addSpacing(30)

        # ------ layout form1 ----
        self.formulario1 = QFormLayout()
        self.formulario1.setContentsMargins(40, 0, 0, 0)

        # Label numero apartamento
        self.numero_apartamento = QLabel()
        self.numero_apartamento.setFixedWidth(250)
        self.numero_apartamento.setText("Ingrese Apartamento:")
        self.numero_apartamento.setFont(QFont('VAG_ROUNDED.ttf', 15))
        self.numero_apartamento.setStyleSheet('background-color: transparent;')


        # QlineEdit del numero de apartamento
        self.campo_apartamento = QLineEdit()
        self.campo_apartamento.setFixedWidth(100)
        self.campo_apartamento.setFixedHeight(30)
        self.campo_apartamento.setMaxLength(4)
        self.campo_apartamento.setStyleSheet('background-color: white;')

        #agregamos objetos a form1
        self.formulario1.addRow(self.numero_apartamento, self.campo_apartamento)
        self.vertical.addLayout(self.formulario1)


        # -------- layout horizontal1 ----------
        self.horizontal1 = QHBoxLayout()

        # crear el boton volver
        self.boton_Volver = QPushButton("Volver")
        self.boton_Volver.setFixedWidth(100)
        self.boton_Volver.setFixedHeight(40)
        self.boton_Volver.setStyleSheet('background-color: #2F4F4F; color: #FFFFFF; padding: 10px;'
                                        'border-radius:10px')
        self.boton_Volver.clicked.connect(self.accion_botonVolver)

        # Crear boton ingresar
        self.boton_ingresar = QPushButton("Ingresar")
        self.boton_ingresar.setFixedWidth(100)
        self.boton_ingresar.setFixedHeight(40)
        self.boton_ingresar.setStyleSheet('background-color: #2F4F4F; color: #FFFFFF; padding: 10px;'
                                          'border-radius:10px')
        self.boton_ingresar.clicked.connect(self.accion_IngresoDatos)

        # Agregamos objetos a layout hor1----
        self.horizontal1.addWidget(self.boton_Volver)
        self.horizontal1.addWidget(self.boton_ingresar)
        self.vertical.addLayout(self.horizontal1)

        # spacing
        self.vertical.addSpacing(25)

        # layout horizontal2
        self.horizontal2 = QHBoxLayout()
        # icono de sendero verde
        self.icon_sendero = QLabel()
        self.imagen2 = QPixmap('imagenes/imagen_sendero_verde.jpg')
        self.icon_sendero.setPixmap(self.imagen2)
        self.icon_sendero.setScaledContents(True)
        self.icon_sendero.setFixedSize(50, 50)

        self.horizontal2.addWidget(self.icon_sendero)
        self.vertical.addLayout(self.horizontal2)

        # Layout que se usa para el fondo de la ventana
        self.fondo.setLayout(self.vertical)

    # funcion para volver
    def accion_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def accion_IngresoDatos(self):
        """self.hide()
        self.ingreso_datos = Ingreso_datos(self)
        self.ingreso_datos.show()"""
        pass

