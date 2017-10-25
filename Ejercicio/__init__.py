#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import BaseDeDatos
# import InterfazGrafica
# import Scraping

mensajeInicial = '''Elija la opción que desee realizar:
1: Crear la base de datos
2: Probar el programa
0: Salir'''

print mensajeInicial

opcion = input()

while True:
    if opcion is 1:
        #BaseDeDatos.cerrarBaseDeDatos()
        print "Base de datos creada correctamente"
        break
    elif opcion is 2:
        print 2
        #InterfazGrafica.ventana()
        break
    elif opcion is 0:
        print "Fin del programa"
        break
    else:
        print mensajeInicial
        opcion = input()