import sys
from PyQt6.QtWidgets import (QApplication,QLabel,
QWidget, QLineEdit, QPushButton,QMessageBox, QCheckBox)
from PyQt6.QtGui import QFont

from registration import view_user_register
from main import MainWindow

class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.initialize_ui()
    
    def initialize_ui(self):
        self.setGeometry(100,100,400,300)
        self.setWindowTitle("Inicio de sesión")
        self.form_generate()
        self.show()

    def form_generate(self):
        self.is_logged = False

        user_label = QLabel(self)
        user_label.setText("Usuario:")
        user_label.setFont(QFont("Arial",10))
        user_label.move(20,54)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(100,50)

        password_label = QLabel(self)
        password_label.setText("Contraseña:")
        password_label.setFont(QFont("Arial",10))
        password_label.move(20,86)

        self.password_input = QLineEdit(self)
        self.password_input.resize(250,24)
        self.password_input.move(100,82)
        self.password_input.setEchoMode(
            QLineEdit.EchoMode.Password)
        
        self.check_view_password = QCheckBox(self)
        self.check_view_password.setText("Ver contraseña")
        self.check_view_password.move(90,110)
        self.check_view_password.toggled.connect(self.show_password)

        login_button = QPushButton(self)
        login_button.setText("Ingresa")
        login_button.resize(320,34)
        login_button.move(20,140)
        login_button.clicked.connect(self.user_login)

        register_button = QPushButton(self)
        register_button.setText("Registrate")
        register_button.resize(320,34)
        register_button.move(20,180)
        register_button.clicked.connect(self.user_register)
    
    def show_password(self,clicked):
        if clicked:
            self.password_input.setEchoMode(
                QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(
                QLineEdit.EchoMode.Password)
    
    def user_login(self):
        users = []
        users_path = "users.txt"

        try:
            with open(users_path, "r") as f:
                for line in f:
                    users.append(line.strip("\n"))
            login_information = f"{self.user_input.text()},{self.password_input.text()}"

            if login_information in users:
                QMessageBox.information(self,"Inicio de sesión",
                "Inicio de sesión exitoso",
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok)
                self.is_logged = True
                self.close()
                self.open_main_window()
            
            else:
                QMessageBox.warning(self, "Mensaje de error",
                "Usuario o contraseña incorrectos",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)

        except FileNotFoundError as e:
            QMessageBox.warning(self, "Mensaje de error",
            "Base de datos de usuarios no encontrada: {e}",
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)

        except Exception as e:
            QMessageBox.warning(self, "Mensaje de error",
            "Error en el servidor",
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)

    def user_register(self):
        self.new_user = view_user_register()
        self.new_user.show()

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())