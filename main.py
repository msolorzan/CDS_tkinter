from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QMessageBox
from PyQt6.QtGui import QFont

from entry_generator import view_order_register
from InsertMenu import ViewSaucerRegister

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(100,100,500,250)
        self.setWindowTitle("Ventana principal")
        self.mode_select()

    def mode_select(self):
        select_label = QLabel(self)
        select_label.setText("Hola, ¿Qué deseas hacer?")
        select_label.setFont(QFont("Arial",10))
        select_label.move(20,54)

        order_enter_button = QPushButton(self)
        order_enter_button.setText("Ingresar pedidos")
        order_enter_button.resize(180,34)
        order_enter_button.move(24,102)
        order_enter_button.clicked.connect(self.order_enter)

        saucer_register_button = QPushButton(self)
        saucer_register_button.setText("Registrar platillo")
        saucer_register_button.resize(180,34)
        saucer_register_button.move(204,102)
        saucer_register_button.clicked.connect(self.saucer_register)

    def order_enter(self):
        self.new_order = view_order_register()
        self.new_order.show()

    def saucer_register(self):
        self.new_saucer = ViewSaucerRegister()
        self.new_saucer.show()

'''from login import *

Login()'''