import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from orders import *

class InsertMenu(ctk.CTk):
    def insert_dish(self):
        try:
            self.quantity = int(self.entry_num.get())
            self.dish = self.entry_name.get()
            if len(self.dish) == 0:
                tk.messagebox.showerror(title='Error', message='Ingrese un nombre de platillo válida')
            else:
                self.dishes[self.dish] = self.quantity

                self.tree.insert('', 0, values = (self.dish, self.quantity))
                # Configurar el estilo de la fila recién insertada
                self.tree.tag_configure("custom_font", font=("Calibri", 15))
                # Aplicar el estilo a la fila recién insertada
                self.tree.item(self.tree.get_children()[0], tags=("custom_font"))

            # Limpiar los campos y posicionar el cursor en entry_name
            self.entry_name.delete(0, tk.END)
            self.entry_num.delete(0, tk.END)
            self.entry_name.focus_set()

        except:
            tk.messagebox.showerror(title='Error', message='Ingrese una cantidad válida')
        

    def finish(self):
        self.destroy()
        Orders(self.dishes)

    def __init__(self):
        super().__init__()
        self.dishes = dict()
        self.title('Insertar platillos')
        self.geometry('800x600')
        self.resizable(False, False)

        self.columnconfigure(0, weight = 1, uniform = 'a')
        self.rowconfigure(0, weight = 1, uniform = 'a')
        self.rowconfigure(1, weight = 2, uniform = 'a')

        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Treeview",
                        background="#2a2d2e",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638")
        self.style.map('Treeview', background=[('selected', '#22559b')])

        # Configurar la fuente para el encabezado del Treeview
        self.style.configure("Treeview.Heading", 
                        font=("Arial", 15),  # Cambia "Arial" y 15 al tamaño y fuente que desees
                        background="#343638",
                        foreground="white",
                        bordercolor = '#AE8D8D ',
                        borderwidth = 2,
                        relief="ridge")
        self.style.map("Treeview.Heading",
                  background=[('active', '#3484F0')])

        # Frame superior
        self.frame_superior = ctk.CTkFrame(self)
        self.frame_superior.grid(row = 0, column = 0, sticky = 'ns')
        self.frame_inferior = ctk.CTkFrame(self)
        self.frame_inferior.grid(row = 1, column = 0, sticky = 'nsew')


        self.label_name = ctk.CTkLabel(self.frame_superior, text = 'Nombre de platillo')
        self.entry_name = ctk.CTkEntry(self.frame_superior)
        
        self.label_num = ctk.CTkLabel(self.frame_superior, text = 'Cantidad de porciones')
        self.entry_num = ctk.CTkEntry(self.frame_superior)

        self.button_insert = ctk.CTkButton(self.frame_superior, text = 'Insertar platillo', command = self.insert_dish)
        self.button_finish = ctk.CTkButton(self.frame_superior, text = 'Terminar', fg_color = 'red', hover_color = '#974040', command = self.finish)

        self.headers = ['Platillo', 'Cantidad']
        self.tree = tk.ttk.Treeview(self.frame_inferior, columns = self.headers, show = 'headings')
        for header in self.headers:
            self.tree.heading(header, text=header)
            self.tree.column(header, anchor='center')  # Centrar el contenido de la columna

        
        self.label_name.pack(pady = 2)
        self.entry_name.pack(pady = 2)
        self.label_num.pack(pady = 2)
        self.entry_num.pack(pady = 2)
        self.button_insert.pack(padx = 5, pady = 20, side = 'left')
        self.button_finish.pack(padx = 5, pady = 20, side = 'right')


        self.tree.pack(expand = True, fill = 'both')

        self.mainloop()


if __name__ == '__main__':
    InsertMenu()