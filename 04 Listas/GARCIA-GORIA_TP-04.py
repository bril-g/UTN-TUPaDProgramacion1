# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
numeros = list(range(4, 101, 4))

print(f"Números del 1 al 100 múltiplos de 4: {numeros}")

# 2) Crear una lista con cinco elementos y mostrar el penúltimo.
frutas = ["manzana", "banana", "naranja", "frutilla", "pera"]

print(f"Frutas: {frutas}")
print(f"Penúltima: {frutas[-2]}")

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
lista_vacia = []

print(f"Lista vacia: {lista_vacia}")

lista_vacia.append("casa")
lista_vacia.append("árbol")
lista_vacia.append("sol")

print(f"Después de append: {lista_vacia}")

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 
# Imprimir la lista resultante por pantalla.
animales = ["perro", "gato", "conejo", "pez"]

print(f"Lista original de animales: {animales}")

animales[1] = "loro"
animales [-1] = "oso"

print(f"Después de reemplazar: {animales}")

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]

numeros.remove(max(numeros))

print(numeros)

# El programa obtiene el número máximo de la lista mediante la función max() 
# y luego lo elimina mediante remove(). Finalmente, imprime la lista actualizada.

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
numeros = list(range(10, 31, 5))

print(f"Dos primeros números: {numeros[0], numeros[1]}")

# 7)  Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]

print(f"Lista original de autos: {autos}")

autos[1] = "tesla"
autos[2] = "mercedes"

print(f"Después de reemplazar: {autos}")

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.
dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(f"Dobles de 5, 10 y 15 usando append: {dobles}")

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

print(f"Lista original de compras: {compras}")

# a) Agregar "jugo" a la lista del tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines"
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")

# d) Imprimir la lista resultante
print(f"Lista resultante {compras}")

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

print(f"Lista anidada: {lista_anidada}")