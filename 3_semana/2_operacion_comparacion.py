
# ***************Los operadores de Comparación en Python: ==, !=, <, >, <=, >=
# permiten "comparar dos" valores o expresiones y devuelven un bool.
# Usados para tomar decisiones en un programa, como estructuras condicionales (if, while, etc.).
# 💡Ejemplo: que hago si edad ingesada de usuario es menor de 18 años?

# + - * ** / // %
#  += -+ *= **= /= //= %=
#& == != >= <= <, >,

#*************⁉️¿Con tipo de dato numéricos?
# Es intuitivo, comparan sus valores numéricos naturalmente.
print(5 == 5)   #T
print(5 == 3)   #F
print(5 >= 3)   #T
print(5 >= 5)   #T
print(5 > 5)    #F
print(5 == "5") #F
print(5 != "5") #T
# print(5 > "5") #!TypeError: '>' not supported between instances of 'int' and 'str'

#*************⁉️¿Con tipo de dato Bool?
# Se tratan como 1 (True) y 0 (False).
print(True > False) #T


# *************⁉️💡¿Con tipo de dato String?
# ✅Se comparan lexicográficamente según el orden Unicode de cada carácter.
# Python compara cadenas carácter a carácter, cada caracter tiene un codigo numerico. 
print('Hola' == 'hola') #F
print('hola' == 'hola') #T
print('h es = ',  ord('h')) # 104
print('H es = ',  ord('H')) # 72
print('que es? ', 'H' ==  72) # F
print('que es? ', ord('H') ==  72) # F
print('Hola' != 'hola') #F
print('H' < 'h') #T


#* Python compara carácter a carácter:
# usando el valor numérico Unicode de cada carácter (obtenible con ord(caracter)).
 

#*✅ La comparación se realiza en orden: 
# se compara el primer carácter de ambas cadenas; si son iguales, se pasa al siguiente, 
# y así sucesivamente, hasta encontrar la diferencia que devuelva el booleano resultado.


#* ✅Puedes usar los operadores de comparacion "entre dos cadenas".
#! 🚫No mezcles tipos diferentes, como str con int en comparaciones directas, porque no son compatibles, 
# si lo intentas usando operadores de orden (<, >, etc.), Python lanzará un TypeError. 


#* ®️💡Resumen clave
# 👀Los operadores de comparación devuelven True o False.
# 👀Debes comparar preferentemente valores del mismo tipo para evitar errores.
# 👀Para cadenas, la comparación es lexicográfica, sensible a mayúsculas y minúsculas.
# 👀En tipos numéricos, se comportan naturalmente según valor.
# 👀== y != pueden comparar distintos tipos pero otros operadores NO.




# comparacion de 2 cadenas que obtenemos por input, 
# necesitamos saber si son iguales y no debes distinguir entre m y n
print('COMPARANDO CADENAS')
palabra_1 = input('Ingrese palabra 1 a comprara: ').strip().lower()
palabra_2 = input('Ingrese palabra 2 a comprara: ').strip().lower()

if palabra_1 == palabra_2:
    print('PALABRAS SON IGUALES ✅')
else: 
    print('PALABRAS SON DIFERENTES ❌')

# nombre  =  'EDILY'
# print(nombre)
# print(nombre.lower())
# nombre_1 = '     edily    '
# print(nombre_1)
# print(nombre_1.strip())


#TODO: 4_op_logicos.py + ejercicio