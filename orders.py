'''import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from entry_generator import EntryGenerator

class Orders(ctk.CTk):
    def __init__(self, dishes):
        super().__init__()
        self.title('CDS control de ventas')
        self.geometry('1020x640')
        self.minsize(800, 500)
        self.maxsize(1820, 1142)
        self.dishes = dishes

        self.columnconfigure(0, weight = 1, uniform = 'a')
        self.rowconfigure(0, weight = 1, uniform = 'a')
        self.rowconfigure(1, weight = 1, uniform = 'a')
        self.rowconfigure(2, weight = 1, uniform = 'a')

        # Frame superior
        self.frame_superior = ctk.CTkFrame(self)
        self.frame_superior.grid(row = 0, column = 0)
        # Frame intermedio
        self.frame_inter = ctk.CTkFrame(self)
        self.frame_inter.grid(row = 1, column = 0)
        # Frame inferior
        self.frame_inferior = ctk.CTkFrame(self)
        self.frame_inferior.grid(row = 2, column = 0)


        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Treeview",
                        background="#2a2d2e",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638",
                        bordercolor="#343638",
                        borderwidth=0)
        self.style.map('Treeview', background=[('selected', '#22559b')])

        # Configurar la fuente para el encabezado del Treeview
        self.style.configure("Treeview.Heading", 
                        font=("Arial", 15),  # Cambia "Arial" y 12 al tamaño y fuente que desees
                        background="#565b5e",
                        foreground="white",
                        relief="flat")
        self.style.map("Treeview.Heading",
                  background=[('active', '#3484F0')])
        
        # Labels datos
        self.label_name = ctk.CTkLabel(self.frame_superior, text='Nombre/alias:')
        self.label_dir = ctk.CTkLabel(self.frame_superior, text='Dirección:')
        self.label_tel = ctk.CTkLabel(self.frame_superior, text='Teléfono:')
        
        self.label_name.grid(row=0, column=0, padx=10, pady=10)
        self.label_dir.grid(row=1, column=0, padx=10, pady=10)
        self.label_tel.grid(row=2, column=0, padx=10, pady=10)

        # Entries datos
        self.entry_name = ctk.CTkEntry(self.frame_superior)
        self.entry_dir = ctk.CTkEntry(self.frame_superior)
        self.entry_tel = ctk.CTkEntry(self.frame_superior)

        self.entry_name.grid(row=0, column=1, padx=10, pady=10)
        self.entry_dir.grid(row=1, column=1, padx=10, pady=10)
        self.entry_tel.grid(row=2, column=1, padx=10, pady=10)

        # Botones
        self.buttnon_add_order = ctk.CTkButton(self.frame_superior, text='Agregar pedido')
        self.button_clear_form = ctk.CTkButton(self.frame_superior, text='Borrar campos escritos')

        self.buttnon_add_order.grid(row=3, column=0, padx=10, pady=10)
        self.button_clear_form.grid(row=3, column=1, padx=10, pady=10)

        self.headers = ['Nombre', 'Dirección', 'Teléfono'] + [dish for dish in list(self.dishes.keys())] + ['Hora de entrega']
        self.tree = tk.ttk.Treeview(self.frame_inferior, columns = self.headers, show = 'headings')
        for head in self.headers:
            self.tree.heading(head, text = head)

        # Entries para ingresar cantidad de platillos en pedidos
        self.entries_dish = EntryGenerator(self.frame_inter, list(self.dishes.keys()))
       

        self.tree.pack(expand = True, fill = 'both')

        self.mainloop()

    def add_dishes(self):
        pass


if __name__ == '__main__':
    platillos = {'Pollo en salsa verde' : 35, 'Caldo de res' : 35, 'Pozole' : 35, 'Carne a la jardinera' : 35, 
                 'Costillas a la BBQ' : 35, 'Papas horneadas rellenas' : 35, 'Caldo de pescado': 35,
                 'Calbacitas a la mexicana' : 35, 'Pollo empanizado' : 35, 'Carne de res empanizada' : 35}
    Orders(platillos)'''