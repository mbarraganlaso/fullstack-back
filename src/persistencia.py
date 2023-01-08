"""
Operaciones de persistencia
"""

def guardar_pedido(nombre, apellidos):
    """
    Persiste el pedido solicitado en el fichero pedidos.txt
    """
    print("nombre: ", nombre)
    print("apellidos: ", apellidos)
    with open("data/pedidos.txt", "a", encoding="utf-8") as file:
        file.write("-" + nombre + " " + apellidos + "\n")
        file.close()

def comprueba_disponibilidad(tamano):
    """
    Comprueba si hay pizzas disponibles del tamaño solicitado
    """
    if tamano == "S":
        return False
    return True
