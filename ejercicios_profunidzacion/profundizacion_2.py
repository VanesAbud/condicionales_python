# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

print("Por favor ingrese un numero")
numero_1 = int(input())

print("Ingrese otro numero")
numero_2 = int(input())

print("Ingrese un numero más")
numero_3 = int(input())

resultado_1 = numero_1 % 2 

if resultado_1 == 0:
    print("El primer numero es par")
else:
    print("El primer numero es impar")

resultado_2 = numero_2 % 2 

if resultado_2 == 0:
    print("El segundo numero es par")
else:
    print("El segundo numero es impar")

resultado_3 = numero_3 % 2 

if resultado_3 == 0:
    print("El tercer numero es par")
else:
    print("El tercer numero es impar")   

# Aplicando bucle sería más simple el programa,
# pero ya vi que es para la proxima clase 