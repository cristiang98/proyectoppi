import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QTabWidget, QLabel, QHBoxLayout, \
    QLineEdit, QPushButton, QMessageBox, QFormLayout, QApplication

from lista_residente import Residente
from residentes import Residentes


# from ingreso_datos import Ingreso_datos


class Ingreso_visitantes(QMainWindow):
    def __init__(self, anterior):
        super().__init__()

        self.ventanaAnterior = anterior

        # hacemos la ventana
        # caracteristicas de la ventana
        self.setWindowTitle("Sofos R.P.H")
        self.ancho = 700
        self.alto = 550
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
        self.formulario1.setContentsMargins(160, 0, 0, 50)

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

        self.nombreResidente = QLabel()
        self.nombreResidente.setFixedWidth(250)
        self.nombreResidente.setText("Nombre del Residente:")
        self.nombreResidente.setFont(QFont('VAG_ROUNDED.ttf', 15))
        self.nombreResidente.setStyleSheet('background-color: transparent;')

        self.campo_nombreResidente = QLineEdit()
        self.campo_nombreResidente.setFixedWidth(100)
        self.campo_nombreResidente.setFixedHeight(30)
        # self.campo_nombreResidente.setMaxLength()
        self.campo_nombreResidente.setStyleSheet('background-color: white;')

        self.celularResidente = QLabel()
        self.celularResidente.setFixedWidth(250)
        self.celularResidente.setText("Celular del Residente:")
        self.celularResidente.setFont(QFont('VAG_ROUNDED.ttf', 15))
        self.celularResidente.setStyleSheet('background-color: transparent;')

        self.campo_celularResidente = QLineEdit()
        self.campo_celularResidente.setFixedWidth(100)
        self.campo_celularResidente.setFixedHeight(30)
        # self.campo_celularResidente.setMaxLength(4)
        self.campo_celularResidente.setStyleSheet('background-color: white;')

        self.nombreVisitante = QLabel()
        self.nombreVisitante.setFixedWidth(250)
        self.nombreVisitante.setText("Nombre del Visitante:")
        self.nombreVisitante.setFont(QFont('VAG_ROUNDED.ttf', 15))
        self.nombreVisitante.setStyleSheet('background-color: transparent;')

        self.campo_nombreVisitante = QLineEdit()
        self.campo_nombreVisitante.setFixedWidth(100)
        self.campo_nombreVisitante.setFixedHeight(30)
        # self.campo_nombreVisitante.setMaxLength(4)
        self.campo_nombreVisitante.setStyleSheet('background-color: white;')

        self.vehiculo = QLabel()
        self.vehiculo.setFixedWidth(250)
        self.vehiculo.setText("Ingresa con Vehiculo?:")
        self.vehiculo.setFont(QFont('VAG_ROUNDED.ttf', 15))
        self.vehiculo.setStyleSheet('background-color: transparent;')

        self.campo_vehiculo = QLineEdit()
        self.campo_vehiculo.setFixedWidth(100)
        self.campo_vehiculo.setFixedHeight(30)
        self.campo_vehiculo.setMaxLength(2)
        self.campo_vehiculo.setStyleSheet('background-color: white;')

        self.placa = QLabel()
        self.placa.setFixedWidth(250)
        self.placa.setText("Placa del Vehiculo:")
        self.placa.setFont(QFont('VAG_ROUNDED.ttf', 15))
        self.placa.setStyleSheet('background-color: transparent;')

        self.campo_placa = QLineEdit()
        self.campo_placa.setFixedWidth(100)
        self.campo_placa.setFixedHeight(30)
        self.campo_placa.setMaxLength(7)
        self.campo_placa.setStyleSheet('background-color: white;')

        # agregamos objetos a form1
        self.formulario1.addRow(self.numero_apartamento, self.campo_apartamento)
        self.formulario1.addRow(self.nombreResidente, self.campo_nombreResidente)
        self.formulario1.addRow(self.celularResidente, self.campo_celularResidente)
        self.formulario1.addRow(self.nombreVisitante, self.campo_nombreVisitante)
        self.formulario1.addRow(self.vehiculo, self.campo_vehiculo)
        self.formulario1.addRow(self.placa, self.campo_placa)
        self.vertical.addLayout(self.formulario1)

        # -------- layout horizontal1 ----------
        self.horizontal1 = QHBoxLayout()

        # crear el boton volver
        self.boton_Volver = QPushButton("Volver")
        self.boton_Volver.setFixedWidth(100)
        self.boton_Volver.setFixedHeight(40)
        self.boton_Volver.setStyleSheet('background-color: #2F4F4F; color: #FFFFFF; padding: 10px;'
                                        'border-radius:10px;')
        self.boton_Volver.clicked.connect(self.accion_botonVolver)

        # Crear boton ingresar
        self.boton_ingresar = QPushButton("Buscar")
        self.boton_ingresar.setFixedWidth(100)
        self.boton_ingresar.setFixedHeight(40)
        self.boton_ingresar.setStyleSheet('background-color: #2F4F4F; color: #FFFFFF; padding: 10px;'
                                          'border-radius:10px;')
        self.boton_ingresar.clicked.connect(self.accion_Buscar)

        self.boton_registrar = QPushButton("Registrar")
        self.boton_registrar.setFixedWidth(100)
        self.boton_registrar.setFixedHeight(40)
        self.boton_registrar.setStyleSheet('background-color: #2F4F4F; color: #FFFFFF; padding: 10px;'
                                           'border-radius:10px;')
        self.boton_registrar.clicked.connect(self.accion_Registrar)

        # Agregamos objetos a layout hor1----
        self.horizontal1.addWidget(self.boton_Volver)
        self.horizontal1.addWidget(self.boton_ingresar)
        self.horizontal1.addWidget(self.boton_registrar)
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

    def accionLimpiar(self):
        # datos correctos
        self.datosCorrectos = True

        self.campo_apartamento.setText("")
        self.campo_nombreResidente.setText("")
        self.campo_celularResidente.setText("")
        self.campo_nombreVisitante.setText("")
        self.campo_vehiculo.setText("")
        self.campo_placa.setText("")

    def accion_Buscar(self):
        self.datosCorrectos = True

        if (
                self.campo_apartamento.text() == ''

        ):
            return QMessageBox.warning(
                self,
                'Warning',
                'No ingresó nada en número de apartamento'
            )

        if (
                not self.campo_apartamento.text().isnumeric()
        ):
            return QMessageBox.warning(
                self,
                'Warning',
                'Ingrese solo números en apartamento'
            )

        if (
                self.datosCorrectos
        ):

            self.file = open('datos/residente.txt', 'rb')
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                # obtenemos del string una lista con 11 datos separados por;
                lista = linea.split(";")

                # paramos el bucle si ya no encuentra mas registros en el archivo
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

                # metemos el objeto en la lista de usuarios
                usuarios.append(u)

            # cerramos ael archivo txt
            self.file.close()

            existeDocumento = False

            # buscamos en la lista de usuarios si existe la cedula

            for u in usuarios:
                """comparamos el documento ingresado:
                si correspopnde con el documento, es el usuario correcto:"""

                if u.apartamento == self.campo_apartamento.text():
                    # aqui mostramos las preguntas del formulario
                    self.campo_nombreResidente.setText(u.nombreCompleto)
                    self.campo_celularResidente.setText(u.celular)

                    # indicamos que existen
                    existeDocumento = True

                    break

            if (
                    not existeDocumento
            ):
                return QMessageBox.warning(
                    self,
                    'Warning',
                    'No existe apartamento registrado'
                )

    def accion_Registrar(self):

        # datos correctos
        self.datosCorrectos = True

        if (
                self.campo_apartamento.text() == ''
                or self.campo_nombreVisitante.text() == ''
                or self.campo_celularResidente.text() == ''
                or self.campo_nombreResidente.text() == ''
                or self.campo_vehiculo.text() == ''
                or self.campo_placa.text() == ''):
            return QMessageBox.warning(
                self,
                'Warning',
                'Debe ingresar todos los campos.'
            )

        # si los datos estan correctos
        if self.datosCorrectos:
            # Abrimos el archivo en modo agregar
            self.file = open('datos/visitantes.txt', 'ab')

            # trae el texto de los Qline y los concatena
            self.file.write(bytes(self.campo_apartamento.text() + ";" +
                                  self.campo_nombreResidente.text() + ";" +
                                  self.campo_celularResidente.text() + ";" +
                                  self.campo_nombreVisitante.text() + ";" +
                                  self.campo_vehiculo.text() + ";" +
                                  self.campo_placa.text() + ";" + '\n', encoding='UTF-8'))
            self.file.close()

        self.file = open('datos/visitantes.txt', 'rb')
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            print(linea)
            if linea == '':
                break
        self.file.close()

        self.accionLimpiar()
