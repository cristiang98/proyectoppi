import os
import subprocess

import openpyxl
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QFormLayout, QPushButton, QHBoxLayout, QToolBar, \
    QWidget, QVBoxLayout, QAction, QSpacerItem, QSizePolicy, QApplication

from ingreso_visitantes import Ingreso_visitantes
from modulo_parqueadero import Modulo_parqueadero
from residentes import Residentes


class Menu_admin(QMainWindow):
    def __init__(self, anterior):
        super().__init__()

        self.ventanaAnterior = anterior

        # hacemos la ventana
        # caracteristicas de la ventana
        self.setWindowTitle("Menú")

        self.ancho = 700
        self.alto = 400
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

        # imagenes / proyecto1.jpg

        # creamos la ventana de fondo
        self.fondo = QLabel(self)

        self.fondo.setStyleSheet('background-color: qlineargradient(spread:pad, x1:0.71, y1:0.176045, x2:0.393, '
                                 'y2:0.643091, stop:0.159091 rgba(172, 172, 172, 255), stop:0.835227 rgba(210, 210, '
                                 '210, 255));')
        self.setCentralWidget(self.fondo)

        # Definimos el layout que vamos a usar
        self.vertical = QVBoxLayout()
        # ------- layout horizontal-----

        self.horizontal = QHBoxLayout()

        self.botonanterior = QPushButton(icon=QIcon('imagenes/anterior.png'))
        self.botonanterior.setStyleSheet('border-radius: 100px;'
                                         'background-color: transparent;'
                                         'margin-left:20px;')
        self.botonanterior.setFixedSize(50, 40)
        self.botonanterior.setIconSize(QSize(30, 30))
        self.botonanterior.clicked.connect(self.accion_botonAnterior)

        # ahora creamos los letreros (Qlabel())
        self.letrero1 = QLabel(self)
        self.letrero1.setText("Inicio de Sesión")
        self.letrero1.setFont(QFont('VAG_ROUNDED.ttf', 20))
        self.letrero1.setAlignment(Qt.AlignCenter)
        self.letrero1.setStyleSheet('background-color: transparent;'
                                    ' color: black; '
                                    'padding: 10px;'
                                    'margin-right: 0px;')
        # icono de sendero verde
        self.icon_sendero = QLabel()
        self.imagen2 = QPixmap('imagenes/imagen_sendero_verde.png')
        self.icon_sendero.setStyleSheet('background-color: transparent;')
        self.icon_sendero.setPixmap(self.imagen2)
        self.icon_sendero.setScaledContents(True)
        self.icon_sendero.setFixedSize(50, 50)

        self.horizontal.addWidget(self.botonanterior)
        self.horizontal.addWidget(self.letrero1)
        self.horizontal.addWidget(self.icon_sendero)
        self.vertical.addLayout(self.horizontal)

        self.vertical.addSpacing(30)

        # ------ layout horizontal1 ------

        self.horizontal1 = QHBoxLayout()

        # Boton ventana registro
        self.ventanaRegistro = QPushButton(icon=QIcon('imagenes/transparencia.png'))
        self.ventanaRegistro.setStyleSheet('background-color: transparent;')
        self.ventanaRegistro.setFixedSize(125, 125)
        self.ventanaRegistro.setIconSize(QSize(170, 120))
        self.ventanaRegistro.clicked.connect(self.accion_ventanaRegistro)

        # boton ventana parqueadero
        self.ventanaParqueadero = QPushButton(icon=QIcon('imagenes/transparencia2.png'))
        self.ventanaParqueadero.setStyleSheet('background-color: transparent;')
        self.ventanaParqueadero.setFixedSize(130, 140)
        self.ventanaParqueadero.setIconSize(QSize(150, 150))
        self.ventanaParqueadero.clicked.connect(self.accion_ventanaParqueadero)

        self.ventanaResidentes = QPushButton(icon=QIcon('imagenes/residentes.png'))
        self.ventanaResidentes.setStyleSheet('background-color: transparent;')
        self.ventanaResidentes.setFixedSize(125, 125)
        self.ventanaResidentes.setIconSize(QSize(170, 120))
        self.ventanaResidentes.clicked.connect(self.accion_ventanaResidentes)

        # ----------Agreagmos objetos al layout------

        self.horizontal1.addWidget(self.ventanaRegistro)
        self.horizontal1.addWidget(self.ventanaParqueadero)
        self.horizontal1.addWidget(self.ventanaResidentes)

        self.vertical.addLayout(self.horizontal1)

        # ----------Creacion de layout horizontal2 --------

        self.horizontal2 = QHBoxLayout()
        self.horizontal2.setContentsMargins(15, 0, 30, 0)

        # crear label para ventanaregisto
        self.label_registro = QLabel()
        self.label_registro.setText("Ingreso de\nVisitantes.")
        self.label_registro.setFont(QFont('VAG_ROUNDED.ttf', 10))
        self.label_registro.setStyleSheet('background-color: transparent;')
        self.label_registro.setAlignment(Qt.AlignCenter)

        # crear label para ventana parqueadero
        self.label_parqueadero = QLabel()
        self.label_parqueadero.setText("  Ocupación de\n   Parqueaderos.")
        self.label_parqueadero.setFont(QFont('VAG_ROUNDED.ttf', 10))
        self.label_parqueadero.setStyleSheet('background-color: transparent;')
        self.label_parqueadero.setAlignment(Qt.AlignCenter)

        self.label_residentes = QLabel()
        self.label_residentes.setText("Registro de los\nResidentes.")

        self.label_residentes.setFont(QFont('fonts/VAG_ROUNDED.ttf', 10))
        self.label_residentes.setStyleSheet('background-color: transparent;')
        self.label_residentes.setAlignment(Qt.AlignCenter)

        # Agreamos objetos al layout horizontal2
        self.horizontal2.addWidget(self.label_registro)
        self.horizontal2.addWidget(self.label_parqueadero)
        self.horizontal2.addWidget(self.label_residentes)

        self.vertical.addLayout(self.horizontal2)

        # ------ layout horizontal3------

        self.horizontal3 = QHBoxLayout()
        self.horizontal3.setContentsMargins(160, 0, 160, 0)

        self.excel = QPushButton("Excel")
        self.excel.setFixedWidth(100)
        self.excel.setFixedHeight(40)
        self.excel.setStyleSheet('background-color: #2F4F4F; color: #FFFFFF; padding: 10px;'
                                 'border-radius:10px')
        self.excel.clicked.connect(self.accion_excel)

        self.horizontal3.addWidget(self.excel)
        self.vertical.addLayout(self.horizontal3)



        # Layout que se usa para el fondo de la ventana
        self.fondo.setLayout(self.vertical)

    # Boton para volver pagina anterior
    def accion_botonAnterior(self):
        self.hide()
        self.ventanaAnterior.show()

    # metodo para ir a las demas pestañas
    def accion_ventanaRegistro(self):
        self.hide()
        self.ingreso_visitantes = Ingreso_visitantes(self)
        self.ingreso_visitantes.show()

    def accion_ventanaParqueadero(self):
        self.hide()
        self.modulo_parqueadero = Modulo_parqueadero(self)
        self.modulo_parqueadero.show()

    def accion_ventanaResidentes(self):
        self.hide()
        self.residentes = Residentes(self)
        self.residentes.show()

    def accion_excel(self):
        archivoTexto = 'datos/baseDatos.txt'

        try:
            # Obtener la ruta absoluta del archivo de texto
            rutaAbsoluta = os.path.abspath(archivoTexto)

            # Crear un nuevo archivo de Excel
            libro = openpyxl.Workbook()
            hoja = libro.active

            # Leer el archivo de texto y guardar los datos en el archivo de Excel
            with open(rutaAbsoluta, 'r') as archivo:
                fila = 1
                for linea in archivo:
                    datos = linea.strip().split(';')
                    hoja.append(datos)
                    fila += 1

            # Guardar el archivo de Excel
            rutaExcel = os.path.splitext(rutaAbsoluta)[0] + '.xlsx'
            libro.save(rutaExcel)

            # Abrir el archivo en Excel
            os.startfile(rutaExcel)
        except OSError:
            print("Error al abrir el archivo de Excel.")
