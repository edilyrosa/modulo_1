
#& *****************************************PRIEMRO: Que es un iterable??
# Estructura que agrupa datos (elemento) los cuales puedes ser iterados o recorridos,
# uno a uno dentro de un bucle, para por ejemplo, manipularlos, filtrarlos, mapearlos. 
# Como: las listas, tuplas, cadenas de texto, diccionarios.


#& ***************************************** CICLO FOR
# Ciclo que recorre o itera sobre una iterable.
# Sintaxis: 
# for variable_elemento in iterable:
     # bloque de código usando variable_elemento
lista = [1, 2, 3, 4, 5, True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

#? 1.⭐ Recorrer un itelable (TDD List) con for
print('Con for')
for elemento in lista:
     print(f'el elemento es {elemento}')
     
print('Con for modificando')
for elemento in lista:
     print(f'Eleva {elemento**2}')


lista_2 = lista

print('la lista dos ', lista_2)

#[1, 2, 3, 4, 5, True]
lista_copia = []
print(lista_copia)

for ele in lista:
     lista_copia.append(ele**3)
print(lista_copia) #[1, 8, 27, 64, 125, 1]


# 💡Nota: En Python NO se crea un nuevo ámbito con los bloques for, while, if, etc. 
# Solo se crean ámbitos nuevos en funciones, clases y módulos.
print('ultimo valor de ele', ele)

#? 2.⭐ Puedes establecer un condicional dentro de un bucle. if
#[1, 2, 3, 4, 5, True]
for ele in lista:
     if(ele % 2 == 0 ):
          print(f'Dentro de la lista, los siguientes elementos son pares {ele}')

print('🚩Bandera de salir de las estructuras del control del flujo')

#? 3.⭐ Sentencias de control dentro de bucles:
# Interrumpe y sale completamente del bucle, sin importar la condición del ciclo.
# y continua ejecutando la programacion principal
#? √ break 
for e in lista: ##[1, 2, 3, 4, 5, True]
     if e == 3:
          break
     print('Se imprimira hasta el ele num 2}')

# Salta el resto del código y pasa a la siguiente iteración.
#? √ continue 
for e in lista: ##[1, 2, 3, 4, 5, True]
     if e == 3:
          continue
     print(f'Se imprimira los elementos {e}')

# No hace nada, es un marcador de posición 
#? √ pass
for e in lista:
    pass # todo if e == 3:
# útil para mantener la sintaxis cuando quieres dejar código pendiente.


#& *******************WHILE
# Repite un bloque de código mientras una condición lógica sea verdadera.
# Sintaxis:
# Definicion inicial del iterador  🚩
# while condición:
#     # bloque de código a repetir
#     # actualizacion del iterador 🚩

#! 🚩🚩🚩👀🤯❌ Si no modificas la variable iterador DENTRO del while que termina la condición,
#! puede generar un bucle infinito.

i = 1
while i < 10:
     print(f'Valor de i = {i}')
     i+=1

# todo: ⭐💡TAREA:
# Genere y muestre la tabla de multiplicar del número especificado por usuario. 
# El programa debe pedirle al usuario con input() que ingrese un número entero y luego, 
# utilizando un bucle while, debe imprimir la tabla de multiplicar de ese número del 1 al 10.

# num = int(input('Ingresa el num entero para imprimir su tabla'))
# i = 0 
# while i<=10:
#      print(f'{i} X {num} = {i*num}') #→ 1*10
#      # print(f'{i} X {num} = {i*num}') #→ 2*10
#      # print(f'{i} X {num} = {i*num}') #→ 3*10
#      i +=2
     



#& *******************EXISTEN OTROS METODOS CICLICOS PARA MANIPULAR ITERABLES map
#?⭐ Metodo map(func, iterable)
# Es una función que presenta 2 parametros 
# 1er parametro: la función que se aplica a cada elemento
# 2do parametro: iterable (lista, tupla...) de los elementos a procesar
# Rertorna: otro iterable con los elementos resultados o procesados.

#? 🤸🏻Ejercicio: Elevar al cuadrado cada elemento
nums = [1, 2, 3, 4]

cuadrados = list(map(lambda x: x**2, nums))
print('Map() de cuadrados', cuadrados)

def eleva(x):
 return x**2
cuadrados_funcion = tuple(map(eleva, nums))
print('Map() de cuadrados con funcion', cuadrados_funcion)

#? 💡EXPLICACION DEL ANTERIOR CODIGO:
# TODO: 🔥mas adelante veremos a detalle las funciones y sus tipos, parametros y return. Pero:
# lambda es una función anónima para operaciones simples y rápidas. se define en 1 linea. Su sintaxis es:
# lambda argumentos: expresión




#? ⭐ metodo filter()
# 1er parametro: función critero para filtrar elementos, mediante condicion logica a evaluar
# 2do parametro: iterable (lista, tupla...) de los elementos a filtrar
# Rertorna: otro iterable con los elementos filtrados.
# 💡Utilidad: filtrar los items de productos excentos del pago de impuesto.

pares = list(filter(lambda x: x % 2 == 0, nums))
print('Filtrado de los pares', pares)

# TODO: INVESTIGA: Cliclos Anidados - Matrices, Como recorrerlas.

matriz = [
     [1, 0, 0],
     [0, 1, 0],
     [0, 0, 1],
]

print(matriz[0][0])
print(matriz[1][1])
print(matriz[2][2])


lista_num = [1, 3, 5, 'Edily']
print('Edily' in lista_num)