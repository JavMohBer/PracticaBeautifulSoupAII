#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import BaseDeDatos
#import Scraping

def mostrarTodo():
    BaseDeDatos.consultar("SELECT nombre from TEMA")

def buscarPorTema():
    BaseDeDatos.consultar()

def temasMasPopulares():
    BaseDeDatos.consultar()

def temasMasActivos():
    BaseDeDatos.consultar()

def ventana():
    top = tk.Tk()

    datos = tk.Menubutton(top, text="Datos")
    datos.menu = tk.Menu(datos, tearoff=0)
    datos["menu"] = datos.menu
    datos.grid(row=0, column=0)

    datos.menu.add_command(label="Cargar")
    datos.menu.add_command(label="Mostrar", command=mostrarTodo())
    datos.menu.add_command(label="Salir", command=top.quit)

    buscar = tk.Menubutton(top, text="Buscar")
    buscar.menu = tk.Menu(buscar, tearoff=0)
    buscar["menu"] = buscar.menu
    buscar.grid(row=0, column=1)

    buscar.menu.add_command(label="Tema")
    buscar.menu.add_command(label="Autor")
    buscar.menu.add_command(label="Fecha")

    estadisticas = tk.Menubutton(top, text="Estadísticas")
    estadisticas.menu = tk.Menu(estadisticas, tearoff=0)
    estadisticas["menu"] = estadisticas.menu
    estadisticas.grid(row=0, column=2)

    estadisticas.menu.add_command(label="Temas más populares", command=temasMasPopulares())
    estadisticas.menu.add_command(label="Temas más activos", command=temasMasActivos())

    top.mainloop()

if __name__ == '__main__':
    ventana()