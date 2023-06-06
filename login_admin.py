import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QVBoxLayout, QFormLayout, \
    QPushButton, QDialogButtonBox, QDialog, QLineEdit, QMessageBox

from menu_admin import Menu_admin
from registro_recuperar import Registro_recuperar
from usuarios import Usuarios


class Login_admin(QMainWindow):
    def __init__(self, anterior):
        super().__init__()
        self.Anterior = anterior
        # hacemos la ventana
        # caracteristicas de la ventana
        self.setWindowTitle("Inicio de Sesión")
        self.ancho = 600
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
                                    'margin-right: 0px;')
        # icono de sendero verde
        self.icon_sendero = QLabel()
        self.imagen2 = QPixmap('imagenes/imagen_sendero_verde.png')
        self.icon_sendero.setStyleSheet('background-color: transparent;')
        self.icon_sendero.setPixmap(self.imagen2)
        self.icon_sendero.setScaledContents(True)
        self.icon_sendero.setFixedSize(50, 50)



        self.horizontal1.addWidget(self.botonanterior)
        self.horizontal1.addWidget(self.letrero1)
        self.horizontal1.addWidget(self.icon_sendero)
        self.vertical1.addLayout(self.horizontal1)


        self.formulario.setContentsMargins(180, 0, 100, 0)
        # etiqueta de usuario
        self.usuario = QLabel()
        self.usuario.setText("Usuario")
        self.usuario.setFont(QFont("VAG_ROUNDED.ttf", 15))
        self.usuario.setStyleSheet('background-color: transparent;'
                                   'margin-top:20px;'
                                   'margin-left:65px;')

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

        # Layout que se usa para el fondo de la ventana
        self.fondo.setLayout(self.vertical1)

    def accion_Registro(self):
        self.hide()
        self.registro_recuperar = Registro_recuperar(self)
        self.registro_recuperar.show()

    def accion_inicioSesion(self):

        # declaracion de verdadero
        self.datos_Correctos = True

        # condiciones

        if self.campo1.text() == '':
            return QMessageBox.warning(
                self,
                'Warning',
                'Por favor introduzca su usuario.'
            )

        if not self.campo1.text().isalpha():
            return QMessageBox.warning(
                self,
                'Warning',
                'Solo letras en usuario.'
            )


        if self.campo2.text() == '':
            return QMessageBox.warning(
                self,
                'Warning',
                'Por favor introduzca su contraseña.'
            )

        if self.campo2.text().isalpha():
            return QMessageBox.warning(
                self,
                'Warning',
                'En contraseña solo es válido números'
            )


        if not self.campo2.text().isalnum():
            self.datos_Correctos = False

            if self.campo2.text() != '':
                return QMessageBox.warning(
                    self,
                    'Warning',
                    'Ingreso caracteres especiales'
                )



        if self.datos_Correctos:

            self.file = open('datos/usuarios.txt', 'rb')
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                # obtenemos del string una lista con 11 datos separados por;
                lista = linea.split(";")

                # paramos el bucle si ya no encuentra mas registros en el archivo
                if linea == '':
                    break

                u = Usuarios(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8],
                    lista[9],
                    lista[10],
                    lista[11],
                    lista[12]
                )

                # metemos el objeto en la lista de usuarios
                usuarios.append(u)

            # cerramos ael archivo txt
            self.file.close()

            # en este punto tenemos la lista de usuarios con todos los usuarios

            existeDocumento = False

            # buscamos en la lista de usuarios si existe la cedula

            for u in usuarios:
                """comparamos el documento ingresado:
                si correspopnde con el documento, es el usuario correcto:"""

                if u.usuario == self.campo1.text() and u.contrasena == self.campo2.text():
                    # indicamos que existen
                    existeDocumento = True

                    break

            if (
                u.contrasena != self.campo2.text()
            ):
                existeDocumento = False

                return QMessageBox.warning(
                    self,
                    'Warning',
                    'No existe contraseña registrado'
                )

            # si no existe usuario con este documento
            if (
                    not existeDocumento
            ):
                return QMessageBox.warning(
                    self,
                    'Warning',
                    'No existe usuario registrado'
                )

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