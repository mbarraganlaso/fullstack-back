"""
API PizzaFullstack
"""
from flask import Flask, request, redirect
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
