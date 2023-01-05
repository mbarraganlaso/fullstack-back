def guardar_pedido(nombre, apellidos):
    print("nombre: ", nombre)
    print("apellidos: ", apellidos)
    with open("data/pedidos.txt", "a", encoding="utf-8") as file:
        file.write("-" + nombre + " " + apellidos + "\n")
        file.close()

