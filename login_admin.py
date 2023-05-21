import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QVBoxLayout, QFormLayout, \
    QPushButton, QDialogButtonBox, QDialog, QLineEdit

from menu_admin import Menu_admin
from registro_recuperar import Registro_recuperar


class Login_admin(QMainWindow):
    def __init__(self, anterior):
        super().__init__()
        self.Anterior = anterior
        # hacemos la ventana
        # caracteristicas de la ventana
        self.setWindowTitle("Sofos R.P.H")
        self.ancho = 600
        self.alto = 450
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
        self.formulario = QFormLayout()
        self.vertical1 = QVBoxLayout()

        # ------- layout horizontal-----

        self.horizontal1 = QHBoxLayout()

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
                                    'margin-right: 50px;')

        self.horizontal1.addWidget(self.botonanterior)
        self.horizontal1.addWidget(self.letrero1)
        self.vertical1.addLayout(self.horizontal1)


        self.formulario.setContentsMargins(180, 0, 100, 0)
        # etiqueta de usuario
        self.usuario = QLabel()
        self.usuario.setText("Usuario")
        self.usuario.setFont(QFont("VAG_ROUNDED.ttf", 15))
        self.usuario.setStyleSheet('background-color: transparent;'
                                   'margin-top:20px;'
                                   'margin-left:50px;')

        # hacemos el campo para el usuario
        self.campo1 = QLineEdit()
        self.campo1.setFixedWidth(170)
        self.campo1.setFixedHeight(25)
        self.campo1.setMaxLength(10)
        self.campo1.setStyleSheet('background-color: white;'
                                  'margin-top:5px;'
                                  'margin-left:60px;')

        # etiqueta de contraseña
        self.contraseña = QLabel("Contraseña")
        self.contraseña.setFont(QFont("VAG_ROUNDED.ttf", 15))
        self.contraseña.setStyleSheet('background-color: transparent;'
                                      'margin-top:10px;'
                                      'margin-left:50px;')

        # campo de la contraseña
        self.campo2 = QLineEdit()
        self.campo2.setFixedWidth(170)
        self.campo2.setFixedHeight(25)
        self.campo2.setMaxLength(4)
        self.campo2.setStyleSheet('background-color: white;'
                                  'margin-top:5px;'
                                  'margin-left:60px;')
        self.campo2.setEchoMode(QLineEdit.EchoMode.Password)

        # hacemos el boton de inicio de sesion
        self.inicio_sesion = QPushButton("Iniciar Sesión")
        self.inicio_sesion.setFixedWidth(100)
        self.inicio_sesion.setFixedHeight(55)
        self.inicio_sesion.setStyleSheet('background-color: #2F4F4F;'
                                         'color: #FFFFFF; '
                                         'padding: 10px;'
                                         'border-radius:10px;'
                                         'margin-top:15px;'
                                         '')
        self.inicio_sesion.clicked.connect(self.accion_inicioSesion)

        # hacer boton registro
        self.registro = QPushButton("Registrar")
        self.registro.setFixedWidth(120)
        self.registro.setFixedHeight(55)
        self.registro.setStyleSheet('background-color: #2F4F4F;'
                                    'color: #FFFFFF; '
                                    'padding: 10px;'
                                    'border-radius:10px;'
                                    'margin-top:15px;'
                                    'margin-right:20px;')
        self.registro.clicked.connect(self.accion_Registro)

        # Agregamos boton recuperar contraseña
        self.recuperar = QPushButton()
        self.recuperar.setText("¿Recuperar Contraseña?")
        self.recuperar.setFont(QFont("VAG_ROUNDED.ttf", 10))
        self.recuperar.setFixedWidth(230)
        self.recuperar.setStyleSheet('background-color: transparent; '
                                     'text-decoration: underline;'
                                     'margin-top:15px;'
                                     'margin-left:0px;')

        self.recuperar.clicked.connect(self.accion_recuperarContrasena)


        # ________Agregamos los objetos a la ventana con formulario_________

        self.formulario.addRow(self.usuario)
        self.formulario.addRow(self.campo1)
        self.formulario.addRow(self.contraseña)
        self.formulario.addRow(self.campo2)
        self.formulario.addRow(self.registro, self.inicio_sesion)
        self.formulario.addRow(self.recuperar)
        self.vertical1.addLayout(self.formulario)

        self.vertical1.addStretch()

        # -------------Layout horizontal--------
        self.horizontal = QHBoxLayout()

        # icono de sendero verde
        self.icon_sendero = QLabel()
        self.imagen2 = QPixmap('imagenes/imagen_sendero_verde.jpg')
        self.icon_sendero.setPixmap(self.imagen2)
        self.icon_sendero.setScaledContents(True)
        self.icon_sendero.setFixedSize(50, 50)
        self.horizontal.addWidget(self.icon_sendero)
        self.vertical1.addLayout(self.horizontal)

        # Layout que se usa para el fondo de la ventana
        self.fondo.setLayout(self.vertical1)

    def accion_Registro(self):
        self.hide()
        self.registro_recuperar = Registro_recuperar(self)
        self.registro_recuperar.show()

    def accion_inicioSesion(self):

        # ventanas emergentes creacion
        self.ventana_Dialogo = QDialog()
        self.ventana_Dialogo.resize(250, 150)

        # creamos boton para ok
        self.boton_OK = QDialogButtonBox.Ok
        self.opciones_Botones = QDialogButtonBox(self.boton_OK)
        self.opciones_Botones.accepted.connect(self.ventana_Dialogo.accept)

        # titulo de la ventana emergente
        self.ventana_Dialogo.setWindowTitle("Error")
        self.ventana_Dialogo.setWindowModality(Qt.ApplicationModal)

        # creamos el layout que queremos usar (vertical)
        self.vertical = QVBoxLayout()

        # creacion del label mensaje
        self.mensaje = QLabel("")
        self.mensaje.setStyleSheet('background-color: #000000; color: #FFFFFF; padding: 10px;'
                                   'border-radius:10px;')

        # agregamos la etiqueta
        self.vertical.addWidget(self.mensaje)
        self.vertical.addWidget(self.opciones_Botones)

        self.ventana_Dialogo.setLayout(self.vertical)

        # declaracion de verdadero
        self.datos_Correctos = True

        # condiciones
        if self.campo1.text().isspace():
            self.datos_Correctos = False
            self.mensaje.setText("Ingreso espacios en blanco en usuario")
            self.ventana_Dialogo.exec_()

        if self.campo1.text() == '':
            self.datos_Correctos = False
            self.mensaje.setText("No ingresó nada en usuario")
            self.ventana_Dialogo.exec_()

        if not self.campo1.text().isalpha():
            self.datos_Correctos = False
            self.mensaje.setText("Solo son válidas letras en usuario")
            self.ventana_Dialogo.exec_()

        if self.campo2.text().isspace():
            self.datos_Correctos = False
            self.mensaje.setText("Ingresó espacios en contraseña")
            self.ventana_Dialogo.exec_()

        if self.campo2.text() == '':
            self.datos_Correctos = False
            self.mensaje.setText("No ingresó nada en contraseña")
            self.ventana_Dialogo.exec_()

        if self.campo2.text().isalpha():
            self.datos_Correctos = False
            self.mensaje.setText("Solo son válidos números en contraseña")
            self.ventana_Dialogo.exec_()

        if not self.campo2.text().isalnum():
            self.datos_Correctos = False

            if self.campo2.text() != '':
                self.mensaje.setText("Ingresó caracteres especiales")
                self.ventana_Dialogo.exec_()



        if self.datos_Correctos:
            self.hide()
            self.menu_admin = Menu_admin(self)
            self.menu_admin.show()

        self.campo1.setText("")
        self.campo2.setText("")

    def accion_recuperarContrasena(self):
        self.hide()
        self.registro_recuperar = Registro_recuperar(self)
        self.registro_recuperar.show()

    def accion_botonAnterior(self):
        self.hide()
        self.Anterior.show()