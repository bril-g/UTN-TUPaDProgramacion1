# Ejercicio 1: Factorial
n = int(input("Ingrese un número: "))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
    
print(factorial(n)) 

# Ejercicio 2: Serie de Fibonacci
n = int(input("Ingrese un número como posición: "))

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(n))

# Ejercicio 3: Potencia
def potencia(n, m):
    if m == 0:
        return 1
    return n * potencia(n, m - 1)

print(potencia(10, 2))

# Ejercicio 4: Binario
n = int(input("Ingrese un número entero positivo: "))

def a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return a_binario(n // 2) + str(n % 2)   

print(a_binario(n))

# Ejercicio 5: Palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

print(es_palindromo("neuquen"))

# Ejercicio 6: Suma de dígitos
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

print(suma_digitos(1234))

# Ejercicio 7: Contar bloques
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

print(contar_bloques(4))

# Ejercicio 8: Contar dígitos
def contar_digito(numero, digito):
    if numero < 10:
        if numero == digito:
            return 1
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    return contar_digito(numero // 10, digito)

print(contar_digito(12233421, 2))

