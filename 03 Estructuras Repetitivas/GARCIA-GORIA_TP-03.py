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

# 6) Programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for i in range(100, -1, -2):
    print(i)

# 7) Programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
numero = int(input("Ingresa un número entero positivo: "))

suma = 0

for i in range(0, numero + 1):
    suma += i

print(f"La suma es: {suma}")

# 8) Programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, 
# cuántos son negativos y cuántos son positivos. 
pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range(100):
    numero = int(input("Ingrese un número: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

# 9) Programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.
suma = 0

for i in range(100):
    numero = int(input("Ingrese un número entero: "))
    suma += numero

media = suma / 100
print(f"Media: {media}")

# 10) Programa que invierta el orden de los dígitos de un número ingresado por el usuario.
numero = int(input("Ingrese un número positivo: "))

invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

print(f"Número invertido: {invertido}")

