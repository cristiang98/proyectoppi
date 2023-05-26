import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout

from consulta_datos import Consulta_datos
from residente_tabular import Residente_tabular
from usuarios import Usuarios


class Residentes(QMainWindow):
    def __init__(self, anterior):
        super().__init__()

        self.Anterior = anterior
        # creacion de la ventana
        self.setWindowTitle("Formulario de registro")
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

        self.titulo = QLabel()
        self.titulo.setText("Registro de residentes o\n propietarios")
        self.titulo.setFont(QFont('VAG_ROUNDED.ttf', 20))
        self.titulo.setStyleSheet('background-color: transparent;')
        self.titulo.setAlignment(Qt.AlignCenter)
        self.vertical.addWidget(self.titulo)

        self.vertical.addSpacing(40)

        # -----creacion del formulario---------

        self.formulario = QFormLayout()
        self.formulario.setContentsMargins(150, 0, 90, 0)

        # labels

        self.labelNombrecompleto = QLabel()
        self.labelNombrecompleto.setText("Ingrese nombre completo*")
        self.labelNombrecompleto.setFont(QFont('VAG_ROUNDED.ttf', 12))
        self.labelNombrecompleto.setStyleSheet('background-color: transparent;')

        self.labelCedula = QLabel()
        self.labelCedula.setText("Ingrese número de cédula*")
        self.labelCedula.setFont(QFont('VAG_ROUNDED.ttf', 12))
        self.labelCedula.setStyleSheet('background-color: transparent;')

        self.labelCelular = QLabel()
        self.labelCelular.setText("Ingrese número de celular*")
        self.labelCelular.setFont(QFont('VAG_ROUNDED.ttf', 12))
        self.labelCelular.setStyleSheet('background-color: transparent;')

        self.labelCorreo = QLabel()
        self.labelCorreo.setText("Ingrese correo electrónico*")
        self.labelCorreo.setFont(QFont('VAG_ROUNDED.ttf', 12))
        self.labelCorreo.setStyleSheet('background-color: transparent;')

        self.labelApartamento = QLabel()
        self.labelApartamento.setText("Ingrese el número de apartamento*")
        self.labelApartamento.setFont(QFont('VAG_ROUNDED.ttf', 12))
        self.labelApartamento.setStyleSheet('background-color: transparent;')

        self.labelPlaca = QLabel()
        self.labelPlaca.setText("Ingrese el número de placa*")
        self.labelPlaca.setFont(QFont('VAG_ROUNDED.ttf', 12))
        self.labelPlaca.setStyleSheet('background-color: transparent;')

        self.labelCelda = QLabel()
        self.labelCelda.setText("¿Cuenta con parqueadero privado?*")
        self.labelCelda.setFont(QFont('VAG_ROUNDED.ttf', 12))
        self.labelCelda.setStyleSheet('background-color: transparent;')

        # -----EDITS------

        self.editNombrecompleto = QLineEdit()
        self.editNombrecompleto.setFixedWidth(170)
        self.editNombrecompleto.setFixedHeight(25)
        self.editNombrecompleto.setStyleSheet('background-color: white;')

        self.editCedula = QLineEdit()
        self.editCedula.setFixedWidth(170)
        self.editCedula.setFixedHeight(25)
        self.editCedula.setStyleSheet('background-color: white;')

        self.editCelular = QLineEdit()
        self.editCelular.setFixedWidth(170)
        self.editCelular.setFixedHeight(25)
        self.editCelular.setStyleSheet('background-color: white;')

        self.editCorreo = QLineEdit()
        self.editCorreo.setFixedWidth(170)
        self.editCorreo.setFixedHeight(25)
        self.editCorreo.setStyleSheet('background-color: white;')

        self.editApartamento = QLineEdit()
        self.editApartamento.setFixedWidth(170)
        self.editApartamento.setFixedHeight(25)
        self.editApartamento.setStyleSheet('background-color: white;')

        self.editPlaca = QLineEdit()
        self.editPlaca.setFixedWidth(170)
        self.editPlaca.setFixedHeight(25)
        self.editPlaca.setStyleSheet('background-color: white;')

        self.editCelda = QLineEdit()
        self.editCelda.setFixedWidth(170)
        self.editCelda.setFixedHeight(25)
        self.editCelda.setStyleSheet('background-color: white;')

        # agregamos al formulario

        self.formulario.addRow(self.labelNombrecompleto, self.editNombrecompleto)
        self.formulario.addRow(self.labelCedula, self.editCedula)
        self.formulario.addRow(self.labelCelular, self.editCelular)
        self.formulario.addRow(self.labelCorreo, self.editCorreo)
        self.formulario.addRow(self.labelApartamento, self.editApartamento)
        self.formulario.addRow(self.labelPlaca, self.editPlaca)
        self.formulario.addRow(self.labelCelda, self.editCelda)

        self.vertical.addLayout(self.formulario)
        self.vertical.addSpacing(60)

        # -------------layout horizontal-----------

        self.horizontal = QHBoxLayout()

        # botones volver y registrar

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(100)
        self.botonVolver.setFixedHeight(40)
        self.botonVolver.setStyleSheet('background-color: #2F4F4F;'
                                       'color: #FFFFFF;'
                                       'padding: 5px;'
                                       'border-radius:10px'
                                       )

        self.botonVolver.clicked.connect(self.accion_botonVolver)

        self.botonRegistrar = QPushButton("Registrar")
        self.botonRegistrar.setFixedWidth(100)
        self.botonRegistrar.setFixedHeight(40)
        self.botonRegistrar.setStyleSheet('background-color: #2F4F4F;'
                                          'color: #FFFFFF;'
                                          'padding: 5px;'
                                          'border-radius:10px'
                                          )
        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        self.botonResidentes = QPushButton("Residentes")
        self.botonResidentes.setFixedWidth(100)
        self.botonResidentes.setFixedHeight(40)
        self.botonResidentes.setStyleSheet('background-color: #2F4F4F;'
                                           'color: #FFFFFF;'
                                           'padding: 5px;'
                                           'border-radius:10px'
                                           )
        self.botonResidentes.clicked.connect(self.accion_botonResidentes)

        self.horizontal.addWidget(self.botonVolver)
        self.horizontal.addWidget(self.botonRegistrar)
        self.horizontal.addWidget(self.botonResidentes)

        self.vertical.addLayout(self.horizontal)

        self.vertical.addSpacing(30)

        # layout horizonat1 icono senderoverde
        self.horizontal = QHBoxLayout()

        # icono de sendero verde
        self.icon_sendero = QLabel()
        self.imagen2 = QPixmap('imagenes/imagen_sendero_verde.jpg')
        self.icon_sendero.setPixmap(self.imagen2)
        self.icon_sendero.setScaledContents(True)
        self.icon_sendero.setFixedSize(50, 50)
        self.horizontal.addWidget(self.icon_sendero)
        self.vertical.addLayout(self.horizontal)

        self.fondo.setLayout(self.vertical)

        # creamos ventana de dialogo
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanaDialogo.resize(300, 150)

        # crear boton para aceptar
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        # titulo
        self.ventanaDialogo.setWindowTitle("Formulario de registro")

        # configuracion modal
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # crear layout vertical
        self.vertical = QVBoxLayout()

        self.mensaje = QLabel("")
        self.mensaje.setStyleSheet('background-color: #008B45; color: #FFFFFF; padding: 10 px;')

        self.vertical.addWidget(self.mensaje)
        self.vertical.addWidget(self.opciones)
        self.ventanaDialogo.setLayout(self.vertical)

    def accion_botonVolver(self):
        self.hide()
        self.Anterior.show()

    def limpiar(self):
        self.editNombrecompleto.setText("")
        self.editCedula.setText("")
        self.editCelular.setText("")
        self.editCorreo.setText("")
        self.editApartamento.setText("")
        self.editPlaca.setText("")
        self.editCelda.setText("")

    def accion_botonRegistrar(self):

        # datos correctos
        self.datosCorrectos = True

        if (
                self.editNombrecompleto.text() == ''
                or self.editCedula.text() == ''
                or self.editCelular.text() == ''
                or self.editCorreo.text() == ''
                or self.editApartamento.text() == ''
                or self.editPlaca.text() == ''
                or self.editCelda.text() == ''
        ):
            self.datosCorrectos = False
            self.mensaje.setText("Debe ingresar todos los campos")
            self.ventanaDialogo.exec_()

        if self.datosCorrectos:
            # si los datos estan correctos

            # Abrimos el archivo en modo agregar
            self.file = open('datos/residente.txt', 'ab')

            # trae el texto de los Qline y los concatena
            self.file.write(bytes(self.editNombrecompleto.text() + ";" +
                                  self.editCedula.text() + ";" +
                                  self.editCelular.text() + ";" +
                                  self.editCorreo.text() + ";" +
                                  self.editApartamento.text() + ";" +
                                  self.editPlaca.text() + ";" +
                                  self.editCelda.text() + ";" + "\n", encoding='UTF-8'))
            self.file.close()

            self.file = open('datos/residente.txt', 'rb')
            while self.file:
                linea = self.file.read().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()

        self.limpiar()

    def accion_botonResidentes(self):
        self.hide()
        self.residente_tabular = Residente_tabular(self)
        self.residente_tabular.show()
