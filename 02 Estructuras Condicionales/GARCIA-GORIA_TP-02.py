# Edad del usuario:
edad = int(input("Ingresa tu edad (solo números): "))

if edad >= 18:
    print("Eres mayor de edad.")
else: 
    print("Eres menor de edad.")

# Nota del usuario:
nota = float(input("Nota del exámen: "))

if nota < 0 or nota > 10:
    print("Nota inválida.")
elif nota >= 6:
    print("Aprobado.")
else: 
    print("Desaprobado.")

# Números pares:
numero = int(input("Ingresa un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

# Categoria de edad del usuario:
edad = int(input("Ingresa tu edad (solo números): "))

if edad < 12:
    print("Niño/a.")
elif 12 <= edad < 18:
    print("Adolescente.")
elif 18 <= edad < 30:
    print("Adulto/a joven.")
else:
    print("Adulto/a.")

# Contraseñas de entre 8 y 14 caracteres:
contraseña = input("Ingresa tu contraseña (8-14 caracteres): ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")
else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

# Lista con 50 números entre 1 y 100 elegidos de forma aleatoria.
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range (50)]

print("Números aleatorios:", numeros_aleatorios)

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana and mediana > moda:
    print("Sesgo positivo.")
elif media < mediana and mediana < moda:
    print("Sesgo negativo.")
elif media == mediana == moda:
    print("Sin sesgo.")
else:
    print("No se puede determinar el sesgo con este criterio.")

# Frase o palabra del usuario:
frase = input("Ingresa una frase o palabra: ").strip()

if len(frase) == 0:
    print("Entrada vacía")
else:
    ultima = frase[-1].lower()

    if ultima in "aeiou":
        print(frase + "!")
    else:
        print(frase)

# Nombre y número: 
nombre = input("Ingresa tu nombre: ")
print("1: Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2: Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3: Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
numero = int(input("Elige una opción: "))

if numero == 1:
    print(nombre.upper())
elif numero == 2: 
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())
else:
    print("Opción inválida.")

# Magnitud de un terremoto.
magnitud = float(input("Magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
elif 7 <= magnitud <= 10:
    print("Extremo (puede causar graves daños a gran escala).")
else:
    print("Improbable.")

# Hemisferio norte y sur:
hemisferio = input("Hemisferio (Norte/Sur): ").lower()
mes = int(input("Mes (1-12): "))
dia = int(input("Día (número): "))

if (mes < 3) or (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20):
    estacion = "Invierno"
elif (mes > 3 and mes < 6) or (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20):
    estacion = "Primavera"
elif (mes > 6 and mes < 9) or (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
    estacion = "Verano"
elif (mes > 9 and mes < 12) or (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20):
    estacion = "Otoño"

if hemisferio == "sur":
    if estacion == "Primavera":
        estacion = "Otoño"
    elif estacion == "Verano":
        estacion = "Invierno"
    elif estacion == "Otoño":
        estacion = "Primavera"
    elif estacion == "Invierno":
        estacion = "Verano"

print("Estación:", estacion)