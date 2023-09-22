import tkinter as tk
import customtkinter as ctk

class EntryGenerator(ctk.CTk):
    def __init__(self, parent_window, labels):
        self.window = parent_window
        self.labels = labels

        self.entries = []

        for i, label_text in enumerate(self.labels):
            label = ctk.CTkLabel(self.window, text=label_text)
            label.grid(row = 0, column = i)

            entry = ctk.CTkEntry(self.window)
            entry.grid(row = 1, column = i)
            self.entries.append(entry)

    def start(self):
        self.window.mainloop()

# Para usar esta clase, crea una instancia de la misma, pasando la ventana principal y una lista de etiquetas correspondientes a cada entrada, y luego llama al método start.
if __name__ == '__main__':
    root_window = ctk.CTk()
    labels = ["Label 1:", "Label 2:", "Label 3:", "Label 4:", "Label 5:"]
    generator = EntryGenerator(root_window, labels)
    generator.start()
