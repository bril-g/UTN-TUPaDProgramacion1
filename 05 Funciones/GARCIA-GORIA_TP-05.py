# Práctico 2: Funciones en Python

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”.
def imprimir_hola_mundo(saludo):
    print(f"¡Hola, {saludo}!")

imprimir_hola_mundo("Mundo") 

# 2. Crear una función llamada saludar_usuario(nombre) que reciba 
# como parámetro un nombre y devuelva un saludo personalizado.
nombre_usuario = input("Ingrese su nombre: ").title()

def saludar_usuario(saludo):
    print(f"¡Hola, {saludo}!")

saludar_usuario(nombre_usuario)

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
nombre_usuario = input("Ingrese su nombre: ").title()
apellido_usuario = input("Ingrese su apellido: ").title()
edad_usuario = int(input("Ingrese su edad (solo números): "))
residencia_usuario = input("Ingrese su lugar de residencia: ").title()

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Hola, soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia_usuario}.")

informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro 
# y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro 
# y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones 
# para mostrar los resultados.
radio_circulo = float(input("Ingrese el radio del circulo: "))

pi = 3.14

def calcular_area_circulo(radio):
    area = pi * radio ** 2
    print(f"Área del circulo: {area}")

calcular_area_circulo(radio_circulo)

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
segundos_usuario = int(input("Ingrese una cantidad de segundos: "))

def segundos_a_horas(segundos):
    horas = segundos // 3600
    print(f"Cantidad de horas correspondientes: {horas}")

segundos_a_horas(segundos_usuario)

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
numero_usuario = int(input("Ingrese un número: "))

def tabla_multiplicar(numero):
    for i in range(1, 11):
        multiplicacion = numero * i
        print(f"{numero} x {i} = {multiplicacion}")

tabla_multiplicar(numero_usuario)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
# restarlos, multiplicarlos y dividirlos.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b

    return suma, resta, multiplicacion, division

x, y, z, r = operaciones_basicas(10, 5)

print(f"Suma: {x}")
print(f"Resta: {y}")
print(f"Multiplicación: {z}")
print(f"División: {r}")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para 
# mostrar el resultado con dos decimales.
peso_usuario = float(input("Ingrese su peso en kg (solo números): "))
altura_usuario = float(input("Ingrese su altura en m (solo números): "))

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

calcular_imc(peso_usuario, altura_usuario)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
temperatura_c = int(input("Ingrese la temperatura en Celsius (solo números): "))

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    print(f"{celsius}°C equivalen a {fahrenheit}°F")

celsius_a_fahrenheit(temperatura_c)

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"Promedio de {a}, {b} y {c}: {promedio}")

calcular_promedio(num1, num2, num3)