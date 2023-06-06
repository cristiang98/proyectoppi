import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QTableWidgetItem, QTableWidget, QScrollArea, QMessageBox, \
    QToolBar, QAction

from lista_residente import Residente
from visitante import Visitante


class Visitantes_tabular(QMainWindow):
    def __init__(self, anterior):
        super().__init__()

        self.Anterior = anterior
        # creacion de la ventana
        self.setWindowTitle("Lista de residentes")
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

        # creacion de layout horizontal para la distribucion
        self.vertical = QVBoxLayout()

        self.file = open('datos/visitantes.txt', 'rb')
        self.usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')
            lista = linea.split(";")

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

        # ---- Fin toolbar------

        # hacemos los labels informativos
        self.letrero1 = QLabel()
        self.letrero1.setText("Lista de Residentes")
        self.letrero1.setFont(QFont("VAG_ROUNDED.ttf", 20))
        self.letrero1.setStyleSheet('color: black;'
                                    'background-color: transparent;')
        self.letrero1.setAlignment(Qt.AlignCenter)
        self.vertical.addWidget(self.letrero1)

        self.vertical.addSpacing(100)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet('background-color: white;')

        # para crear la tabla para que se vean de forma tabular
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(9)

        # definimos los numeros de colimnas que tendra la tabla

        self.tabla.setColumnWidth(0, 150)
        self.tabla.setColumnWidth(1, 200)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 200)
        self.tabla.setColumnWidth(4, 100)
        self.tabla.setColumnWidth(5, 100)
        self.tabla.setColumnWidth(6, 100)
        self.tabla.setColumnWidth(7, 100)
        self.tabla.setColumnWidth(8, 100)

        self.tabla.setHorizontalHeaderLabels(["Apartamento",
                                              "Nombre del Residente",
                                              "Celular",
                                              "Nombre del visitante",
                                              "Vehiculo",
                                              "Placa",
                                              "Fecha",
                                              "Hora",
                                              "Celda"
                                              ])

        self.tabla.setRowCount(self.numeroUsuarios)

        for u in self.usuarios:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.apartamento))
            # evitar que se deje modificar
            self.tabla.item(self.contador, 0).setFlags(Qt.ItemIsEnabled)

            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.nombreCompleto))
            self.tabla.item(self.contador, 1).setFlags(Qt.ItemIsEnabled)

            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.celular))
            self.tabla.item(self.contador, 2).setFlags(Qt.ItemIsEnabled)

            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.nomVisitante))
            #self.tabla.item(self.contador, 3).setFlags(Qt.ItemIsEnabled)

            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.vehiculo2))
            #self.tabla.item(self.contador, 4).setFlags(Qt.ItemIsEnabled)

            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.placa))
            #self.tabla.item(self.contador, 5).setFlags(Qt.ItemIsEnabled)

            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.fecha))
            self.tabla.item(self.contador, 6).setFlags(Qt.ItemIsEnabled)

            self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.hora))
            self.tabla.item(self.contador, 7).setFlags(Qt.ItemIsEnabled)

            self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.celda))
            #self.tabla.item(self.contador, 8).setFlags(Qt.ItemIsEnabled)

            self.contador += 1

        self.scrollArea.setWidget(self.tabla)
        self.vertical.addWidget(self.scrollArea)

        self.vertical.addStretch()

        # creacion layout horizontal botones
        self.horizontal = QHBoxLayout()

        # Boton volver

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(100)
        self.botonVolver.setFixedHeight(40)
        self.botonVolver.setStyleSheet('background-color: #2F4F4F;'
                                       'color: #FFFFFF;'
                                       'padding: 5px;'
                                       'border-radius:10px;')

        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        # Se agrega el boton al layout vertical

        self.horizontal.addWidget(self.botonVolver)
        self.vertical.addLayout(self.horizontal)

        self.vertical.addSpacing(30)

        # layout horizontal para el icono sendero verde
        self.horizontal2 = QHBoxLayout()

        # icono de sendero verde
        self.icon_sendero = QLabel()
        self.imagen2 = QPixmap('imagenes/imagen_sendero_verde.png')
        self.icon_sendero.setStyleSheet('background-color: transparent;')
        self.icon_sendero.setPixmap(self.imagen2)
        self.icon_sendero.setScaledContents(True)
        self.icon_sendero.setFixedSize(50, 50)
        self.horizontal2.addWidget(self.icon_sendero)
        self.vertical.addLayout(self.horizontal2)

        self.fondo.setLayout(self.vertical)

    def metodo_botonVolver(self):
        self.hide()
        self.Anterior.show()

    def accion_delete(self):

        return QMessageBox.warning(
            self,
            'Warning',
            'Boton inhabilitado.'
        )
        """filaActual = self.tabla.currentRow()

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
                    self.tabla.item(filaActual, 6).text() != ''
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
                        lista[6]
                    )

                    usuarios.append(u)

                self.file.close()

                for u in usuarios:

                    if (
                            u.cedula == self.tabla.item(filaActual, 1).text()
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
                                          u.placa + ';' +
                                          u.celda + ';' + '\n', encoding='UTF-8'))
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
                self.tabla.removeRow(filaActual)"""

    def accion_agregar(self):

        return QMessageBox.warning(
            self,
            'Warning',
            'boton inhabilitado.'
        )
        """ultimafila = self.tabla.rowCount()

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
        self.tabla.setItem(ultimafila, 8, QTableWidgetItem(''))"""

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
                    self.tabla.item(filaActual, 8).text() != ''
            ):

                datosVacios = False

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

                self.file.close()

                # variables controladoras si existe registro y si se va a editar
                existeRegistro = False
                existeDocumento = False



                if not existeRegistro:

                    for u in usuarios:

                        if existeDocumento == True:

                            u.apartamento = self.tabla.item(filaActual, 0).text()
                            u.nombreCompleto = self.tabla.item(filaActual, 1).text()
                            u.celular = self.tabla.item(filaActual, 2).text()
                            u.nomVisitante = self.tabla.item(filaActual, 3).text()
                            u.vehiculo2 = self.tabla.item(filaActual, 4).text()
                            u.placa = self.tabla.item(filaActual, 5).text()
                            u.fecha = self.tabla.item(filaActual, 6).text()
                            u.hora = self.tabla.item(filaActual, 7).text()
                            u.celda = self.tabla.item(filaActual, 8).text()

                            self.file = open('datos/visitantes.txt', 'wb')

                            for u in usuarios:
                                self.file.write(bytes(
                                    u.apartamento + ';' +
                                    u.nombreCompleto + ';' +
                                    u.celular + ';' +
                                    u.nomVisitante + ';' +
                                    u.vehiculo2 + ';' +
                                    u.placa + ';' +
                                    u.fecha + ';' +
                                    u.hora + ';' +
                                    u.celda + ';' + '\n', encoding='UTF-8'
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
                        self.file = open('datos/visitantes.txt', 'ab')

                        self.file.write(bytes(
                            self.tabla.item(filaActual, 0).text() + ';' +
                            self.tabla.item(filaActual, 1).text() + ';' +
                            self.tabla.item(filaActual, 2).text() + ';' +
                            self.tabla.item(filaActual, 3).text() + ';' +
                            self.tabla.item(filaActual, 4).text() + ';' +
                            self.tabla.item(filaActual, 6).text() + ';' +
                            self.tabla.item(filaActual, 7).text() + ';' +
                            self.tabla.item(filaActual, 8).text() + ';' + '\n', encoding='UTF-8'))

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
