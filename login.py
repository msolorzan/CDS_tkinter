import tkinter as tk
import customtkinter as ctk
from InsertMenu import *

class Login(ctk.CTk):

    def login(self):
        user_name = self.entry_user.get()
        password = self.entry_password.get()
        if user_name == 'Mikessxx' and password == '12345':
            self.destroy()
            InsertMenu()
        else:
            tk.messagebox.showerror(title='Error', message='Usuario o contraseña incorrecto')

    def __init__(self):
        super().__init__()
        self.title('Inicio de sesión')
        self.geometry('800x600')
        self.resizable(False, False)

        self.columnconfigure(0, weight = 1, uniform = 'a')
        self.columnconfigure(1, weight = 1, uniform = 'a')
        self.rowconfigure(0, weight = 1, uniform = 'a')

        self.left_frame = ctk.CTkFrame(self)
        self.right_frame = ctk.CTkFrame(self)

        self.left_frame.columnconfigure(0, weight = 1, uniform = 'a')
        self.left_frame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight = 1, uniform = 'a')

        self.label_user = ctk.CTkLabel(self.left_frame, text = 'Usuario')
        self.entry_user = ctk.CTkEntry(self.left_frame)
        
        self.label_password = ctk.CTkLabel(self.left_frame, text = 'Contraseña')
        self.entry_password = ctk.CTkEntry(self.left_frame)

        self.button_session = ctk.CTkButton(self.left_frame, text = 'Iniciar sesión', command = self.login)

        self.label_color = ctk.CTkLabel(self.right_frame, bg_color = '#F3BA48', text = None)

        self.left_frame.grid(row = 0, column = 0, sticky = 'nsew')
        self.right_frame.grid(row = 0, column = 1, sticky = 'nsew')
        self.label_user.grid(row = 2, column = 0, sticky = 's')
        self.entry_user.grid(row = 3, column = 0, sticky = 'n')
        self.label_password.grid(row = 4, column = 0, sticky = 's')
        self.entry_password.grid(row = 5, column = 0, sticky = 'n')
        self.entry_password.configure(show = '*')
        self.button_session.grid(row = 6, column = 0, sticky = 's')
        self.label_color.pack(expand = True, fill = 'both')
        self.bind('<Return>', func = (lambda event: self.login()))
        self.mainloop()

if __name__ == '__main__':
    Login()