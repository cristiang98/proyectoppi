from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QVBoxLayout, QFormLayout, \
    QPushButton, QDialogButtonBox, QDialog, QLineEdit

from login_admin import Login_admin


class Verificacion_admin(QMainWindow):
    def __init__(self, anterior):
        super().__init__()
        self.Anterior = anterior
        self.setWindowTitle("Sophos R.P.H")
        self.ancho = 600
        self.alto = 400
        self.resize(self.ancho, self.alto)
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.fondo = QLabel()
        self.fondo.setStyleSheet('background-color: qlineargradient(spread:pad, x1:0.71, y1:0.176045, x2:0.393, '
                                 'y2:0.643091, stop:0.159091 rgba(172, 172, 172, 255), stop:0.835227 rgba(210, 210, '
                                 '210, 255));'
                                 '')

        self.setCentralWidget(self.fondo)

        self.vertical = QVBoxLayout()

        # ahora creamos los letreros (Qlabel())
        self.letrero1 = QLabel()
        self.letrero1.setText("Administrador")
        self.letrero1.setFont(QFont('VAG Rounded.ttf', 20))
        self.letrero1.setAlignment(Qt.AlignCenter)
        self.letrero1.setStyleSheet('background-color: transparent; '
                                    'color: black;'
                                    'margin-bottom:0px;'
                                    'padding:10px;')

        # layout formulario

        self.formulario = QFormLayout()
        self.formulario.setContentsMargins(0, 30, 90, 0)

        # label y campo

        self.verificar = QLabel()
        self.verificar.setText("Introduzca clave de verificación:")
        self.verificar.setFont(QFont('VAG Rounded.ttf', 12))
        self.verificar.setStyleSheet('background-color:transparent;'
                                     'color:black;'
                                     'margin-left:80px;')

        self.campo_verificar = QLineEdit()
        self.campo_verificar.setFixedWidth(100)
        self.campo_verificar.setFixedHeight(25)
        self.campo_verificar.setEchoMode(QLineEdit.EchoMode.Password)
        self.campo_verificar.setStyleSheet('background-color: white;')

        # _________Agregamos los objetos al layout formulario--------------

        self.vertical.addWidget(self.letrero1)
        self.formulario.addRow(self.verificar, self.campo_verificar)
        self.vertical.addLayout(self.formulario)

        # layout horizontal
        self.horizontal = QHBoxLayout()
        # boton volver, boton ingresar

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(100)
        self.botonVolver.setFixedHeight(40)
        self.botonVolver.setStyleSheet('background-color: #2F4F4F; '
                                       'color: #FFFFFF; '
                                       'border-radius:10px;'
                                       '')
        self.botonVolver.clicked.connect(self.accion_botonVolver)

        self.botonIngresar = QPushButton("Ingresar")
        self.botonIngresar.setFixedWidth(100)
        self.botonIngresar.setFixedHeight(40)

        self.botonIngresar.setStyleSheet('background-color: #2F4F4F; '
                                         'color: #FFFFFF; '
                                         'border-radius:10px;')
        self.botonIngresar.clicked.connect(self.accion_botonIngresar)

        self.horizontal.addWidget(self.botonVolver)
        self.horizontal.addWidget(self.botonIngresar)

        self.vertical.addLayout(self.horizontal)
        self.vertical.addSpacing(60)

        # creacion horizontal2
        self.horizontal2 = QHBoxLayout()
        # icono de sendero verde
        self.icon_sendero = QLabel()
        self.imagen2 = QPixmap('imagenes/imagen_sendero_verde.jpg')
        self.icon_sendero.setPixmap(self.imagen2)
        self.icon_sendero.setScaledContents(True)
        # esta linena es para correr a la derecha el icono
        # self.horizontal2.addSpacing(0)
        self.icon_sendero.setFixedSize(50, 50)
        self.horizontal2.addWidget(self.icon_sendero)
        self.vertical.addLayout(self.horizontal2)

        self.fondo.setLayout(self.vertical)

    def accion_botonVolver(self):
        self.hide()
        self.Anterior.show()

    def accion_botonIngresar(self):
        # creamos ventana de dialogo
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanaDialogo.resize(300, 150)

        # crear boton para aceptar
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        # titulo
        self.ventanaDialogo.setWindowTitle("Verificación de Administrador")

        # configuracion modal
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # crear layout vertical
        self.vertical = QVBoxLayout()

        self.mensaje = QLabel("")
        self.mensaje.setStyleSheet('background-color: #000000; '
                                   'color: #FFFFFF; '
                                   'padding: 10px;'
                                   'border-radius:10px;')

        self.vertical.addWidget(self.mensaje)
        self.vertical.addWidget(self.opciones)
        self.ventanaDialogo.setLayout(self.vertical)

        # declaracion de verdadero
        self.datos_Correctos = True

        """if self.campo_verificar.text().isalpha():
            self.datos_Correctos = False
            self.mensaje.setText("Solo números en el campo.")
            self.ventanaDialogo.exec_()

        if not (self.campo_verificar.text() == "1234"):
            self.datos_Correctos = False
            self.mensaje.setText("Código inválido.")
            self.ventanaDialogo.exec_()"""

        if self.datos_Correctos:
            self.hide()
            self.login_admin = Login_admin(self)
            self.login_admin.show()

        self.campo_verificar.setText("")
