# Práctico 6: Estructuras de datos complejas

# 1) Diccionario precios_frutas

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# 2) Actualizar los precios de las siguientes frutas

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

# 3) Crear una lista que contenga únicamente las frutas sin los precios

frutas = list(precios_frutas.keys())

# 4) Escribí un programa que permita almacenar y consultar números telefónicos

contactos = {}

for i in range(5):
    nombre = input("Ingrese un nombre como clave: ").title()
    numero = input("Ingrese un número como valor: ")

    contactos[nombre] = numero

consultar = input("Ingrese el nombre que desea consultar: ").title()

if consultar in contactos:
    print(f"{consultar}: {contactos[consultar]}")

else:
    print("Ese nombre no está en la agenda.")

# 5) Solicita al usuario una frase

frase = input("Ingrese una frase: ")

palabras = frase.split()
palabras_unicas = set(palabras)

print(f"Palabras únicas: {palabras_unicas}")

palabras_repetidas = {}

for palabra in palabras:
    palabras_repetidas[palabra] = palabras_repetidas.get(palabra, 0) + 1

print(f"Recuento: {palabras_repetidas}")

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno

for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ").title()
    nota = input("Ingrese las notas del alumno: ")

    notas_float = []
    notas_texto = nota.split()

    for n in notas_texto:
        notas_float.append(float(n))

    notas_tupla = tuple(notas_float)
    promedio = sum(notas_tupla) / len(notas_tupla)

    print(f"El promedio de {nombre} es: {promedio:.2f}\n")

# 7) Dado dos sets de números, representando dos listas de estudiantes
#    que aprobaron Parcial 1 y Parcial 2

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {3, 4, 5, 6, 7}

print(f"Estudiantes que aprobaron ambos parciales: {parcial1.intersection(parcial2)}")
print(f"Estudiantes que aprobaron solo uno de los dos parciales: {parcial1.union(parcial2) - parcial1.intersection(parcial2)}")
print(f"Lista total de estudiantes que aprobaron al menos un parcial: {parcial1.union(parcial2)}")

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 

productos = {"Oreo": 5,
            "Coca-Cola": 10,
            "Doritos": 15, 
            "KitKat": 20, 
            "Nescafé": 25}

print(f"Productos: {productos}\n")

while True:
    print("\n--- Menú de Inventario ---")
    print("Opción 1: Consultar el stock de un producto ingresado.")
    print("Opción 2: Agregar unidades al stock si el producto ya existe.")
    print("Opción 3: Agregar un nuevo producto si no existe.")
    print("Opción 4: Salir.")

    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        producto = input("Ingrese el producto que desee consultar: ").title()

        if producto in productos:
            print(f"El stock de {producto} es: {productos[producto]}")
        else:
            print(f"El producto '{producto}' no existe en el inventario.")

    elif opcion == 2:
        producto = input("Ingrese el producto que desee reestockear: ").title()

        if producto in productos:
            stock = int(input("Ingrese la cantidad de unidades que desea agregar al stock: "))
            productos[producto] += stock
            print(f"El nuevo stock de {producto} es: {productos[producto]}")
        else:
            print(f"El producto '{producto}' no existe en el inventario.")

    elif opcion == 3:
        producto = input("Ingrese el producto que desee agregar: ").title()

        if producto not in productos:
            stock_inicial = int(input(f"Ingrese el stock inicial para {producto}: "))
            productos[producto] = stock_inicial
            print(f"Producto '{producto}' agregado con éxito. Inventario actualizado: {productos}")
        else:
            print(f"El producto '{producto}' ya existe en el inventario.")

    elif opcion == 4:
        print("¡Gracias por usar el sistema de inventario!")
        break
    else:
        print("Opción inválida, intente nuevamente.")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:30"): "Clase de Programación",
    ("viernes", "18:00"): "Gimnasio"
}

dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora (ej: 10:00): ")

busqueda = (dia, hora)

if busqueda in agenda:
    print(f"Evento encontrado: {agenda[busqueda]}")
else:
    print("No hay ninguna actividad programada en ese día y hora.")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario 
paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
}

paises_invertido = {}

for pais, capital in paises.items():
    paises_invertido[capital] = pais

print(f"Original: {paises}")
print(f"Invertido: {paises_invertido}")