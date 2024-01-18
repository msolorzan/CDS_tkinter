from PyQt6.QtWidgets import (QDialog, QLabel,
QPushButton,QLineEdit,QMessageBox)
from PyQt6.QtGui import QFont

class view_user_register(QDialog):
    
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.form_generate()
    
    def form_generate(self):
        self.setGeometry(100,100,400,300)
        self.setWindowTitle("Ventana de registro")

        user_label = QLabel(self)
        user_label.setText("Usuario")
        user_label.setFont(QFont("Arial",10))
        user_label.move(20,44)

        self.user_input = QLineEdit(self)
        self.user_input.resize(150,24)
        self.user_input.move(190,40)
        
        password_1_label = QLabel(self)
        password_1_label.setText("Contraseña:")
        password_1_label.setFont(QFont("Arial",10))
        password_1_label.move(20,74)

        self.password_1_input = QLineEdit(self)
        self.password_1_input.resize(150,24)
        self.password_1_input.move(190,70)
        self.password_1_input.setEchoMode(
            QLineEdit.EchoMode.Password)
        
        password_2_label = QLabel(self)
        password_2_label.setText("Confirma contraseña:")
        password_2_label.setFont(QFont("Arial",10))
        password_2_label.move(20,104)

        self.password_2_input = QLineEdit(self)
        self.password_2_input.resize(150,24)
        self.password_2_input.move(190,100)
        self.password_2_input.setEchoMode(
            QLineEdit.EchoMode.Password)
        
        create_button = QPushButton(self)
        create_button.setText("Crear")
        create_button.resize(150,32)
        create_button.move(20,170)
        create_button.clicked.connect(self.create_user)
        
        cancel_button = QPushButton(self)
        cancel_button.setText("Cancelar")
        cancel_button.resize(150,32)
        cancel_button.move(170,170)
        cancel_button.clicked.connect(self.cancel_create)

    def create_user(self):
        user_path = "users.txt"
        user = self.user_input.text()
        password1 = self.password_1_input.text()
        password2 = self.password_2_input.text()

        if password1 == "" or password2 == "" or user == "":
            QMessageBox.warning(self, "Error",
            "Por favor ingrese datos validos o llene todos los campos",
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)
        
        elif password1 != password2:
            QMessageBox.warning(self, "Error",
            "Las contraseñas no son iguales",
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)
             
        else:
            try:
                with open(user_path,"a+") as f:
                    f.write(f"{user},{password1}\n")
                QMessageBox.information(self, "Creación exitosa",
                "Usuario creado correctamene",
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok)
                self.close()

            except FileNotFoundError as e:
                QMessageBox.warning(self, "Error",
                f"La base de datos de usuario no existe:{e}",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)

    def cancel_create(self):
        self.close()