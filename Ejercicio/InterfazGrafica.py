import Tkinter as tk
import BaseDeDatos

def ventana():
    top = tk.Tk()
    almacenar = tk.Button(top, text="nombre1")
    almacenar.grid(row=0, column=0)

    listar = tk.Button(top, text="nombre2")
    listar.grid(row=0, column=1)

    top.mainloop()