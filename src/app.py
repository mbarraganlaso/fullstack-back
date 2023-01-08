"""
API PizzaFullstack
"""
from flask import Flask, request, redirect, Response
import persistencia

app = Flask(__name__)

@app.route("/pizza", methods=['POST'])
def procesa_pedido():
    """
    Servicio para dar de alta un pedido
    """
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    persistencia.guardar_pedido(nombre, apellidos)
    return redirect("http://localhost/solicita_pedido.html", code=302)

@app.route("/checksize",methods=['POST'])
def checksize():
    """
    Comprueba disponibilidad de un tamaño de pizza.
    """
    tamano = request.form.get("tamano")
    mensaje = "Disponible" if persistencia.comprueba_disponibilidad(tamano) else "No disponible"
    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
