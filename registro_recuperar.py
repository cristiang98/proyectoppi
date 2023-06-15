import codecs
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QMessageBox

from consulta_datos import Consulta_datos
from consulta_datos_tabular import Consulta_datos_tabular
from usuarios import Usuarios


class Registro_recuperar(QMainWindow):
    def __init__(self, anterior):
        super().__init__()

        self.Anterior = anterior
        # creacion de la ventana
        self.setWindowTitle("Formulario de registro")
        self.setWindowIcon(QtGui.QIcon('imagenes/sophos.jpeg'))
        self.ancho = 800
        self.alto = 750
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

        self.horizontal1 = QHBoxLayout()
        self.horizontal1.setContentsMargins(0, 0, 50, 0)
        self.botonanterior = QPushButton(icon=QIcon('imagenes/anterior.png'))
        self.botonanterior.setStyleSheet('border-radius: 100px;'
                                         'background-color: transparent;'
                                         'margin-left:30px;')
        self.botonanterior.setFixedSize(50, 40)
        self.botonanterior.setIconSize(QSize(30, 30))
        self.botonanterior.clicked.connect(self.accion_botonAnterior)

        # ahora creamos los letreros (Qlabel())
        self.letrero1 = QLabel(self)
        self.letrero1.setText("Registro de Colaboradores")
        self.letrero1.setFont(QFont('VAG_ROUNDED.ttf', 20))
        self.letrero1.setStyleSheet('background-color: transparent;'
                                    ' color: black; '
                                    'padding: 10px;'
                                    'margin-left: 140px;')

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

        # ---------Creacion del layout izquierdo---------
        self.layoutIzq_form = QFormLayout()
        self.layoutIzq_form.setContentsMargins(60, 0, 0, 0)

        # hacemos los labels informativos
        self.letrero2 = QLabel()
        self.letrero2.setText("Información del\nColaborador")
        self.letrero2.setFont(QFont("Arial", 20))
        self.letrero2.setStyleSheet('color: black;'
                                    'background-color:transparent;')

        # labels y campos

        self.label_nombreCompleto = QLabel()
        self.label_nombreCompleto.setText("Nombre Completo*")
        self.label_nombreCompleto.setStyleSheet('background-color: transparent;')

        self.label_usuario = QLabel()
        self.label_usuario.setText("Ingrese Usuario*")
        self.label_usuario.setStyleSheet('background-color: transparent;')

        self.label_contrasena = QLabel()
        self.label_contrasena.setText("Ingrese Contraseña*")
        self.label_contrasena.setStyleSheet('background-color: transparent;')

        self.label_confirmarContrasena = QLabel()
        self.label_confirmarContrasena.setText("Confirmar Contraseña*")
        self.label_confirmarContrasena.setStyleSheet('background-color: transparent;')

        self.label_documento = QLabel()
        self.label_documento.setText("Documento*")
        self.label_documento.setStyleSheet('background-color: transparent;')

        self.label_correo = QLabel()
        self.label_correo.setText("Correo Electrónico*")
        self.label_correo.setStyleSheet('background-color: transparent;')

        self.label_telefono = QLabel()
        self.label_telefono.setText("Teléfono*")
        self.label_telefono.setStyleSheet('background-color: transparent;')

        self.label_direccion = QLabel()
        self.label_direccion.setText("Dirección*")
        self.label_direccion.setStyleSheet('background-color: transparent;')

        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)
        self.nombreCompleto.setStyleSheet('background-color: white;')

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)
        self.usuario.setStyleSheet('background-color: white;')

        self.contrasena = QLineEdit()
        self.contrasena.setFixedWidth(250)
        self.contrasena.setEchoMode(QLineEdit.Password)
        self.contrasena.setMaxLength(4)
        self.contrasena.setStyleSheet('background-color: white;')

        self.confirmar_contrasena = QLineEdit()
        self.confirmar_contrasena.setFixedWidth(250)
        self.confirmar_contrasena.setMaxLength(4)
        self.confirmar_contrasena.setEchoMode(QLineEdit.Password)
        self.confirmar_contrasena.setStyleSheet('background-color: white;')

        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)
        self.documento.setMaxLength(10)
        self.documento.setStyleSheet('background-color: white;')

        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)
        self.correo.setStyleSheet('background-color: white;')

        self.telefono = QLineEdit()
        self.telefono.setFixedWidth(250)
        self.telefono.setMaxLength(15)
        self.telefono.setStyleSheet('background-color: white;')

        self.direccion = QLineEdit()
        self.direccion.setFixedWidth(250)
        self.direccion.setMaxLength(20)
        self.direccion.setStyleSheet('background-color: white;')

        # Crear boton ingresar
        self.boton_ingresar = QPushButton(icon=QIcon('imagenes/buscar1.png'))
        self.boton_ingresar.setFixedSize(30, 30)
        self.boton_ingresar.setIconSize(QSize(25, 25))
        self.boton_ingresar.setStyleSheet('background-color: transparent;')
        self.boton_ingresar.clicked.connect(self.accionBuscar)

        # Se agrega todo al layout formulario izquierdo
        self.layoutIzq_form.addRow(self.letrero2)
        self.layoutIzq_form.addRow(self.label_nombreCompleto)
        self.layoutIzq_form.addRow(self.nombreCompleto)

        self.layoutIzq_form.addRow(self.label_usuario)
        self.layoutIzq_form.addRow(self.usuario)

        self.layoutIzq_form.addRow(self.label_contrasena)
        self.layoutIzq_form.addRow(self.contrasena)

        self.layoutIzq_form.addRow(self.label_confirmarContrasena)
        self.layoutIzq_form.addRow(self.confirmar_contrasena)

        self.layoutIzq_form.addRow(self.label_documento)
        self.layoutIzq_form.addRow(self.documento, self.boton_ingresar)

        self.layoutIzq_form.addRow(self.label_correo)
        self.layoutIzq_form.addRow(self.correo)

        self.layoutIzq_form.addRow(self.label_telefono)
        self.layoutIzq_form.addRow(self.telefono)

        self.layoutIzq_form.addRow(self.label_direccion)
        self.layoutIzq_form.addRow(self.direccion)

        # Agregamos layout formulario al layout horizontal
        self.horizontal.addLayout(self.layoutIzq_form)
        self.vertical.addLayout(self.horizontal)

        # --------- Layout horixontal--------

        # ---------Layout formulario lado derecho------------
        self.layoutDer_form = QFormLayout()
        self.layoutDer_form.setContentsMargins(80, 0, 0, 0)

        # letreros de informacion derecho
        self.letrero3 = QLabel()
        self.letrero3.setFixedWidth(355)
        self.letrero3.setText("Recuperar Contraseña")
        self.letrero3.setFont(QFont("Arial", 20))
        self.letrero3.setStyleSheet('color: black;'
                                    'background-color: transparent;')

        # Labels y campos lado derecho (preguntas y respuestas)

        # Labels
        self.pregunta1 = QLabel("Pregunta de verificacion 1*")
        self.pregunta1.setStyleSheet('background-color: transparent;')

        self.pregunta2 = QLabel("Pregunta de verificacion 2*")
        self.pregunta2.setStyleSheet('background-color: transparent;')

        self.pregunta3 = QLabel("Pregunta de verificacion 3*")
        self.pregunta3.setStyleSheet('background-color: transparent;')

        self.pregunta4 = QLabel("Respuesta de verificacion 1*")
        self.pregunta4.setStyleSheet('background-color: transparent;')

        self.pregunta5 = QLabel("Respuesta de verificacion 2*")
        self.pregunta5.setStyleSheet('background-color: transparent;')

        self.pregunta6 = QLabel("Respuesta de verificacion 3*")
        self.pregunta6.setStyleSheet('background-color: transparent;')

        # campos QlineEdits
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(250)
        self.respuesta1.setStyleSheet('background-color: white;')

        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(250)
        self.respuesta2.setStyleSheet('background-color: white;')

        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(250)
        self.respuesta3.setStyleSheet('background-color: white;')

        self.respuesta4 = QLineEdit()
        self.respuesta4.setFixedWidth(250)
        self.respuesta4.setStyleSheet('background-color: white;')

        self.respuesta5 = QLineEdit()
        self.respuesta5.setFixedWidth(250)
        self.respuesta5.setStyleSheet('background-color: white;')

        self.respuesta6 = QLineEdit()
        self.respuesta6.setFixedWidth(250)
        self.respuesta6.setStyleSheet('background-color: white;')

        # Creacion de boton buscar y recuperar

        self.botonRecuperar = QPushButton("Recuperar")
        self.botonRecuperar.setFixedWidth(115)
        self.botonRecuperar.setStyleSheet('background-color: #2F4F4F;'
                                          'color: #FFFFFF;'
                                          'padding: 10px;'
                                          'margin-top: 10px;'
                                          'margin-left: 25px;'
                                          'border-radius:10px;'
                                          )
        self.botonRecuperar.clicked.connect(self.accionRecuperar)

        self.botonContinuar = QPushButton("Borrar")
        self.botonContinuar.setFixedWidth(100)
        self.botonContinuar.setStyleSheet('background-color: #2F4F4F;'
                                          'color: #FFFFFF;'
                                          'padding: 10px;'
                                          'margin-top: 10px;'
                                          'margin-left:10px;'
                                          'border-radius:10px;'
                                          )
        self.botonContinuar.clicked.connect(self.accion_delete)

        # Se agrega al layout derecho
        self.layoutDer_form.addRow(self.letrero3)

        self.layoutDer_form.addRow(self.pregunta1)
        self.layoutDer_form.addRow(self.respuesta1)

        self.layoutDer_form.addRow(self.pregunta2)
        self.layoutDer_form.addRow(self.respuesta2)

        self.layoutDer_form.addRow(self.pregunta3)
        self.layoutDer_form.addRow(self.respuesta3)

        self.layoutDer_form.addRow(self.pregunta4)
        self.layoutDer_form.addRow(self.respuesta4)

        self.layoutDer_form.addRow(self.pregunta5)
        self.layoutDer_form.addRow(self.respuesta5)

        self.layoutDer_form.addRow(self.pregunta6)
        self.layoutDer_form.addRow(self.respuesta6)

        self.layoutDer_form.addRow(self.botonRecuperar, self.botonContinuar)

        self.horizontal.addLayout(self.layoutDer_form)
        self.vertical.addLayout(self.horizontal)

        # ----------- horizontal1 ------

        self.horizontal2 = QHBoxLayout()
        self.horizontal2.setContentsMargins(65, 0, 485, 50)

        # Creacion de botones limpiar y registrar

        self.botonregistrar = QPushButton("Registrar")
        self.botonregistrar.setFixedWidth(90)
        self.botonregistrar.setStyleSheet('background-color: #2F4F4F;'
                                          'color: #FFFFFF;'
                                          'padding: 10px;'
                                          ''
                                          'border-radius:10px;'
                                          ''
                                          )

        self.botonregistrar.clicked.connect(self.accionRegistrar)

        self.botonActualizar = QPushButton("Editar")
        self.botonActualizar.setFixedWidth(90)
        self.botonActualizar.setStyleSheet('background-color: #2F4F4F;'
                                           'color: #FFFFFF;'
                                           'padding: 10px;'
                                           ''
                                           'border-radius:10px;'
                                           ''
                                           )

        self.botonActualizar.clicked.connect(self.accion_editar)

        self.horizontal2.addWidget(self.botonregistrar)
        self.horizontal2.addWidget(self.botonActualizar)
        self.vertical.addLayout(self.horizontal2)

        # --------Layout que almacena toda la ventana----------
        self.fondo.setLayout(self.vertical)

    def accionLimpiar(self):

        self.nombreCompleto.setText("")
        self.usuario.setText("")
        self.contrasena.setText("")
        self.confirmar_contrasena.setText("")
        self.documento.setText("")
        self.correo.setText("")
        self.telefono.setText("")
        self.direccion.setText("")
        self.respuesta1.setText("")
        self.respuesta2.setText("")
        self.respuesta3.setText("")
        self.respuesta4.setText("")
        self.respuesta5.setText("")
        self.respuesta6.setText("")

    def accionRegistrar(self):

        # datos correctos
        self.datosCorrectos = True

        if not self.usuario.text().isalpha():
            return QMessageBox.warning(
                self,
                'Warning',
                'Solo letras en usuario.'
            )

        if self.contrasena.text().isalpha():
            return QMessageBox.warning(
                self,
                'Warning',
                'En contraseña solo es válido números.'
            )

        if self.documento.text().isalpha():
            return QMessageBox.warning(
                self,
                'Warning',
                'En documento solo es válido números.'
            )

        if not self.contrasena.text().isalnum():
            self.datos_Correctos = False

            if self.contrasena.text() != '':
                return QMessageBox.warning(
                    self,
                    'Warning',
                    'Ingreso caracteres especiales.'
                )

        # Validacion de passwords
        if (
                self.contrasena.text() != self.confirmar_contrasena.text()
        ):
            return QMessageBox.warning(
                self,
                'Warning',
                'Las contraseñas no son iguales.'
            )

        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.contrasena.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.telefono.text() == ''
                or self.direccion.text() == ''
                or self.respuesta1.text() == ''
                or self.respuesta2.text() == ''
                or self.respuesta3.text() == ''
                or self.respuesta4.text() == ''
                or self.respuesta5.text() == ''
                or self.respuesta6.text() == ''
        ):
            return QMessageBox.warning(
                self,
                'Warning',
                'Debe ingresar todos los campos.'
            )

        # si los datos estan correctos
        if self.datosCorrectos:

            self.file = open('datos/usuarios.txt', 'rb')
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                lista = linea.split(';')

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

                usuarios.append(u)

                if u.documento == self.documento.text():
                    return QMessageBox.warning(
                        self,
                        'Warning',
                        'El documento ya existe.'
                    )

                if u.usuario == self.usuario.text():
                    return QMessageBox.warning(
                        self,
                        'Warning',
                        'El usuario no esta disponible.'
                    )

            self.file.close()

            # Abrimos el archivo en modo agregar
            self.file = open('datos/usuarios.txt', 'ab')

            # trae el texto de los Qline y los concatena
            self.file.write(bytes(self.nombreCompleto.text() + ";" +
                                  self.usuario.text() + ";" +
                                  self.contrasena.text() + ";" +
                                  self.documento.text() + ";" +
                                  self.correo.text() + ";" +
                                  self.telefono.text() + ";" +
                                  self.direccion.text() + ";" +
                                  self.respuesta1.text() + ";" +
                                  self.respuesta2.text() + ";" +
                                  self.respuesta3.text() + ";" +
                                  self.respuesta4.text() + ";" +
                                  self.respuesta5.text() + ";" +
                                  self.respuesta6.text() + ";" + "\n", encoding='UTF-8'))

            self.file.close()

            self.file = open('datos/usuarios.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()

        self.accionLimpiar()

    def accion_editar(self):
        boton = QMessageBox.question(
            self,
            'Confirmation',
            '¿Seguro que quiere ingresar este nuevo registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if boton == QMessageBox.StandardButton.Yes:

            if (
                    self.nombreCompleto.text() == '' or
                    self.usuario.text() == '' or
                    self.contrasena.text() == '' or
                    self.documento.text() == '' or
                    self.correo.text() == '' or
                    self.telefono.text() == '' or
                    self.direccion.text() == '' or
                    self.respuesta1.text() == '' or
                    self.respuesta2.text() == '' or
                    self.respuesta3.text() == '' or
                    self.respuesta4.text() == '' or
                    self.respuesta5.text() == '' or
                    self.respuesta6.text() == ''
            ):
                QMessageBox.warning(
                    self,
                    'Warning',
                    'Debe ingresar todos los campos.'
                )
                return

            # Verificar si las contraseñas son iguales
            if self.contrasena.text() != self.confirmar_contrasena.text():
                QMessageBox.warning(
                    self,
                    'Warning',
                    'Las contraseñas no coinciden.'
                )
                return

            usuarios = []

            # Al leer el archivo, utiliza el módulo 'codecs' para abrirlo con codificación UTF-8
            with codecs.open('datos/usuarios.txt', 'r', 'utf-8') as file:
                for linea in file:
                    linea = linea.strip()
                    if linea:
                        datos = linea.split(';')
                        u = Usuarios(
                            datos[0],
                            datos[1],
                            datos[2],
                            datos[3],
                            datos[4],
                            datos[5],
                            datos[6],
                            datos[7],
                            datos[8],
                            datos[9],
                            datos[10],
                            datos[11],
                            datos[12]
                        )
                        usuarios.append(u)

            # Variables controladoras si existe registro y si se va a editar
            existeRegistro = False
            existeDocumento = False

            for u in usuarios:
                if (
                        u.nombreCompleto == self.nombreCompleto.text() and
                        u.usuario == self.usuario.text() and
                        u.contrasena == self.contrasena.text() and
                        u.documento == self.documento.text() and
                        u.correo == self.correo.text() and
                        u.telefono == self.telefono.text() and
                        u.direccion == self.direccion.text() and
                        u.respuesta1 == self.respuesta1.text() and
                        u.respuesta2 == self.respuesta2.text() and
                        u.respuesta3 == self.respuesta3.text() and
                        u.respuesta4 == self.respuesta4.text() and
                        u.respuesta5 == self.respuesta5.text() and
                        u.respuesta6 == self.respuesta6.text()
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

            # Obtén el documento actual
            documento_actual = self.documento.text()

            for u in usuarios:
                if u.documento == documento_actual:
                    existeDocumento = True
                    u.nombreCompleto = self.nombreCompleto.text()
                    u.usuario = self.usuario.text()
                    u.contrasena = self.contrasena.text()
                    u.documento = self.documento.text()
                    u.correo = self.correo.text()
                    u.telefono = self.telefono.text()
                    u.direccion = self.direccion.text()
                    u.respuesta1 = self.respuesta1.text()
                    u.respuesta2 = self.respuesta2.text()
                    u.respuesta3 = self.respuesta3.text()
                    u.respuesta4 = self.respuesta4.text()
                    u.respuesta5 = self.respuesta5.text()
                    u.respuesta6 = self.respuesta6.text()

            # Al escribir en el archivo, utiliza el módulo 'codecs' para abrirlo con codificación UTF-8
            with codecs.open('datos/usuarios.txt', 'w', 'utf-8') as file:
                for u in usuarios:
                    linea = f"{u.nombreCompleto};{u.usuario};{u.contrasena};{u.documento};{u.correo};{u.telefono};{u.direccion};{u.respuesta1};{u.respuesta2};{u.respuesta3};{u.respuesta4};{u.respuesta5};{u.respuesta6}"
                    file.write(linea + '\n')

            QMessageBox.question(
                self,
                'Confirmation',
                'Los datos del registro se han editado exitosamente.',
                QMessageBox.StandardButton.Ok
            )
            self.accionLimpiar()
            return

    def accionBuscar(self):

        # datos correctos
        self.datosCorrectos = True

        # condicionales de campos
        # ingresa el documento
        if (
                self.documento.text() == ''

        ):
            return QMessageBox.warning(
                self,
                'Warning',
                "si va a buscar preguntas "
                "para recuperar la contraseña.\n"
                "Debe primero,ingresar el documento"
            )

        if (
                not self.documento.text().isnumeric()
        ):
            return QMessageBox.warning(
                self,
                'Warning',
                'Ingrese solo numeros en el documento'
            )

            self.documento.setText('')

        if (
                self.datosCorrectos
        ):

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

                if u.documento == self.documento.text():
                    # aqui mostramos las preguntas del formulario
                    self.nombreCompleto.setText(u.nombreCompleto)
                    self.usuario.setText(u.usuario)
                    self.correo.setText(u.correo)
                    self.telefono.setText(u.telefono)
                    self.direccion.setText(u.direccion)
                    self.respuesta1.setText(u.respuesta1)
                    self.respuesta2.setText(u.respuesta2)
                    self.respuesta3.setText(u.respuesta3)
                    self.respuesta4.setText(u.respuesta4)
                    self.respuesta5.setText(u.respuesta5)
                    self.respuesta6.setText(u.respuesta6)

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
                    'No existe usuario registrado'
                )

    def accion_delete(self):

        boton = QMessageBox.question(
            self,
            'Confirmation',
            '¿Estas seguro de borrar este registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if boton == QMessageBox.StandardButton.Yes:

            if (
                    self.nombreCompleto.text() != '' and
                    self.usuario.text() != '' and
                    self.contrasena.text() != '' and
                    self.documento.text() != '' and
                    self.correo.text() != '' and
                    self.telefono.text() != '' and
                    self.direccion.text() != '' and
                    self.respuesta1.text() != '' and
                    self.respuesta2.text() != '' and
                    self.respuesta3.text() != '' and
                    self.respuesta4.text() != '' and
                    self.respuesta5.text() != '' and
                    self.respuesta6.text() != ''
            ):
                self.file = open('datos/usuarios.txt', 'rb')

                usuarios = []

                while self.file:
                    linea = self.file.readline().decode('UTF-8')
                    lista = linea.split(';')

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

                    usuarios.append(u)

                self.file.close()

                for u in usuarios:

                    if (
                            u.documento == self.documento.text()
                    ):
                        usuarios.remove(u)
                        break

                self.file = open('datos/usuarios.txt', 'wb')

                for u in usuarios:
                    self.file.write(bytes(u.nombreCompleto + ';' +
                                          u.usuario + ';' +
                                          u.contrasena + ';' +
                                          u.documento + ';' +
                                          u.correo + ';' +
                                          u.telefono + ';' +
                                          u.direccion + ';' +
                                          u.respuesta1 + ';' +
                                          u.respuesta2 + ';' +
                                          u.respuesta3 + ';' +
                                          u.respuesta4 + ';' +
                                          u.respuesta5 + ';' +
                                          u.respuesta6 + ';' + '\n', encoding='UTF-8'))
                self.file.close()

                # hacemos que la tabla no se vea en el registro

                return QMessageBox.question(
                    self,
                    'confirmation',
                    'El registro ha sido eliminado exitosamente.',
                    QMessageBox.StandardButton.Yes
                )
                self.accionLimpiar()


    def accionRecuperar(self):

        self.datosCorrectos = True

        if (
                self.respuesta1.text() == '' or
                self.respuesta2.text() == '' or
                self.respuesta3.text() == ''
        ):
            return QMessageBox.warning(
                self,
                'Warning',
                "Para recuperar la contraseña debe:"
                "\nbuscar las preguntas de verificación."
                "\n\nPrimero ingrese su documento y luego"
                "\npresione el boton 'buscar'."
            )

        # Validamos si se buscaron las preguntas pero no se ingresaron las respuestas
        if (
                self.respuesta1.text() != '' and
                self.respuesta4.text() == '' and
                self.respuesta2.text() != '' and
                self.respuesta5.text() == '' and
                self.respuesta3.text() != '' and
                self.respuesta6.text() == ''
        ):
            return QMessageBox.warning(
                self,
                'Warning',
                "Para recuperar la contraseña debe:"
                "\nIngresar las respuestas a cada pregunta."
            )

        # condicional si son correctos
        if (
                self.datosCorrectos
        ):

            # Abrimos el archivo en modo lectura
            linea = self.file = open('datos/usuarios.txt', 'rb')

            # creamos Array lista vacia
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')

                # obtenemos el string una lista de 12 datos separados por ;
                lista = linea.split(";")

                if linea == '':
                    break

                # creamos un objeto tipo cliente llamado u

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
                usuarios.append(u)
            self.file.close()

            # en este punto tenemos la lista con la lista de usuarios

            # variable para controlar si existe el documento

            existeDocumento = False

            resp4 = ''
            resp5 = ''
            resp6 = ''
            passw = ''

            # buscamos en la lista usuario por usuario si existe la cedula:
            for u in usuarios:
                if u.documento == self.documento.text():
                    existeDocumento = True

                    resp4 = u.respuesta4
                    resp5 = u.respuesta5
                    resp6 = u.respuesta6
                    passw = u.contrasena

                    break

            if (
                    self.respuesta4.text().lower().strip() == resp4.lower().strip() and
                    self.respuesta5.text().lower().strip() == resp5.lower().strip() and
                    self.respuesta6.text().lower().strip() == resp6.lower().strip()

            ):
                # limpiamos los campos
                self.accionLimpiar()

                return QMessageBox.warning(
                    self,
                    'Warning',
                    f"Contraseña: {passw}"
                )


            else:

                return QMessageBox.warning(
                    self,
                    'Warning',
                    "Las respuesta son incorrectas"
                    "\npara estas preguntas de recuperación."
                    "\n\nVuelva a intentarlo."

                )

    def accion_botonAnterior(self):
        self.hide()
        self.Anterior.show()

    def accion_botonContinuar(self):
        self.hide()
        self.consulta_datos = Consulta_datos_tabular(self)
        self.consulta_datos.show()
