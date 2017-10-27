#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2

def scrap():
    titulos = []
    enlaces = []
    autores = []
    fechas = []
    respuestas = []
    visitas = []

    for i in range(4):
        if i is 1:
            url = urllib2.urlopen("https://foros.derecho.com/foro/20-Derecho-Civil-General").read()
            soup = BeautifulSoup(url, "html.parser")

            elementos = soup.find_all("div", {"class": ["rating", "nonsticky"]})

            aux_fechas = soup.find_all("span", {"class": "label"})

            for fecha in aux_fechas:
                fechas.append(fecha.a.get("title").split(",")[-1])

            aux_respuestas = soup.find_all("a", {"class": "understate"})

            for respuesta in aux_respuestas:
                try:
                    if respuesta.string.isdigit():
                        respuestas.append(respuesta.string)

                except Exception as e:
                    pass

            aux_visitas = soup.find_all("ul", {"class": ["threadingstate", "td", "alt"]})

            for visita in aux_visitas:
                try:
                    li = visita.find_all("li")
                    visitas.append(li[1].string.split(":")[-1])


                except Exception as e:
                    pass

            for elemento in elementos:
                aux = elemento.find_all("h3", {"class": "threadtitle"})
                aux2 = elemento.find_all("div", {"class": "author"})
                for a in aux:
                    titulos.append(a.a.string)
                    enlaces.append("https://foros.derecho.com/" + a.a.get("href"))
                for a2 in aux2:
                    autores.append(a2.span.a.string)

        elif i is 2 or i is 3:
            url = urllib2.urlopen("https://foros.derecho.com/foro/20-Derecho-Civil-General/page" + str(i)).read()
            soup = BeautifulSoup(url, "html.parser")

            elementos = soup.find_all("div", {"class": ["rating", "nonsticky"]})

            aux_fechas = soup.find_all("span", {"class": "label"})

            for fecha in aux_fechas:
                fechas.append(fecha.a.get("title").split(",")[-1])

            aux_respuestas = soup.find_all("a", {"class": "understate"})

            for respuesta in aux_respuestas:
                try:
                    if respuesta.string.isdigit():
                        respuestas.append(respuesta.string)

                except Exception as e:
                    pass

            aux_visitas = soup.find_all("ul", {"class": ["threadingstate", "td", "alt"]})

            for visita in aux_visitas:
                try:
                    li = visita.find_all("li")
                    visitas.append(li[1].string.split(":")[-1])


                except Exception as e:
                    pass

            for elemento in elementos:
                aux = elemento.find_all("h3", {"class": "threadtitle"})
                aux2 = elemento.find_all("div", {"class": "author"})
                for a in aux:
                    titulos.append(a.a.string)
                    enlaces.append("https://foros.derecho.com/" + a.a.get("href"))
                for a2 in aux2:
                    autores.append(a2.span.a.string)
    return titulos, enlaces, autores, fechas, respuestas, visitas