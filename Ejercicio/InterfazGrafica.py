#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import BaseDeDatos
import Scraping

def cargarDatos():
    titulos, enlaces, autores, fechas, respuestas, visitas = Scraping.scrap()
    for i in range(len(titulos)):
        BaseDeDatos.insertarValoresBaseDeDatos(titulos[i], enlaces[i], autores[i], fechas[i], respuestas[i], visitas[i])

def mostrarTodo():
    BaseDeDatos.consultar("SELECT titulo, autor, fechainic, from TEMA")

def temasMasPopulares():
    lista = BaseDeDatos.consultar("SELECT titulo, autor, fechainic, visitas from TEMA ORDER BY visitas")
    return lista[0:5]

def temasMasActivos():
    lista =  BaseDeDatos.consultar("SELECT titulo, autor, fechainic, respuestas from TEMA ORDER BY respuestas")
    return lista[0:5]

def ventana():
    top = tk.Tk()

    datos = tk.Menubutton(top, text="Datos")
    datos.menu = tk.Menu(datos, tearoff=0)
    datos["menu"] = datos.menu
    datos.grid(row=0, column=0)

    datos.menu.add_command(label="Cargar", command=cargarDatos())
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