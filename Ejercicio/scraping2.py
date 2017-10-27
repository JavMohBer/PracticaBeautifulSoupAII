from bs4 import BeautifulSoup
import urllib2

def carga_pagina():
    url1 = "https://foros.derecho.com/foro/20-Derecho-Civil-General"

    req = urllib2.urlopen(url1).read()

    html = BeautifulSoup(req, "html.parser")
    #print html

    fechas =  html.find_all("span", {"class" : "label"})
    #print fechas
    aux_fechas = []
    for fecha in fechas:
        aux_fechas.append(fecha.a.get("title").split(",")[-1])

    #print aux_fechas

    respuestas = html.find_all("a", {"class": "understate"})
    aux_respuestas = []
    for respuesta in respuestas:
        try:
            if respuesta.string.isdigit():
                #print respuesta.string
                aux_respuestas.append(respuesta.string)
        except Exception as e:
            pass
    visitas = html.find_all("ul", {"class": ["threadingstate", "td" , "alt"]})
    aux_visitas = []
    for visita in visitas:
        try :
            li = visita.find_all("li")

            aux_visitas.append(li[1].string.split(":")[-1])
        except Exception as e:
            pass
    return aux_fechas, aux_respuestas, aux_visitas
if "__main__" =="__main__":
    carga_pagina()