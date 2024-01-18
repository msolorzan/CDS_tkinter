import sys   
from PyQt6.QtWidgets import (QDialog, QLabel,
QPushButton,QLineEdit,QMessageBox, QApplication)
from PyQt6.QtGui import QFont

from verification import ValueVerification

class ViewDishRegister(QDialog):
     
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.form_generate()
        self.show()
    
    def form_generate(self):
        self.setGeometry(100,100,400,300)
        self.setWindowTitle("Ventana de registro de platillos")

        dish_label = QLabel(self)
        dish_label.setText("Nombre del platillo:")
        dish_label.setFont(QFont("Arial",10))
        dish_label.move(20,44)

        self.dish_input = QLineEdit(self)
        self.dish_input.resize(150,24)
        self.dish_input.move(190,40)
        
        price_dish_label = QLabel(self)
        price_dish_label.setText("Precio:")
        price_dish_label.setFont(QFont("Arial",10))
        price_dish_label.move(20,74)

        self.price_dish_input = QLineEdit(self)
        self.price_dish_input.resize(150,24)
        self.price_dish_input.move(190,70)
        
        create_button = QPushButton(self)
        create_button.setText("Registar platilllo")
        create_button.resize(150,32)
        create_button.move(20,170)
        create_button.clicked.connect(self.create_dish)
        
        cancel_button = QPushButton(self)
        cancel_button.setText("Cancelar registro")
        cancel_button.resize(150,32)
        cancel_button.move(170,170)
        cancel_button.clicked.connect(self.cancel_create)

    def create_dish(self):
        dish_path = "dishes.txt"
        dish = self.dish_input.text()
        price = self.price_dish_input.text()

        verifier_numeric = ValueVerification(price, "numeric")
        verifier_string = ValueVerification(dish, "string")

        result_numeric, self.numeric_value = verifier_numeric.verify()
        result_string, self.string_value = verifier_string.verify()
        
        if result_numeric == False and self.numeric_value == None:
            QMessageBox.warning(self, "Error",
            "Ingrese el precio en numero",
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)
        
        elif result_numeric == False or result_string == False:
            QMessageBox.warning(self, "Error",
            "Por favor ingrese datos validos o llene todos los campos",
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)
             
        else:
            try:
                with open(dish_path,"a+") as f:
                    f.write(f"{dish},{price}\n")
                QMessageBox.information(self, "Creación exitosa",
                "Platillo creado correctamene",
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok)
                self.close()

            except FileNotFoundError as e:
                QMessageBox.warning(self, "Error",
                f"La base de datos de los platillos no existe:{e}",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)

    def cancel_create(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = ViewDishRegister()
    sys.exit(app.exec())