# 2. Leer y mostrar productos: 

with open ("productos.txt", "r") as archivo:
    for linea in archivo:

        linea = linea.strip()
        partes = linea.split(",")

        print(partes)

# 3. Agregar productos desde teclado: 

print("Ingrese los datos del nuevo producto:")

nombre = input("Nombre: ")
precio = input("Precio: ")
cantidad = input("Cantidad: ")

nueva_linea = f"{nombre},{precio},{cantidad}\n"

with open("productos.txt", "a") as archivo:
    archivo.write(nueva_linea)

print("¡Producto agregado con éxito!")

# 4. Cargar productos en una lista de diccionarios: 

productos = []

with open ("productos.txt", "r") as archivo:
    for linea in archivo:

        linea = linea.strip()
        partes = linea.split(",")

        diccionario_producto = {
            "nombre": partes[0],
            "precio": partes[1],
            "cantidad": partes[2]
        }

        productos.append(diccionario_producto)

# 5. Buscar producto por nombre: 

busqueda = input("Ingrese el nombre de un producto: ")

encontrado = False

for p in productos:

    if p["nombre"] == busqueda:
        print("Producto encontrado:")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: {p['precio']}")
        print(f"Cantidad: {p['cantidad']}")

        encontrado = True

        break

if encontrado == False:
    print("El producto ingresado no existe.")

# 6. Guardar los productos actualizados: 

with open("productos.txt", "w") as archivo:
    for p in productos:

        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"

        archivo.write(linea)

print("¡Archivo actualizado correctamente!")
