# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("¡Hola, mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
nombre = input("Ingrese su nombre: ").title()

print(f"¡Hola, {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
nombre = input("Ingrese su nombre: ").title()
apellido = input("Ingrese su apellido: ").title()
edad = int(input("Ingrese su edad (solo números): "))
lugar_residencia = input("Ingrese su lugar de residencia: ").title()

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
import math

radio = float(input("Ingrese el radio de un círculo: "))

area = math.pi * radio**2
perimetro = 2 * math.pi * radio

print(f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int(input("Ingrese una cantidad entera de segundos: "))

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas} horas, {minutos} minutos y {segundos} segundos.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero = int(input("Ingrese un número: "))

print(f"{numero} x 1: {numero * 1}")
print(f"{numero} x 2: {numero * 2}")
print(f"{numero} x 3: {numero * 3}")
print(f"{numero} x 4: {numero * 4}")
print(f"{numero} x 5: {numero * 5}")
print(f"{numero} x 6: {numero * 6}")
print(f"{numero} x 7: {numero * 7}")
print(f"{numero} x 8: {numero * 8}")
print(f"{numero} x 9: {numero * 9}")
print(f"{numero} x 10: {numero * 10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1 = int(input("Ingrese un número entero distinto de 0: "))
numero2 = int(input("Ingrese otro número entero distinto de 0: "))

if numero1 != 0 and numero2 != 0:
    print(f"Suma: {numero1 + numero2} ")
    print(f"Resta: {numero1 - numero2} ")
    print(f"Multiplicación: {numero1 * numero2} ")
    print(f"División: {numero1 / numero2} ")

else:
    print("No ingresó un número entero distinto de 0.")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

imc = peso / altura**2

print(f"Índice de masa corporal: {imc:.2f}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 
temperatura_celcius = int(input("Ingrese una temperatura en grados Celsius (solo números): "))

print(f"Temperatura en Fahrenheit: {9/5 * temperatura_celcius + 32}")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))
numero3 = int(input("Ingrese otro número: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"Promedio: {promedio:.2f}")