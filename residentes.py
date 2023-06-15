import codecs
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QMessageBox

from consulta_datos import Consulta_datos
from lista_residente import Residente
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
        self.alto = 550
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
        self.vertical = QVBoxLayout()

        # creacion de layout horizontal para la distribucion
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
        self.letrero1.setText("Registro de residentes o\n propietarios")
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

        # -----creacion del formulario---------

        self.horizontalForm = QHBoxLayout()

        self.formulario = QFormLayout()
        self.formulario.setContentsMargins(100, 0, 0, 0)

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

        self.editNombrecompleto = QLineEdit()
        self.editNombrecompleto.setFixedWidth(170)
        self.editNombrecompleto.setFixedHeight(25)
        self.editNombrecompleto.setPlaceholderText("Nombre y Apellido")
        self.editNombrecompleto.setAlignment(Qt.AlignCenter)
        self.editNombrecompleto.setStyleSheet('background-color: white;')

        self.editCedula = QLineEdit()
        self.editCedula.setFixedWidth(170)
        self.editCedula.setFixedHeight(25)
        self.editCedula.setPlaceholderText("Cédula")
        self.editCedula.setAlignment(Qt.AlignCenter)
        self.editCedula.setStyleSheet('background-color: white;')

        self.editCelular = QLineEdit()
        self.editCelular.setFixedWidth(170)
        self.editCelular.setFixedHeight(25)
        self.editCelular.setPlaceholderText("Num Celular")
        self.editCelular.setAlignment(Qt.AlignCenter)
        self.editCelular.setStyleSheet('background-color: white;')

        self.editCorreo = QLineEdit()
        self.editCorreo.setFixedWidth(180)
        self.editCorreo.setFixedHeight(25)
        self.editCorreo.setPlaceholderText("example@gmail.com")
        self.editCorreo.setAlignment(Qt.AlignCenter)
        self.editCorreo.setStyleSheet('background-color: white;')

        self.formulario.addRow(self.labelNombrecompleto)
        self.formulario.addRow(self.editNombrecompleto)

        self.formulario.addRow(self.labelCedula)
        self.formulario.addRow(self.editCedula)

        self.formulario.addRow(self.labelCelular)
        self.formulario.addRow(self.editCelular)

        self.formulario.addRow(self.labelCorreo)
        self.formulario.addRow(self.editCorreo)

        self.horizontalForm.addLayout(self.formulario)

        #  -------------fin form-----------

        self.formulario2 = QFormLayout()
        self.formulario2.setContentsMargins(50, 0, 0, 0)

        self.labelApartamento = QLabel()
        self.labelApartamento.setText("Número de apartamento*")
        self.labelApartamento.setFont(QFont('VAG_ROUNDED.ttf', 12))
        self.labelApartamento.setStyleSheet('background-color: transparent;')

        self.labelPlaca = QLabel()
        self.labelPlaca.setText("Número de placa")
        self.labelPlaca.setFont(QFont('VAG_ROUNDED.ttf', 12))
        self.labelPlaca.setStyleSheet('background-color: transparent;')

        self.labelVehiculo = QLabel()
        self.labelVehiculo.setText("¿Cuenta con Vehículo?")
        self.labelVehiculo.setFont(QFont('VAG_ROUNDED.ttf', 12))
        self.labelVehiculo.setStyleSheet('background-color: transparent;')

        self.labelCelda = QLabel()
        self.labelCelda.setText("Celda que Ocupa")
        self.labelCelda.setFont(QFont('VAG_ROUNDED.ttf', 12))
        self.labelCelda.setStyleSheet('background-color: transparent;')

        # -----EDITS------

        self.editApartamento = QLineEdit()
        self.editApartamento.setFixedWidth(170)
        self.editApartamento.setFixedHeight(25)
        self.editApartamento.setPlaceholderText("APTO")
        self.editApartamento.setAlignment(Qt.AlignCenter)
        self.editApartamento.setStyleSheet('background-color: white;')

        # Crear boton ingresar
        self.boton_ingresar = QPushButton(icon=QIcon('imagenes/buscar1.png'))
        self.boton_ingresar.setFixedSize(30, 30)
        self.boton_ingresar.setIconSize(QSize(25, 25))
        self.boton_ingresar.setStyleSheet('background-color: transparent;')
        self.boton_ingresar.clicked.connect(self.accionBuscar)

        self.editPlaca = QLineEdit()
        self.editPlaca.setFixedWidth(170)
        self.editPlaca.setFixedHeight(25)
        self.editPlaca.setPlaceholderText("AAA 000")
        self.editPlaca.setAlignment(Qt.AlignCenter)
        self.editPlaca.setStyleSheet('background-color: white;')

        self.editVehiculo = QLineEdit()
        self.editVehiculo.setFixedWidth(170)
        self.editVehiculo.setFixedHeight(25)
        self.editVehiculo.setPlaceholderText("Si o No")
        self.editVehiculo.setAlignment(Qt.AlignCenter)
        self.editVehiculo.setStyleSheet('background-color: white;')

        self.editCelda = QLineEdit()
        self.editCelda.setFixedWidth(170)
        self.editCelda.setFixedHeight(25)
        self.editCelda.setMaxLength(3)
        self.editCelda.setPlaceholderText("0")
        self.editCelda.setAlignment(Qt.AlignCenter)
        self.editCelda.setStyleSheet('background-color: white;')

        # agregamos al formulario

        self.formulario2.addRow(self.labelApartamento)
        self.formulario2.addRow(self.editApartamento, self.boton_ingresar)

        self.formulario2.addRow(self.labelVehiculo)
        self.formulario2.addRow(self.editVehiculo)

        self.formulario2.addRow(self.labelPlaca)
        self.formulario2.addRow(self.editPlaca)

        self.formulario2.addRow(self.labelCelda)
        self.formulario2.addRow(self.editCelda)

        self.horizontalForm.addLayout(self.formulario2)

        self.vertical.addLayout(self.horizontalForm)
        self.vertical.addSpacing(60)

        # -------------layout horizontal-----------

        self.horizontal = QHBoxLayout()
        self.horizontal.setContentsMargins(100, 0, 100, 0)

        # botones volver, registrar, editar y borrar

        self.botonRegistrar = QPushButton("Registrar")
        self.botonRegistrar.setFixedWidth(100)
        self.botonRegistrar.setFixedHeight(40)
        self.botonRegistrar.setStyleSheet('background-color: #2F4F4F;'
                                          'color: #FFFFFF;'
                                          'padding: 5px;'
                                          'border-radius:10px'
                                          )
        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        self.botonEditar = QPushButton("Editar")
        self.botonEditar.setFixedWidth(100)
        self.botonEditar.setFixedHeight(40)
        self.botonEditar.setStyleSheet('background-color: #2F4F4F;'
                                       'color: #FFFFFF;'
                                       'padding: 5px;'
                                       'border-radius:10px'
                                       )
        self.botonEditar.clicked.connect(self.accion_editar)

        self.botonBorrar = QPushButton("Borrar")
        self.botonBorrar.setFixedWidth(100)
        self.botonBorrar.setFixedHeight(40)
        self.botonBorrar.setStyleSheet('background-color: #2F4F4F;'
                                       'color: #FFFFFF;'
                                       'padding: 5px;'
                                       'border-radius:10px'
                                       )
        self.botonBorrar.clicked.connect(self.accion_delete)

        self.botonResidentes = QPushButton("Residentes")
        self.botonResidentes.setFixedWidth(100)
        self.botonResidentes.setFixedHeight(40)
        self.botonResidentes.setStyleSheet('background-color: #2F4F4F;'
                                           'color: #FFFFFF;'
                                           'padding: 5px;'
                                           'border-radius:10px'
                                           )
        self.botonResidentes.clicked.connect(self.accion_botonResidentes)

        self.horizontal.addWidget(self.botonRegistrar)
        self.horizontal.addWidget(self.botonEditar)
        self.horizontal.addWidget(self.botonBorrar)
        self.horizontal.addWidget(self.botonResidentes)

        self.vertical.addLayout(self.horizontal)

        self.vertical.addSpacing(30)

        self.fondo.setLayout(self.vertical)

    def accion_botonAnterior(self):
        self.hide()
        self.Anterior.show()

    def limpiar(self):
        self.editNombrecompleto.setText("")
        self.editCedula.setText("")
        self.editCelular.setText("")
        self.editCorreo.setText("")
        self.editApartamento.setText("")
        self.editVehiculo.setText("")
        self.editPlaca.setText("")
        self.editCelda.setText("")

    def accionBuscar(self):

        # datos correctos
        self.datosCorrectos = True

        # condicionales de campos

        if (
                not self.editApartamento.text().isnumeric()
        ):
            return QMessageBox.warning(
                self,
                'Warning',
                'Ingrese solo números en apartamento.'
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

            # en este punto tenemos la lista de usuarios con todos los usuarios

            existeDocumento = False

            # buscamos en la lista de usuarios si existe la cedula

            for u in usuarios:
                """comparamos el documento ingresado:
                si correspopnde con el documento, es el usuario correcto:"""

                if u.apartamento == self.editApartamento.text():
                    # aqui mostramos las preguntas del formulario
                    self.editNombrecompleto.setText(u.nombreCompleto)
                    self.editCedula.setText(u.cedula)
                    self.editCelular.setText(u.celular)
                    self.editCorreo.setText(u.correo)
                    self.editVehiculo.setText(u.vehiculo3)
                    self.editPlaca.setText(u.placa)
                    self.editCelda.setText(u.celda)

                    # indicamos que existen
                    existeDocumento = True

                    break

            # si no existe usuario con este documento
            if (
                    not existeDocumento
            ):
                return QMessageBox.warning(
                    self,
                    'Warning',
                    'No existe apartamento registrado.'
                )

    def accion_botonRegistrar(self):

        # datos correctos
        self.datosCorrectos = True

        if (
                self.editNombrecompleto.text() == ''
                or self.editCedula.text() == ''
                or self.editCelular.text() == ''
                or self.editCorreo.text() == ''
                or self.editApartamento.text() == ''
        ):
            return QMessageBox.warning(
                self,
                'Warning',
                'Debe ingresar todos los campos.'
            )

        if not (self.editNombrecompleto.text().replace(' ', '').isalpha() and
                self.editVehiculo.text().replace(' ', '').isalpha()
        ):
            return QMessageBox.warning(
                self,
                'Warning',
                'El nombre y el vehículo solo deben contener letras.'
            )

        if (
                not self.editCedula.text().isdigit() or
                not self.editCelular.text().isdigit() or
                not self.editApartamento.text().isdigit() or
                not self.editCelda.text().isdigit()
        ):
            return QMessageBox.warning(
                self,
                'Warning',
                'Cédula, Celular, Apto y Celda solo deben contener números.'
            )

        if self.datosCorrectos:
            # si los datos estan correctos

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

                if (u.apartamento == self.editApartamento.text()
                ):
                    return QMessageBox.warning(
                        self,
                        'Warning',
                        'El apartamento se encuentra registrado.'
                    )

                if (u.placa == self.editPlaca.text()
                ):
                    return QMessageBox.warning(
                        self,
                        'Warning',
                        'La placa del vehículo se encuentra registrada.'
                    )

                if (u.celda == self.editCelda.text()
                ):
                    return QMessageBox.warning(
                        self,
                        'Warning',
                        'La celda se encuentra ocupada.'
                    )

            # cerramos ael archivo txt
            self.file.close()

            existeResidente = False
            placa = self.editPlaca.text().replace(" ", "")
            # Abrimos el archivo en modo agregar
            self.file = open('datos/residente.txt', 'ab')

            # trae el texto de los Qline y los concatena
            self.file.write(bytes(self.editNombrecompleto.text() + ";" +
                                  self.editCedula.text() + ";" +
                                  self.editCelular.text() + ";" +
                                  self.editCorreo.text() + ";" +
                                  self.editApartamento.text() + ";" +
                                  self.editVehiculo.text() + ";" +
                                  placa + ";" +
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

    def accion_editar(self):
        boton = QMessageBox.question(
            self,
            'Confirmation',
            '¿Seguro que quiere ingresar este nuevo registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if boton == QMessageBox.StandardButton.Yes:

            if (
                    self.editNombrecompleto.text() == '' or
                    self.editCedula.text() == '' or
                    self.editCelular.text() == '' or
                    self.editCorreo.text() == '' or
                    self.editApartamento.text() == '' or
                    self.editVehiculo.text() == ''
            ):
                QMessageBox.warning(
                    self,
                    'Warning',
                    'Debe ingresar todos los campos.'
                )
                return

            if not (self.editNombrecompleto.text().replace(' ', '').isalpha() and
                    self.editVehiculo.text().replace(' ', '').isalpha()
            ):
                return QMessageBox.warning(
                    self,
                    'Warning',
                    'El nombre y el vehículo solo deben contener letras.'
                )

            if (
                    not self.editCedula.text().isdigit() or
                    not self.editCelular.text().isdigit() or
                    not self.editApartamento.text().isdigit() or
                    not self.editCelda.text().isdigit()
            ):
                return QMessageBox.warning(
                    self,
                    'Warning',
                    'Cédula, Celular, Apto y Celda solo deben contener números.'
                )

            usuarios = []

            # Al leer el archivo, utiliza el módulo 'codecs' para abrirlo con codificación UTF-8
            with codecs.open('datos/residente.txt', 'r', 'utf-8') as file:
                for linea in file:
                    linea = linea.strip()
                    if linea:
                        datos = linea.split(';')
                        u = Residente(
                            datos[0],
                            datos[1],
                            datos[2],
                            datos[3],
                            datos[4],
                            datos[5],
                            datos[6],
                            datos[7]
                        )
                        usuarios.append(u)

            # Variables controladoras si existe registro y si se va a editar
            existeRegistro = False
            existeDocumento = False

            for u in usuarios:
                if (
                        u.nombreCompleto == self.editNombrecompleto.text() and
                        u.cedula == self.editCedula.text() and
                        u.celular == self.editCelular.text() and
                        u.correo == self.editCorreo.text() and
                        u.apartamento == self.editApartamento.text() and
                        u.vehiculo3 == self.editVehiculo.text() and
                        u.placa == self.editPlaca.text() and
                        u.celda == self.editCelda.text()
                ):
                    existeRegistro = True
                    break

            if existeRegistro:
                QMessageBox.warning(
                    self,
                    'Warning',
                    'Registro duplicado, no se puede registrar'
                )
                return

            # Obtén el apartamento actual
            apartamento_actual = self.editApartamento.text()

            for u in usuarios:
                if u.apartamento == apartamento_actual:
                    existeDocumento = True
                    u.nombreCompleto = self.editNombrecompleto.text()
                    u.cedula = self.editCedula.text()
                    u.celular = self.editCelular.text()
                    u.correo = self.editCorreo.text()
                    u.apartamento = self.editApartamento.text()
                    u.vehiculo3 = self.editVehiculo.text()
                    u.placa = self.editPlaca.text()
                    u.celda = self.editCelda.text()

            # Al escribir en el archivo, utiliza el módulo 'codecs' para abrirlo con codificación UTF-8
            with codecs.open('datos/residente.txt', 'w', 'utf-8') as file:
                for u in usuarios:
                    linea = f"{u.nombreCompleto};{u.cedula};{u.celular};{u.correo};{u.apartamento};{u.vehiculo3};{u.placa};{u.celda}"
                    file.write(linea + '\n')

            QMessageBox.question(
                self,
                'Confirmation',
                'Los datos del registro se han editado exitosamente.',
                QMessageBox.StandardButton.Ok
            )
            self.limpiar()
            return

    def accion_delete(self):

        boton = QMessageBox.question(
            self,
            'Confirmation',
            '¿Estas seguro de borrar este registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if boton == QMessageBox.StandardButton.Yes:

            if (
                    self.editNombrecompleto.text() != '' and
                    self.editCedula.text() != '' and
                    self.editCelular.text() != '' and
                    self.editCorreo.text() != '' and
                    self.editApartamento.text() != '' and
                    self.editVehiculo.text() != '' and
                    self.editPlaca.text() != '' and
                    self.editCelda.text() != ''
            ):
                self.file = open('datos/residente.txt', 'rb')

                usuarios = []

                while self.file:
                    linea = self.file.readline().decode('UTF-8')
                    lista = linea.split(';')

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

                    usuarios.append(u)

                self.file.close()

                for u in usuarios:

                    if (
                            u.apartamento == self.editApartamento.text()
                    ):
                        usuarios.remove(u)
                        break

                self.file = open('datos/residente.txt', 'wb')

                for u in usuarios:
                    self.file.write(bytes(u.nombreCompleto + ';' +
                                          u.cedula + ';' +
                                          u.celular + ';' +
                                          u.correo + ';' +
                                          u.apartamento + ';' +
                                          u.vehiculo3 + ';' +
                                          u.placa + ';' +
                                          u.celda + ';' + '\n', encoding='UTF-8'))
                self.file.close()
                self.limpiar()

                # hacemos que la tabla no se vea en el registro

                return QMessageBox.question(
                    self,
                    'confirmation',
                    'El registro ha sido eliminado exitosamente.',
                    QMessageBox.StandardButton.Yes
                )

    def accion_botonResidentes(self):
        self.hide()
        self.residente_tabular = Residente_tabular(self)
        self.residente_tabular.show()
