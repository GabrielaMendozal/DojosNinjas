from ninjas_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,id,first_name,last_name, age,created_at,updated_at, dojo_id):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.created_at = created_at
        self.updated_at =updated_at
        self.dojo_id = dojo_id

    @classmethod
    def insertarNinja (cls, nuevoNinja):
        query = "INSERT INTO ninjas ( first_name,last_name,age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s, %(dojo_id)s );"
        resultado = connectToMySQL ("esquema_dojos_y_ninjas").query_db (query,nuevoNinja)
        return resultado


    @classmethod
    def obtenerDojoConNinjas(cls,ninja):
        query = "SELECT n.first_name,n.last_name,n.age FROM dojos d LEFT JOIN ninjas n ON d.id =n.dojo_id WHERE d.id =%(id)s;"
        resultado = connectToMySQL ("esquema_dojos_y_ninjas").query_db (query, ninja)
        return resultado
        