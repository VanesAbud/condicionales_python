# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print("La primer palabra es mayor a la segunda")
else:
    print("La segunda palabra es mayor a la primera")

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

largo_1 = len(texto_1)
largo_2 = len(texto_2)
if largo_1 > largo_2:
    print("La primer palabra tiene mayor cantidad de letras")
elif largo_2 > largo_1:
    print("La segunda palabra tiene mayor cantidad de letras")
else:
    print("Las palabras tienen la misma cantidad de letras")
    
# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

letra_1 = texto_1[0]
letra_2 = texto_2[0]
if letra_1 > letra_2:
    print("La 1er letra de la 1er palabra es mayor a la 1er letra de la 2da")
else:
    print("La 1er letra de la 1er palabra no es mayor a la 1er letra de la 2da")


copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if copia_texto_1 == texto_1:
    print("Las variables texto y copia son iguales")
else: 
    print("Las variables texto y copia son diferentes")

