# Se crea una variable llamada 'carrera' con el texto "software engineering"
carrera = "software engineering"

# Aquí se modifica la cadena:
# carrera[:2]  → toma los primeros 2 caracteres (posición 0 y 1): "so"
# "f"          → se agrega la letra "f"
# carrera[3:]  → toma la cadena desde la posición 3 hasta el final: "tware engineering"
# Todo eso se concatena para formar una nueva cadena
carrera = carrera[:2] + "f" + carrera[3:]

# Se imprime el resultado final en pantalla
print(carrera)
