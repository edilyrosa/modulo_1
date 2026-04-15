#
# *split()
#Tipo de dato: cadena (str)
#Qué hace: Divide una cadena en una lista, usando un separador (por defecto es el espacio).
#?Ejemplo:
texto = "hola mundo python"
lista = texto.split()
print(lista)
 

#*join()
#Tipo de dato: cadena (str)
#Qué hace: Une los elementos de una lista en una sola cadena, usando un separador.
#?Ejemplo:
lista = ["hola", "mundo", "python"]
texto = " ".join(lista)
print(texto)

#*max()
#Tipo de dato: listas, tuplas, cadenas, etc.
#Qué hace: Devuelve el valor máximo de un conjunto de datos.
#?Ejemplo:
numeros = [3, 7, 2, 9]
print(max(numeros))


# *min()
#Tipo de dato: listas, tuplas, cadenas, etc.
#Qué hace: Devuelve el valor mínimo de un conjunto de datos.
#?Ejemplo:
numeros = [3, 7, 2, 9]
print(min(numeros))


#*extend()
#Tipo de dato: lista (list)
#Qué hace: Agrega varios elementos a una lista (desde otra lista o iterable).
#?Ejemplo:
lista1 = [1, 2, 3]
lista2 = [4, 5]

lista1.extend(lista2)
print(lista1)

#*count()
#Tipo de dato: listas y cadenas
#Qué hace: Cuenta cuántas veces aparece un elemento.
#?Ejemplo:
numeros = [1, 2, 2, 3, 2]
print(numeros.count(2))