from ninjas_app.config.mysqlconnection import connectToMySQL
from ninjas_app.modelos.modelo_ninjas import Ninja

class Dojo:
    def __init__(self,id,name,created_at,updated_at):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at =updated_at
        self.ninjas = []


    @classmethod
    def obtenerListaDojos (cls):
        query = "SELECT * from dojos ;"
        resultado = connectToMySQL ("esquema_dojos_y_ninjas").query_db (query)
        listaDojos = []
        for dojo in resultado:
            listaDojos.append (Dojo (dojo["id"],dojo["name"],dojo["created_at"],dojo["updated_at"]))
        return listaDojos

    @classmethod
    def insertarDojo (cls, nuevoDojo):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        resultado = connectToMySQL ("esquema_dojos_y_ninjas").query_db (query,nuevoDojo)
        return resultado

    @classmethod
    def infoDojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        resultado = connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)
        return resultado[0]

