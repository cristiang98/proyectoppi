import datetime

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QTabWidget, QLabel, QHBoxLayout, \
    QLineEdit, QPushButton, QMessageBox, QFormLayout, QApplication

from lista_residente import Residente
from modulo_parqueadero import Modulo_parqueadero
from visitante import Visitante
from visitantes_tabular import Visitantes_tabular

# from ingreso_datos import Ingreso_datos

class Ingreso_visitantes(QMainWindow):
    def __init__(self, anterior):
        super().__init__()

        self.ventanaAnterior = anterior

        # hacemos la ventana
        # caracteristicas de la ventana
        self.setWindowTitle("Ingreso de Visitantes")
        self.ancho = 800
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
        self.letrero1.setText("Ingreso de Visitantes")
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

        self.vertical.addSpacing(30)

        self.horizontal = QHBoxLayout()

        # ------ layout form1 ----
        self.formulario1 = QFormLayout()
        self.formulario1.setContentsMargins(130, 0, 0, 0)

        # Label numero apartamento
        self.numero_apartamento = QLabel()
        self.numero_apartamento.setFixedWidth(250)
        self.numero_apartamento.setText("Ingrese Apartamento:")
        self.numero_apartamento.setFont(QFont('VAG_ROUNDED.ttf', 13))
        self.numero_apartamento.setStyleSheet('background-color: transparent;')

        # QlineEdit del numero de apartamento
        self.campo_apartamento = QLineEdit()
        self.campo_apartamento.setFixedWidth(170)
        self.campo_apartamento.setFixedHeight(30)
        self.campo_apartamento.setMaxLength(4)
        self.campo_apartamento.setPlaceholderText("APTO")
        self.campo_apartamento.setAlignment(Qt.AlignCenter)
        self.campo_apartamento.setStyleSheet('background-color: white;')

        self.nombreResidente = QLabel()
        self.nombreResidente.setFixedWidth(250)
        self.nombreResidente.setText("Nombre del Residente:")
        self.nombreResidente.setFont(QFont('VAG_ROUNDED.ttf', 13))
        self.nombreResidente.setStyleSheet('background-color: transparent;')

        self.campo_nombreResidente = QLineEdit()
        self.campo_nombreResidente.setFixedWidth(170)
        self.campo_nombreResidente.setFixedHeight(30)
        self.campo_nombreResidente.setPlaceholderText("Nombre Residente")
        self.campo_nombreResidente.setReadOnly(True)
        self.campo_nombreResidente.setAlignment(Qt.AlignCenter)
        self.campo_nombreResidente.setStyleSheet('background-color: white;')

        self.celularResidente = QLabel()
        self.celularResidente.setFixedWidth(250)
        self.celularResidente.setText("Celular del Residente:")
        self.celularResidente.setFont(QFont('VAG_ROUNDED.ttf', 13))
        self.celularResidente.setStyleSheet('background-color: transparent;')

        self.campo_celularResidente = QLineEdit()
        self.campo_celularResidente.setFixedWidth(170)
        self.campo_celularResidente.setFixedHeight(30)
        self.campo_celularResidente.setPlaceholderText("Celular")
        self.campo_celularResidente.setReadOnly(True)
        self.campo_celularResidente.setAlignment(Qt.AlignCenter)
        self.campo_celularResidente.setStyleSheet('background-color: white;')

        self.nombreVisitante = QLabel()
        self.nombreVisitante.setFixedWidth(250)
        self.nombreVisitante.setText("Nombre del Visitante:")
        self.nombreVisitante.setFont(QFont('VAG_ROUNDED.ttf', 13))
        self.nombreVisitante.setStyleSheet('background-color: transparent;')

        self.campo_nombreVisitante = QLineEdit()
        self.campo_nombreVisitante.setFixedWidth(170)
        self.campo_nombreVisitante.setFixedHeight(30)
        self.campo_nombreVisitante.setMaxLength(25)
        self.campo_nombreVisitante.setPlaceholderText("Nombre")
        self.campo_nombreVisitante.setAlignment(Qt.AlignCenter)
        self.campo_nombreVisitante.setStyleSheet('background-color: white;')

        # Crear boton ingresar
        self.boton_ingresar = QPushButton(icon=QIcon('imagenes/buscar1.png'))
        self.boton_ingresar.setFixedSize(30, 30)
        self.boton_ingresar.setIconSize(QSize(25, 25))
        self.boton_ingresar.setStyleSheet('background-color: transparent;')
        self.boton_ingresar.clicked.connect(self.accion_Buscar)

        # agregamos objetos a form1
        self.formulario1.addRow(self.numero_apartamento)
        self.formulario1.addRow(self.campo_apartamento, self.boton_ingresar)

        self.formulario1.addRow(self.nombreResidente)
        self.formulario1.addRow(self.campo_nombreResidente)

        self.formulario1.addRow(self.celularResidente)
        self.formulario1.addRow(self.campo_celularResidente)

        self.formulario1.addRow(self.nombreVisitante)
        self.formulario1.addRow(self.campo_nombreVisitante)
        self.horizontal.addLayout(self.formulario1)

        # ------ fin form1 ---------

        # ----- form 2 ----------
        self.formulario2 = QFormLayout()
        self.formulario2.setContentsMargins(90, 0, 0, 30)

        self.vehiculo = QLabel()
        self.vehiculo.setFixedWidth(250)
        self.vehiculo.setText("¿Ingresa con Vehiculo?:")
        self.vehiculo.setFont(QFont('VAG_ROUNDED.ttf', 13))
        self.vehiculo.setStyleSheet('background-color: transparent;')

        self.campo_vehiculo = QLineEdit()
        self.campo_vehiculo.setFixedWidth(170)
        self.campo_vehiculo.setFixedHeight(30)
        self.campo_vehiculo.setMaxLength(2)
        self.campo_vehiculo.setPlaceholderText("Si o No")
        self.campo_vehiculo.setAlignment(Qt.AlignCenter)
        self.campo_vehiculo.setStyleSheet('background-color: white;')

        self.placa = QLabel()
        self.placa.setFixedWidth(250)
        self.placa.setText("Placa del Vehiculo:")
        self.placa.setFont(QFont('VAG_ROUNDED.ttf', 13))
        self.placa.setStyleSheet('background-color: transparent;')

        self.campo_placa = QLineEdit()
        self.campo_placa.setFixedWidth(170)
        self.campo_placa.setFixedHeight(30)
        self.campo_placa.setMaxLength(7)
        self.campo_placa.setPlaceholderText("AAA 000")
        self.campo_placa.setAlignment(Qt.AlignCenter)
        self.campo_placa.setStyleSheet('background-color: white;')

        self.fechaVisitante = QLabel()
        self.fechaVisitante.setFixedWidth(250)
        self.fechaVisitante.setText("Fecha de Ingreso:")
        self.fechaVisitante.setFont(QFont('VAG_ROUNDED.ttf', 13))
        self.fechaVisitante.setStyleSheet('background-color: transparent;')

        self.campo_fechaVisitante = QLineEdit()
        self.campo_fechaVisitante.setFixedWidth(170)
        self.campo_fechaVisitante.setFixedHeight(30)
        self.campo_fechaVisitante.setMaxLength(8)
        self.campo_fechaVisitante.setPlaceholderText("DD/MM/AA")
        self.campo_fechaVisitante.setInputMask('99/99/9999')
        self.campo_fechaVisitante.setText(datetime.date.today().strftime('%d/%m/%Y'))
        self.campo_fechaVisitante.setReadOnly(True)
        self.campo_fechaVisitante.setAlignment(Qt.AlignCenter)
        self.campo_fechaVisitante.setStyleSheet('background-color: white;')

        self.horaVisitante = QLabel()
        self.horaVisitante.setFixedWidth(250)
        self.horaVisitante.setText("Hora de ingreso:")
        self.horaVisitante.setFont(QFont('VAG_ROUNDED.ttf', 13))
        self.horaVisitante.setStyleSheet('background-color: transparent;')

        self.campo_horaVisitante = QLineEdit()
        self.campo_horaVisitante.setFixedWidth(170)
        self.campo_horaVisitante.setFixedHeight(30)
        self.campo_horaVisitante.setMaxLength(8)
        self.campo_horaVisitante.setInputMask('99:99:99')
        self.campo_horaVisitante.setText(datetime.datetime.now().strftime('%H:%M:%S'))
        self.campo_horaVisitante.setReadOnly(True)
        self.campo_horaVisitante.setAlignment(Qt.AlignCenter)
        self.campo_horaVisitante.setStyleSheet('background-color: white;')

        self.celdaVisitante = QLabel()
        self.celdaVisitante.setFixedWidth(250)
        self.celdaVisitante.setText("Celda:")
        self.celdaVisitante.setFont(QFont('VAG_ROUNDED.ttf', 13))
        self.celdaVisitante.setStyleSheet('background-color: transparent;')

        self.campo_celdaVisitante = QLineEdit()
        self.campo_celdaVisitante.setFixedWidth(170)
        self.campo_celdaVisitante.setFixedHeight(30)
        self.campo_celdaVisitante.setMaxLength(3)
        self.campo_celdaVisitante.setPlaceholderText("0")
        self.campo_celdaVisitante.setAlignment(Qt.AlignCenter)
        self.campo_celdaVisitante.setStyleSheet('background-color: white;')

        self.boton_parqueadero = QPushButton(icon=QIcon('imagenes/transparencia2.png'))
        self.boton_parqueadero.setFixedSize(30, 30)
        self.boton_parqueadero.setIconSize(QSize(25, 25))
        self.boton_parqueadero.setStyleSheet('background-color: transparent;')

        self.boton_parqueadero.clicked.connect(self.accion_boton_parqueadero)

        self.formulario2.addRow(self.vehiculo)
        self.formulario2.addRow(self.campo_vehiculo)

        self.formulario2.addRow(self.placa)
        self.formulario2.addRow(self.campo_placa)

        self.formulario2.addRow(self.fechaVisitante)
        self.formulario2.addRow(self.campo_fechaVisitante)

        self.formulario2.addRow(self.horaVisitante)
        self.formulario2.addRow(self.campo_horaVisitante)

        self.formulario2.addRow(self.celdaVisitante)
        self.formulario2.addRow(self.campo_celdaVisitante, self.boton_parqueadero)
        # self.campo_celdaVisitante.deleteLater()

        # self.formulario2.addRow(self.boton_parqueadero)

        self.horizontal.addLayout(self.formulario2)

        self.vertical.addLayout(self.horizontal)

        # -------- layout horizontal1 ----------
        self.horizontal1 = QHBoxLayout()
        self.horizontal1.setContentsMargins(200, 0, 200, 0)

        self.boton_registrar = QPushButton("Registrar")
        self.boton_registrar.setFixedWidth(100)
        self.boton_registrar.setFixedHeight(40)
        self.boton_registrar.setStyleSheet('background-color: #2F4F4F; color: #FFFFFF; padding: 10px;'
                                           'border-radius:10px;')
        self.boton_registrar.clicked.connect(self.accion_Registrar)

        self.botonHistorial = QPushButton("Historial")
        self.botonHistorial.setFixedWidth(100)
        self.botonHistorial.setFixedHeight(40)
        self.botonHistorial.setStyleSheet('background-color: #2F4F4F; color: #FFFFFF; padding: 10px;'
                                          'border-radius:10px;')
        self.botonHistorial.clicked.connect(self.accion_botonHistorial)

        # Agregamos objetos a layout hor1----
        self.horizontal1.addWidget(self.boton_registrar)
        self.horizontal1.addWidget(self.botonHistorial)
        self.vertical.addLayout(self.horizontal1)

        self.vertical.addSpacing(30)

        # Layout que se usa para el fondo de la ventana
        self.fondo.setLayout(self.vertical)

    # funcion para volver
    def accion_botonAnterior(self):
        self.hide()
        self.ventanaAnterior.show()

    def accion_boton_parqueadero(self):

        """self.campo_celdaVisitante = QLineEdit()
        self.campo_celdaVisitante.setFixedWidth(170)
        self.campo_celdaVisitante.setFixedHeight(30)
        self.campo_celdaVisitante.setMaxLength(2)
        self.campo_celdaVisitante.setPlaceholderText("0")
        self.campo_celdaVisitante.setAlignment(Qt.AlignCenter)
        self.campo_celdaVisitante.setStyleSheet('background-color: white;')

        self.boton_parqueadero.deleteLater()
        self.formulario2.addRow(self.campo_celdaVisitante)"""
        self.hide()
        self.modulo_parqueadero = Modulo_parqueadero(self)
        self.modulo_parqueadero.show()

    def accion_botonHistorial(self):
        self.hide()
        self.visitantes_tabular = Visitantes_tabular(self)
        self.visitantes_tabular.show()

    def accionLimpiar(self):
        # datos correctos
        self.datosCorrectos = True

        self.campo_apartamento.setText("")
        self.campo_nombreResidente.setText("")
        self.campo_celularResidente.setText("")
        self.campo_nombreVisitante.setText("")
        self.campo_vehiculo.setText("")
        self.campo_placa.setText("")
        self.campo_fechaVisitante.setText("")
        self.campo_horaVisitante.setText("")
        self.campo_celdaVisitante.setText("")

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
                    lista[6],
                    lista[7]
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
                or self.campo_nombreResidente.text() == ''):
            return QMessageBox.warning(
                self,
                'Warning',
                'Debe ingresar todos los campos.'
            )

        if self.campo_vehiculo.text().strip().lower() not in ['si', 'no']:
            QMessageBox.warning(
                self,
                'Warning',
                'En ingresa con vehículo\nsolo escribir "si" o "no".'
            )
            return

        if self.campo_placa.text().strip() and not self.campo_placa.text().replace(' ', '').isalnum():
            QMessageBox.warning(
                self,
                "Advertencia",
                "En placa de vehículo. Solo se permiten letras, números y espacios"
            )
            return

        # si los datos estan correctos
        if self.datosCorrectos:

            self.file = open('datos/visitantes.txt', 'rb')
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                lista = linea.split(';')

                if linea == '':
                    break

                u = Visitante(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8]
                )

                usuarios.append(u)

                if self.campo_celdaVisitante.text().strip() and u.celda == self.campo_celdaVisitante.text():
                    return QMessageBox.warning(
                        self,
                        'Warning',
                        'La celda se encuentra ocupada.'
                    )

            self.file.close()

            placa = self.campo_placa.text().replace(" ", "")
            # Abrimos el archivo en modo agregar
            self.file = open('datos/visitantes.txt', 'ab')

            # trae el texto de los Qline y los concatena
            self.file.write(bytes(self.campo_apartamento.text() + ";" +
                                  self.campo_nombreResidente.text() + ";" +
                                  self.campo_celularResidente.text() + ";" +
                                  self.campo_nombreVisitante.text() + ";" +
                                  self.campo_vehiculo.text() + ";" +
                                  placa + ";" +
                                  self.campo_fechaVisitante.text() + ";" +
                                  self.campo_horaVisitante.text() + ";" +
                                  self.campo_celdaVisitante.text() + ";" + '\n', encoding='UTF-8'))
            self.file.close()

        if self.datosCorrectos:
            placa = self.campo_placa.text().replace(" ", "")
            # Abrimos el archivo en modo agregar
            self.file = open('datos/baseDatos.txt', 'ab')

            # trae el texto de los Qline y los concatena
            self.file.write(bytes(self.campo_apartamento.text() + ";" +
                                  self.campo_nombreResidente.text() + ";" +
                                  self.campo_celularResidente.text() + ";" +
                                  self.campo_nombreVisitante.text() + ";" +
                                  self.campo_vehiculo.text() + ";" +
                                  placa + ";" +
                                  self.campo_fechaVisitante.text() + ";" +
                                  self.campo_horaVisitante.text() + ";" +
                                  self.campo_celdaVisitante.text() + ";" + '\n', encoding='UTF-8'))
            self.file.close()

        self.file = open('datos/visitantes.txt', 'rb')
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            print(linea)
            if linea == '':
                break
        self.file.close()

        self.accionLimpiar()

        self.campo_fechaVisitante.setInputMask('99/99/9999')
        self.campo_fechaVisitante.setText(datetime.date.today().strftime('%d/%m/%Y'))

        self.campo_horaVisitante.setInputMask('99:99:99')
        self.campo_horaVisitante.setText(datetime.datetime.now().strftime('%H:%M:%S'))

        """self.campo_celdaVisitante.deleteLater()
        self.boton_parqueadero = QPushButton("Asignar Parqueadero")
        self.boton_parqueadero.setFixedWidth(150)
        self.boton_parqueadero.setFixedHeight(40)
        self.boton_parqueadero.setStyleSheet('background-color: #2F4F4F; color: #FFFFFF; padding: 10px;'
                                             'border-radius:10px;')
        self.boton_parqueadero.clicked.connect(self.accion_boton_parqueadero)
        self.formulario2.addRow(self.boton_parqueadero)"""
