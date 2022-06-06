from .connection import Connection
from flask import json
from psycopg2.errors import UniqueViolation

class Query(Connection):

# --------------- CONSUMO A QUERY DE BASE DE DATOS --------------------
    def get_pasillos(self):
        cnx = self.connect()
        cursor = cnx.cursor()
        try:
            query= f"""SELECT * FROM pasillos"""
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            return lista
        except Exception as e:
            print(e)
            return "prueba"
    def get_sub_pasillos(self,idPasillo):
        cnx = self.connect()
        cursor = cnx.cursor()
        try:
            query= f"""SELECT * FROM subpasillos WHERE idpasillo = {idPasillo}"""
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
            print(lista)
            self.closeConnection(cnx)
            return lista
        except Exception as e:
            print(e)
            return "prueba"
    def get_productos_sub_pasillos(self,idSubPasillo):
        cnx = self.connect()
        cursor = cnx.cursor()
        try:
            query= f"""SELECT p.idproducto, p.titulo, p.descripcion, p.precio, p.img FROM productos p
            JOIN subpasillo_productos ON subpasillo_productos.idproducto = p.idproducto
            WHERE subpasillo_productos.idsubpasillo = {idSubPasillo}"""
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
            print(lista)
            self.closeConnection(cnx)
            return lista
        except Exception as e:
            print(e)
            return "prueba"
    def get_productos_pasillos(self,idPasillo):
        cnx = self.connect()
        cursor = cnx.cursor()
        try:
            query= f"""SELECT p.idproducto, p.titulo, p.descripcion, p.precio, p.img FROM productos p
            JOIN subpasillo_productos ON subpasillo_productos.idproducto = p.idproducto
            JOIN subpasillos ON subpasillos.idsubpasillo = subpasillo_productos.idsubpasillo
            WHERE subpasillos.idpasillo = {idPasillo}"""
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
            print(lista)
            self.closeConnection(cnx)
            return lista
        except Exception as e:
            print(e)
            return "prueba"


    def insertar(self, tabla ,datoModificar):
        cnx = self.connect()
        cursor = cnx.cursor()
        var=list(datoModificar)
        datos=[]
        for k in datoModificar:
            datos.append(str(datoModificar[str(k)]))

        var_text=", ".join(var)
        datos_text="','".join(datos)

        
        
        try:
            query= f""" INSERT INTO {tabla} ({var_text}) VALUES ('{datos_text}') RETURNING * ;"""
            print(query)
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            return lista
        except Exception as e:
            print(e)
            return f"error {e}"

    def modificar(self, tabla,datosBuscar, datoModificar):
        cnx = self.connect()
        cursor = cnx.cursor()

        try:
            for k in datoModificar:
                query= f""" UPDATE {tabla} SET  {  f"{k} = '{str(datoModificar[str(k)])}'"}   WHERE {datosBuscar[0][0]} = {datosBuscar[0][1]} RETURNING * ;"""
                print(query)
                cursor.execute(query)
                cnx.commit()
            lista = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            return lista
        except Exception as e:
            print(e)
            return f"error {e}"