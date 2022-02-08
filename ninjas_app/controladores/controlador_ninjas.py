from flask import Flask, render_template, request , redirect
from ninjas_app import app
from ninjas_app.modelos.modelo_ninjas import Ninja
from ninjas_app.modelos.modelo_dojos import Dojo



    
@app.route ("/ninja/new")
def desplegarRegistro():
    return render_template("new.html", dojos= Dojo.obtenerListaDojos())


@app.route ("/ninja/create", methods = ["POST"])
def registrarNinjas():
    nuevoNinja = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo"]
    }
    
    
    resultado = Ninja.insertarNinja( nuevoNinja )
    print (type(resultado))

    if type( resultado ) == int:
        return redirect("/dojos/" + str(nuevoNinja["dojo_id"]))
    else:
        return redirect ("/ninja/new")    

