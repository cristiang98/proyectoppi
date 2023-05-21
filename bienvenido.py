import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QVBoxLayout, QFormLayout, \
    QPushButton

from login_admin import Login_admin
from login_vigilante import Login_vigilante
from verificacion_admin import Verificacion_admin


class Bienvenido(QMainWindow):
    def __init__(self, parent=None):
        super(Bienvenido, self).__init__(parent)

        self.setWindowTitle("Sophos R.P.H")
        self.setWindowIcon(QIcon('imagenes/sophos.jpeg'))
        self.ancho = 500
        self.alto = 350
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
                                 '210, 255)); '
                                 '')

        self.setCentralWidget(self.fondo)

        self.vertical = QVBoxLayout()

        self.titulo = QLabel()
        self.titulo.setText("¡Bienvenido!")
        self.titulo.setFont(QFont('VAG Rounded.ttf', 20))
        self.titulo.setStyleSheet('color: black;'
                                  'background-color: transparent;'
                                  )
        self.titulo.setAlignment(Qt.AlignCenter)

        # -------------formulario-----------
        self.formulario = QFormLayout()
        self.botonVigilante = QPushButton("Vigilante")
        self.botonVigilante.setFixedWidth(210)
        self.botonVigilante.setFixedHeight(50)
        self.botonVigilante.setStyleSheet('padding: 10px; '
                                          'background-color: #2F4F4F; '
                                          'color: #FFFFFF;'
                                          'margin-left:65px;'
                                          'margin-top:10px;'
                                          'border-radius:10px;'
                                          )
        self.botonVigilante.clicked.connect(self.accion_botonVigilante)

        self.botonAdmin = QPushButton("Administrador")
        self.botonAdmin.setFixedWidth(200)
        self.botonAdmin.setFixedHeight(50)
        self.botonAdmin.setStyleSheet('padding: 10px; '
                                      'background-color: #2F4F4F; '
                                      'color: #FFFFFF;'
                                      'margin-left:55px;'
                                      'margin-top:10px;'
                                      'border-radius:10px;'
                                      )
        self.botonAdmin.clicked.connect(self.accion_botonAdmin)


        # agregamos layout
        self.vertical.addWidget(self.titulo)
        self.formulario.addRow(self.botonVigilante, self.botonAdmin)
        self.vertical.addLayout(self.formulario)

        # -------------Layout horizontal--------
        self.horizontal = QHBoxLayout()

        # icono de sendero verde
        self.icon_sendero = QLabel()
        self.imagen2 = QPixmap('imagenes/imagen_sendero_verde.jpg')
        self.icon_sendero.setPixmap(self.imagen2)
        self.icon_sendero.setScaledContents(True)
        self.setStyleSheet('background-color: transparent;')
        self.icon_sendero.setFixedSize(50, 50)

        # Agregamos icono al horizontal
        self.horizontal.addWidget(self.icon_sendero)
        self.vertical.addLayout(self.horizontal)


        #______Layout de la ventana principal-------
        self.fondo.setLayout(self.vertical)



    def accion_botonVigilante(self):
        self.hide()
        self.login_vigilante = Login_vigilante(self)
        self.login_vigilante.show()

    def accion_botonAdmin(self):
        self.hide()
        self.verificacion_admin = Verificacion_admin(self)
        self.verificacion_admin.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    bienvenido = Bienvenido()
    bienvenido.show()
    sys.exit(app.exec())
