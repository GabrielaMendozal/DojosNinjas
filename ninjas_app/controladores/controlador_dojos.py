from flask import Flask, render_template, request , redirect
from ninjas_app import app
from ninjas_app.modelos.modelo_dojos import Dojo
from ninjas_app.modelos.modelo_ninjas import Ninja



@app.route("/", methods = ["GET"])
def inicio():
    return redirect ("/dojos")

@app.route("/dojos", methods = ["GET"])
def desplegarListDojos():
    return render_template("dojo.html", dojos = Dojo.obtenerListaDojos())

@app.route("/dojos", methods = ["POST"])
def agregarDojo():
    nuevoDojo = {
        "name" : request.form["name"]
    } 

    #if nuevoUsuario["first_name"] == "" or nuevoUsuario["last_name"] == "" or nuevoUsuario["email"] == "":
    #    return redirect( '/user/new' )
    
    resultado = Dojo.insertarDojo( nuevoDojo )
    # ToDo: Validar resultado que nos arroja 0
    if type( resultado ) is int and resultado == 0:
        return redirect( '/dojos' )
    else:
        return redirect( '/dojos' )

@app.route("/dojos/<int:id>", methods = ["GET"] )
def desplegarDojoConNinjas(id):
    data = {
        "id": id
    }
    resultado = Dojo.infoDojo(data)
    return render_template ("show.html", dojos = Ninja.obtenerDojoConNinjas(data), resultado =resultado )


