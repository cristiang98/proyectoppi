import math
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QWidget, QButtonGroup, QGridLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QToolBar, QAction, QMessageBox

from usuarios import Usuarios


class Consulta_datos_tabular(QMainWindow):
    def __init__(self, anterior):
        super().__init__()

        self.Anterior = anterior
        # creacion de la ventana
        self.setWindowTitle("Usuarios Registrados")
        self.setWindowIcon(QtGui.QIcon('imagenes/sophos.jpeg'))
        self.ancho = 900
        self.alto = 400
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

        self.file = open('datos/usuarios.txt', 'rb')
        self.usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')
            lista = linea.split(";")

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

            self.usuarios.append(u)
        self.file.close()

        self.numeroUsuarios = len(self.usuarios)
        self.contador = 0

        # ---- Construccion del toolbar----
        self.toolbar = QToolBar('Main Toolbar')
        self.toolbar.setIconSize(QSize(25, 25))
        self.addToolBar(self.toolbar)

        # toolbar eliminar
        self.delete = QAction(QIcon('imagenes/borrar.png'), "&borrar", self)
        self.delete.triggered.connect(self.accion_delete)
        self.toolbar.addAction(self.delete)

        # toolbar agregar
        self.agregar = QAction(QIcon('imagenes/agregar.png'), "&agregar", self)
        self.agregar.triggered.connect(self.accion_agregar)
        self.toolbar.addAction(self.agregar)

        # toolbar editar
        self.editar = QAction(QIcon('imagenes/editar.png'), "&editar", self)
        self.editar.triggered.connect(self.accion_editar)
        self.toolbar.addAction(self.editar)

        # toolbar buscar
        self.actualizar = QAction(QIcon('imagenes/actualizar1.png'), "&Actualizar", self)
        self.actualizar.triggered.connect(self.reiniciar_scroll)
        self.toolbar.addAction(self.actualizar)

        self.labelApto = QLabel("Apartamento: ")
        self.labelApto.setStyleSheet('margin-left: 420px;')
        self.toolbar.addWidget(self.labelApto)

        self.campo_apartamento = QLineEdit()
        self.campo_apartamento.setFixedWidth(100)
        self.toolbar.addWidget(self.campo_apartamento)

        # toolbar buscar
        self.buscar = QAction(QIcon('imagenes/buscar1.png'), "&Buscar", self)
#        self.buscar.triggered.connect(self.accion_buscar)
        self.toolbar.addAction(self.buscar)

        # ---- Fin toolbar------

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

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet('background-color: white;')

        # para crear la tabla para que se vean de forma tabular
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(13)

        # definimos los numeros de colimnas que tendra la tabla

        self.tabla.setColumnWidth(0, 150)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 150)
        self.tabla.setColumnWidth(4, 150)
        self.tabla.setColumnWidth(5, 150)
        self.tabla.setColumnWidth(6, 150)
        self.tabla.setColumnWidth(7, 150)
        self.tabla.setColumnWidth(8, 150)
        self.tabla.setColumnWidth(9, 150)
        self.tabla.setColumnWidth(10, 150)
        self.tabla.setColumnWidth(11, 150)
        self.tabla.setColumnWidth(12, 150)

        self.tabla.setHorizontalHeaderLabels(["Nombre",
                                              "Usuario",
                                              "Contraseña",
                                              "Documento",
                                              "Correo",
                                              "teléfono",
                                              "dirección",
                                              "Pregunta 1",
                                              "Pregunta 2",
                                              "Pregunta 3",
                                              "Respuesta 1",
                                              "Respuesta 2",
                                              "Respuesta 3"
                                              ])

        self.tabla.setRowCount(self.numeroUsuarios)

        for u in self.usuarios:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.nombreCompleto))
            # no dejar se que edite
            self.tabla.item(self.contador, 0).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.contrasena))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
            # evitar que se deje modificar
            self.tabla.item(self.contador, 3).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.telefono))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.direccion))
            self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.respuesta1))
            self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.respuesta2))
            self.tabla.setItem(self.contador, 9, QTableWidgetItem(u.respuesta3))
            self.tabla.setItem(self.contador, 10, QTableWidgetItem(u.respuesta4))
            self.tabla.setItem(self.contador, 11, QTableWidgetItem(u.respuesta5))
            self.tabla.setItem(self.contador, 12, QTableWidgetItem(u.respuesta6))

            self.contador += 1

        self.scrollArea.setWidget(self.tabla)
        self.vertical.addWidget(self.scrollArea)

        self.vertical.addSpacing(30)

        self.fondo.setLayout(self.vertical)

    def accion_botonAnterior(self):
        self.hide()
        self.Anterior.show()

    def accion_delete(self):
        filaActual = self.tabla.currentRow()

        if filaActual < 0:
            return QMessageBox.warning(self, "Warning", "Para borrar, debe seleccionar un registro")

        boton = QMessageBox.question(
            self,
            'Confirmation',
            '¿Estas seguro de borrar este registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if boton == QMessageBox.StandardButton.Yes:

            if (
                    self.tabla.item(filaActual, 0).text() != '' and
                    self.tabla.item(filaActual, 1).text() != '' and
                    self.tabla.item(filaActual, 2).text() != '' and
                    self.tabla.item(filaActual, 3).text() != '' and
                    self.tabla.item(filaActual, 4).text() != '' and
                    self.tabla.item(filaActual, 5).text() != '' and
                    self.tabla.item(filaActual, 6).text() != '' and
                    self.tabla.item(filaActual, 7).text() != '' and
                    self.tabla.item(filaActual, 8).text() != '' and
                    self.tabla.item(filaActual, 9).text() != '' and
                    self.tabla.item(filaActual, 10).text() != '' and
                    self.tabla.item(filaActual, 11).text() != '' and
                    self.tabla.item(filaActual, 12).text() != ''
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
                            u.documento == self.tabla.item(filaActual, 3).text()
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

                self.tabla.removeRow(filaActual)

                return QMessageBox.question(
                    self,
                    'confirmation',
                    'El registro ha sido eliminado exitosamente.',
                    QMessageBox.StandardButton.Yes
                )
            else:
                # Hacemos que en la tabla no se vea el registro en caso de tratarse de na fila vacia
                self.tabla.removeRow(filaActual)

    def accion_agregar(self):
        ultimafila = self.tabla.rowCount()

        # insertas una fila nueva despues de la ultima fila
        self.tabla.insertRow(ultimafila)

        # LLenamos las celdas con espacios en blancos

        self.tabla.setItem(ultimafila, 0, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 1, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 2, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 3, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 4, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 5, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 6, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 7, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 8, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 9, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 10, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 11, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 12, QTableWidgetItem(''))

    def accion_editar(self):

        filaActual = self.tabla.currentRow()

        if filaActual < 0:
            return QMessageBox.warning(
                self,
                'Warning',
                'Para ingresar debe seleccionar un registro.',

            )

        boton = QMessageBox.question(
            self,
            'Confirmation',
            '¿Seguro que quiere ingresar este nuevo registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        datosVacios = True

        if boton == QMessageBox.StandardButton.Yes:

            if (
                    self.tabla.item(filaActual, 0).text() != '' and
                    self.tabla.item(filaActual, 1).text() != '' and
                    self.tabla.item(filaActual, 2).text() != '' and
                    self.tabla.item(filaActual, 3).text() != '' and
                    self.tabla.item(filaActual, 4).text() != '' and
                    self.tabla.item(filaActual, 5).text() != '' and
                    self.tabla.item(filaActual, 6).text() != '' and
                    self.tabla.item(filaActual, 7).text() != '' and
                    self.tabla.item(filaActual, 8).text() != '' and
                    self.tabla.item(filaActual, 9).text() != '' and
                    self.tabla.item(filaActual, 10).text() != '' and
                    self.tabla.item(filaActual, 11).text() != '' and
                    self.tabla.item(filaActual, 12).text() != ''
            ):

                datosVacios = False

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

                # variables controladoras si existe registro y si se va a editar
                existeRegistro = False
                existeDocumento = False

                for u in usuarios:

                    if (
                            u.nombreCompleto == self.tabla.item(filaActual, 0).text() and
                            u.usuario == self.tabla.item(filaActual, 1).text() and
                            u.contrasena == self.tabla.item(filaActual, 2).text() and
                            u.documento == self.tabla.item(filaActual, 3).text() and
                            u.correo == self.tabla.item(filaActual, 4).text() and
                            u.telefono == self.tabla.item(filaActual, 5).text() and
                            u.direccion == self.tabla.item(filaActual, 6).text() and
                            u.respuesta1 == self.tabla.item(filaActual, 7).text() and
                            u.respuesta2 == self.tabla.item(filaActual, 8).text() and
                            u.respuesta3 == self.tabla.item(filaActual, 9).text() and
                            u.respuesta4 == self.tabla.item(filaActual, 10).text() and
                            u.respuesta5 == self.tabla.item(filaActual, 11).text() and
                            u.respuesta6 == self.tabla.item(filaActual, 12).text()
                    ):
                        existeRegistro = True

                        return QMessageBox.warning(
                            self,
                            'Warning',
                            'Resgistro duplicado, no se pude registrar')
                        break

                if not existeRegistro:

                    for u in usuarios:

                        if (
                                u.documento == self.tabla.item(filaActual, 3).text()
                        ):

                            existeDocumento = True

                            u.nombreCompleto = self.tabla.item(filaActual, 0).text()
                            u.usuario = self.tabla.item(filaActual, 1).text()
                            u.contrasena = self.tabla.item(filaActual, 2).text()
                            u.documento = self.tabla.item(filaActual, 3).text()
                            u.correo = self.tabla.item(filaActual, 4).text()
                            u.telefono = self.tabla.item(filaActual, 5).text()
                            u.direccion = self.tabla.item(filaActual, 6).text()
                            u.respuesta1 = self.tabla.item(filaActual, 7).text()
                            u.respuesta2 = self.tabla.item(filaActual, 8).text()
                            u.respuesta3 = self.tabla.item(filaActual, 9).text()
                            u.respuesta4 = self.tabla.item(filaActual, 10).text()
                            u.respuesta5 = self.tabla.item(filaActual, 11).text()
                            u.respuesta6 = self.tabla.item(filaActual, 12).text()

                            self.file = open('datos/usuarios.txt', 'wb')

                            for u in usuarios:
                                self.file.write(bytes(
                                    u.nombreCompleto + ';' +
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
                                    u.respuesta6 + ';' + '\n', encoding='UTF-8'
                                ))

                            self.file.close()

                            return QMessageBox.question(
                                self,
                                'Confirmation',
                                'Los datos del registro se han editados exitosamente.',
                                QMessageBox.StandardButton.Ok
                            )
                            break

                    if not existeDocumento:
                        self.file = open('datos/usuarios.txt', 'ab')

                        self.file.write(bytes(
                            self.tabla.item(filaActual, 0).text() + ';' +
                            self.tabla.item(filaActual, 1).text() + ';' +
                            self.tabla.item(filaActual, 2).text() + ';' +
                            self.tabla.item(filaActual, 3).text() + ';' +
                            self.tabla.item(filaActual, 4).text() + ';' +
                            self.tabla.item(filaActual, 5).text() + ';' +
                            self.tabla.item(filaActual, 6).text() + ';' +
                            self.tabla.item(filaActual, 7).text() + ';' +
                            self.tabla.item(filaActual, 8).text() + ';' +
                            self.tabla.item(filaActual, 9).text() + ';' +
                            self.tabla.item(filaActual, 10).text() + ';' +
                            self.tabla.item(filaActual, 11).text() + ';' +
                            self.tabla.item(filaActual, 12).text() + ';' + '\n', encoding='UTF-8'))

                        self.file.seek(0, 2)
                        self.file.close()
                    return QMessageBox.question(
                        self,
                        'Confirmation',
                        'Los datos del registro se han ingresado correctamente.',
                        QMessageBox.StandardButton.Ok

                    )

            if datosVacios:
                return QMessageBox.warning(
                    self,
                    'Warning',
                    'Debe ingresar todos los datos en el registro'
                )

    def reiniciar_scroll(self):

        # Limpiar la tabla
        self.tabla.clearContents()

        # Obtener todos los visitantes
        visitantes = self.usuarios

        # Actualizar la tabla con los datos de todos los visitantes
        self.tabla.setRowCount(len(visitantes))

        for row, visitante in enumerate(visitantes):
            self.tabla.setItem(row, 0, QTableWidgetItem(visitante.nombreCompleto))
            self.tabla.setItem(row, 1, QTableWidgetItem(visitante.usuario))
            self.tabla.setItem(row, 2, QTableWidgetItem(visitante.contrasena))
            self.tabla.setItem(row, 3, QTableWidgetItem(visitante.documento))
            self.tabla.setItem(row, 4, QTableWidgetItem(visitante.correo))
            self.tabla.setItem(row, 5, QTableWidgetItem(visitante.telefono))
            self.tabla.setItem(row, 6, QTableWidgetItem(visitante.direccion))
            self.tabla.setItem(row, 7, QTableWidgetItem(visitante.respuesta1))
            self.tabla.setItem(row, 8, QTableWidgetItem(visitante.respuesta2))
            self.tabla.setItem(row, 9, QTableWidgetItem(visitante.respuesta3))
            self.tabla.setItem(row, 10, QTableWidgetItem(visitante.respuesta4))
            self.tabla.setItem(row, 11, QTableWidgetItem(visitante.respuesta5))
            self.tabla.setItem(row, 12, QTableWidgetItem(visitante.respuesta6))


        self.tabla.resizeColumnsToContents()