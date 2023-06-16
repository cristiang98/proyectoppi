from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QVBoxLayout, QFormLayout, \
    QPushButton, QDialogButtonBox, QDialog, QLineEdit, QMessageBox

from login_admin import Login_admin


class Verificacion_admin(QMainWindow):
    def __init__(self, anterior):
        super().__init__()
        self.Anterior = anterior
        self.setWindowTitle("Validación")
        self.setWindowIcon(QtGui.QIcon('imagenes/sophos.jpeg'))
        self.ancho = 500
        self.alto = 250
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
        self.letrero1.setText("Administrador")
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
        self.vertical.addLayout(self.horizontal1)



        # layout formulario

        self.formulario = QFormLayout()
        self.formulario.setContentsMargins(65, 30, 0, 0)

        # label y campo

        self.verificar = QLabel()
        self.verificar.setText("Introduzca clave de verificación:")
        self.verificar.setFont(QFont('VAG Rounded.ttf', 12))
        self.verificar.setStyleSheet('background-color:transparent;'
                                     'color:black;'
                                     )

        self.campo_verificar = QLineEdit()
        self.campo_verificar.setFixedWidth(100)
        self.campo_verificar.setFixedHeight(25)
        self.campo_verificar.setMaxLength(4)
        self.campo_verificar.setEchoMode(QLineEdit.EchoMode.Password)
        self.campo_verificar.returnPressed.connect(self.accion_botonIngresar)
        self.campo_verificar.setStyleSheet('background-color: white;')

        # _________Agregamos los objetos al layout formulario--------------

        self.formulario.addRow(self.verificar, self.campo_verificar)
        self.vertical.addLayout(self.formulario)

        # layout horizontal
        self.horizontal = QHBoxLayout()
        self.horizontal.setContentsMargins(160, 0, 160, 10)

        # boton volver, boton ingresar


        self.botonIngresar = QPushButton("Ingresar")
        self.botonIngresar.setFixedWidth(100)
        self.botonIngresar.setFixedHeight(40)

        self.botonIngresar.setStyleSheet('background-color: #2F4F4F; '
                                         'color: #FFFFFF; '
                                         'border-radius:10px;')
        self.botonIngresar.clicked.connect(self.accion_botonIngresar)


        self.horizontal.addWidget(self.botonIngresar)

        self.vertical.addLayout(self.horizontal)


        # creacion horizontal2


        self.fondo.setLayout(self.vertical)

    def accion_botonAnterior(self):
        self.hide()
        self.Anterior.show()

    def accion_botonIngresar(self):
        self.datos_Correctos = True

        if self.campo_verificar.text() == '':
            return QMessageBox.warning(
                self,
                'Warning',
                'Por favor introduzca su pin.'
            )

        if self.campo_verificar.text() != '1998':
            return QMessageBox.warning(
                self,
                'Warning',
                'Ingrese el pin correcto si desea continuar.'
            )


        if self.datos_Correctos:
            self.hide()
            self.login_admin = Login_admin(self)
            self.login_admin.show()

        self.campo_verificar.setText("")
