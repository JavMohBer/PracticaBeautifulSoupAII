import sqlite3

baseDeDatos = sqlite3.connect("baseDeDatos.db")

def crearBaseDeDatos():
    baseDeDatos.execute('''CREATE TABLE TEMA
            (TITULO         TEXT                  NOT NULL,
             ENLACE         TEXT PRIMARY KEY      NOT NULL,
             AUTOR          TEXT                  NOT NULL,
             FECHAINIC      TEXT                  NOT NULL,
             RESPUESTAS     INTEGER               NOT NULL,
             VISITAS        INTEGER               NOT NULL);''')
    baseDeDatos.commit()

def insertarValoresBaseDeDatos(nombre, enlace, autor, fechainic, respuestas, visitas):
    baseDeDatos.execute("INSERT INTO TEMA (TITULO,ENLACE,AUTOR,FECHAINIC,RESPUESTAS,VISITAS) \
          VALUES (nombre, enlace, autor, fechainic, respuestas, visitas)");

    baseDeDatos.commit()

def consultar(consulta):
    cursor = baseDeDatos.execute(consulta)

def cerrarBaseDeDatos():
    baseDeDatos.close()