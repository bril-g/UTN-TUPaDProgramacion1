# 1) Programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), 
# en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)

# 2) Programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
numero = int(input("Ingrese un número entero: "))

if numero == 0:
    contador = 1
else:
    contador = 0

    while numero > 0:
        contador += 1
        numero //= 10

print("El número tiene", contador, "dígitos.")

# 3) Programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
inicio = int(input("Ingresa un número entero: "))
fin = int(input("Ingresa otro número entero: "))

suma = 0
numero = inicio + 1

while numero < fin:
    suma += numero
    numero += 1

print("La suma es:", suma)

# 4) Programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
numero = int(input("Ingrese un número entero: "))

suma = 0

while numero != 0:
    numero = int(input("Ingrese otro número entero: "))
    suma += numero

print("La suma es:", suma)

# 5) Juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

numero_random = random.randint(0, 9)
intentos = 0

numero = int(input("Adivina el número entre 0 y 9: "))
intentos += 1

while numero != numero_random:
    numero = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1

print(f"Acertaste. Cantidad de intentos: {intentos}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for i in range(0, 101, -2):
    print(i)