import persistencia

with open("data/pedidos.txt", "w", encoding="utf-8") as file:
    file.write("")
    file.close()

pedidos = [
    {"nombre": "Pedro", "apellidos": "Gil de Diego"},
    {"nombre": "Michael", "apellidos": "Jordan"}
]

for pedido in pedidos:
    persistencia.guardar_pedido(pedido["nombre"], pedido["apellidos"])
