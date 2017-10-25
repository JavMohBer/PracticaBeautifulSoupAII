import sqlite3

baseDeDatos = sqlite3.connect("baseDeDatos.db")

def crearBaseDeDatos():
    baseDeDatos.execute('''CREATE TABLE NOMBRE
             (ID INT PRIMARY KEY    NOT NULL,
             NOMBRE         TEXT    NOT NULL,
             CATEGORIA      TEXT    NOT NULL,
             LINK           TEXT    NOT NULL,
             PRECIO         REAL    NOT NULL,
             PRECIODESC     REAL,
             DESCUENTO      REAL);''')
    baseDeDatos.commit()

def insertarValoresBaseDeDatos(atributos):
    baseDeDatos.execute("INSERT INTO NOMBRE (ID,NOMBRE,CATEGORIA,LINK,PRECIO, PRECIODESC, DESCUENTO) \
          VALUES (1, 'Nombre', 'Categoria', 'link.html', 20.00, NULL, NULL)");

    baseDeDatos.commit()

def consultas():
    cursor = baseDeDatos.execute("SELECT id FROM PRODUCTO")

def cerrarBaseDeDatos():
    baseDeDatos.close()