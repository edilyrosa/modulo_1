

#& *****************************************PRIEMRO: Que es un iterable??
# Estructura que agrupa datos, identificados como elemento, los cuales puedes ser iterados o recorridos,
# uno a uno dentro de un bucle, para por ejemplo, manipularlos, filtrarlos, mapearlos. 
# Como: las listas, tuplas, cadenas de texto, diccionarios.


#& ***************************************** FOR
# Ciclo que recorre o itera sobre una iterable.
# Sintaxis: 
# for variable_elemento in iterable:
     # bloque de código usando variable_elemento lista


#? 1.⭐ Recorrer una lista con for


#? 2.⭐ Puedes establecer un condicional dentro de un bucle. if


#? 3.⭐ Sentencias de control dentro de bucles:
# Interrumpe y sale completamente del bucle, sin importar la condición del ciclo.
# y continua ejecutando la programacion principal
#? √ break 


# Salta el resto del código y pasa a la siguiente iteración.
#? √ continue 


# No hace nada, es un marcador de posición 
#? √ pass
# útil para mantener la sintaxis cuando quieres dejar código pendiente.


#& *******************WHILE
# Repite un bloque de código mientras una condición lógica sea verdadera.
# Sintaxis:
# Definicion inicial del iterador  🚩
# while condición:
#     # bloque de código a repetir
#     # actualizacion del iterador 🚩

#! 🚩🚩🚩👀🤯❌ Si no modificas una variable DENTRO del while que termina la condición,
#! puede generar un bucle infinito.



#& *******************EXISTEN OTROS METODOS CICLICOS PARA MANIPULAR ITERABLES map
#?⭐ Metodo map()
# Es una función que presenta 2 parametros 
# 1er parametro: la función que se aplica a cada elemento
# 2do parametro: iterable (lista, tupla...) de los elementos a procesar
# Rertorna: otro iterable con los elementos resultados o procesados.

#? 🤸🏻Ejercicio: Elevar al cuadrado cada elemento



#? 💡EXPLICACION DEL ANTERIOR CODIGO:
# TODO: 🔥mas adelante veremos a detalle las funciones y sus tipos, parametros y return. Pero:
# lambda es una función anónima para operaciones simples y rápidas. se define en 1 linea. Su sintaxis es:
# lambda argumentos: expresión




#? ⭐ metodo filter()
# 1er parametro: función critero para filtrar elementos, mediante condicion logica a evaluar
# 2do parametro: iterable (lista, tupla...) de los elementos a filtrar
# Rertorna: otro iterable con los elementos filtrados.
# 💡Utilidad: filtrar los items de productos excentos del pago de impuesto.




# TODO: INVESTIGA: Cliclos Anidados - Matrices, Como recorrerlas.


