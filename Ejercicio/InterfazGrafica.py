#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
#import BaseDeDatos
#import Scraping

def ventana():
    top = tk.Tk()

    datos = tk.Menubutton(top, text="Datos")
    datos.menu = tk.Menu(datos, tearoff=0)
    datos["menu"] = datos.menu
    datos.grid(row=0, column=0)

    datos.menu.add_checkbutton(label="Cargar")
    datos.menu.add_checkbutton(label="Mostrar")
    datos.menu.add_checkbutton(label="Salir")

    buscar = tk.Menubutton(top, text="Buscar")
    buscar.menu = tk.Menu(buscar, tearoff=0)
    buscar["menu"] = buscar.menu
    buscar.grid(row=0, column=1)

    buscar.menu.add_checkbutton(label="Tema")
    buscar.menu.add_checkbutton(label="Autor")
    buscar.menu.add_checkbutton(label="Fecha")

    estadisticas = tk.Menubutton(top, text="Estadísticas")
    estadisticas.menu = tk.Menu(estadisticas, tearoff=0)
    estadisticas["menu"] = estadisticas.menu
    estadisticas.grid(row=0, column=2)

    estadisticas.menu.add_checkbutton(label="Temas más populares")
    estadisticas.menu.add_checkbutton(label="Temas más activos")

    top.mainloop()

if __name__ == '__main__':
    ventana()