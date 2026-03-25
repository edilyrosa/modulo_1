

# *************************** 1. LAS LISTAS: (array, vector, arreglo)
# son colecciones ordenadas de datos, el orden es secuencial y preciso.
# Cada dato coleccionado es un elemento.
# La lista puede contener cualquier tipo de dato, incluso otras listas.
# Al elemento se accede por su posición (índice, que comienza desde 0), para:
# Obtenerlo, establecerlo, Modificarlo y Eliminarlo, entonces las listas son mutables.
# Se sabe su tamaño con la función con len(my_list).
#! Acceder a una posición fuera de rango, genera un error.


#?⭐ Creación de una lista: Se representa, conteniendo a sus elementos entre corchetes [] lista_numeros
lista_numeros = [1, 2, 3, 4, '5', False]
print(lista_numeros)

sabores = ['mantecado', 'chocolate', 'fresa']


#& 💡Utilidad de las listas: 
# Entre otras utilidades, es la forma de empaquetar un conjunto de data relacionada para, 
# por ejemplo, transportarla de un sistema a otro: https://jsonplaceholder.typicode.com/users

#?⭐ Acceso: medidante su índice (posición)

print('Primera pos', lista_numeros[0])
print('Pos del "5"', lista_numeros[-2])
print('Pos del False', lista_numeros[5])
print('Pos del False', lista_numeros[-1])

#?⭐ Modificación de un elemento
# lista_numeros = [1, 2, 3, 4, '5', False]
print(type(lista_numeros[-2])) #<class 'str'>
lista_numeros[-2] = 5
print(lista_numeros)

#?⭐ Saber el TDD de las Listas
print(type(lista_numeros)) # <class 'list'>
print(type(lista_numeros[-2])) #<class 'int'>

#?⭐ Longitud
# lista_numeros = [1, 2, 3, 4, 5, False]
print(len(lista_numeros)) #6

#?⭐ Metodo append(ele)
# Este metodo agrega el elemento parametro al final de la lista.
lista_vacia = []
print(lista_vacia)
# lista_vacia[0] = 'hola' #! Esto produce IndexError: list assignment index out of range
# Esto ocurre porque la lista inicialmente no tiene elementos y no se puede asignar directamente a un índice inexistente.
# ⭐ Para agregar elementos a una lista vacía debes usar métodos como:
# append() para añadir al final
lista_vacia.append('hola')
lista_vacia.append(2)
print(lista_vacia.append('3')) # None
lista_vacia.append('3') # None
lista_vacia.append('3') # None
# 'Edily'.upper()

print(lista_vacia)
ele_borrado = lista_vacia.pop()
# print(lista_vacia.pop()) # '3'
print(ele_borrado) # '3'
print(lista_vacia) #['hola', 2, '3', '3']
lista_vacia.remove('hola') 
print(lista_vacia) #[2, '3', '3']
lista_vacia.pop(0) # es = a lista_vacia.pop(-3)
print(lista_vacia) #['3', '3']

print(lista_numeros.sort())
print(lista_numeros.sort(reverse=True))
print(lista_numeros)
print(lista_numeros) #[5, 4, 3, 2, 1, False]
print(lista_numeros.index(False))


#TODO: 🧠TAREA:Existen otros metodos de las listas, te invito a que los investigues y pruebes. Los usaremos mas adelante.
"""
TABLA DE MÉTODOS IMPORTANTES DE LISTAS EN PYTHON
| Método    | Parámetros                         | Retorna                         | Descripción / Señal de uso                  |
|-----------|------------------------------------|---------------------------------|---------------------------------------------|
| append()  | obj (cualquier objeto)             | None (modifica lista in-place)  | Añade elemento al final: lista.append(x)    |
| pop()     | index=-1 (opcional, índice)        | Elemento removido               | Elimina y retorna elemento: lista.pop([i])  |
| remove()  | obj (elemento a eliminar)          | None (modifica lista in-place)  | Elimina primera ocurrencia: lista.remove(x) |
| sort()    | key=None, reverse=False (opc.)     | None (modifica lista in-place)  | Ordena lista: lista.sort() o sort(reverse)  |
| index()   | obj, start=0, end=len(lista) (opc.)| Índice de primera ocurrencia    | Busca posición: lista.index(x[,start,end])  |

Ejemplos rápidos:

"""
# *************************** 2. TUPLAS: (tuple)
# Son colecciones ordenadas de datos, el orden es secuencial y preciso.
# Cada dato coleccionado es un elemento.
# A diferencia de las listas, las tuplas son inmutables, no se pueden modificar, agregar o eliminar elementos.
# Se sabe su tamaño con la función con len(my_tuple).
#! Acceder a una posición fuera de rango, genera un error.

#?⭐ Creación de una tupla: Se representa, conteniendo a sus elementos entre paréntesis ()
tupla_numeros = (1, 2, 3, 4, '5', False)
tupla_numeros = 1, 2, 3, 4, '5', False
tupla_numeros = 1, 2, 3, 4, [100, 101]

#?⭐ Saber el TDD de las Tuplas
print(type(tupla_numeros)) # <class 'tuple'>
print(tupla_numeros)       # (1, 2, 3, 4, [100, 101])

#?⭐ Acceso: meidante su índice (posición)
print(tupla_numeros[0])       # 1
print(tupla_numeros[-1])      # 1
print(tupla_numeros[4])       # 1
print(tupla_numeros[4][0])    # 100

que_soy = tupla_numeros[4]

print(que_soy)

#?⭐ ❌ NO podemos Modificar las tuplas
# tupla_numeros[4] = 500 #!TypeError: 'tuple' object does not support item assignment

#?⭐ Longitud
print(len(tupla_numeros))

#& 💡Utilidad de las tuplas: 
# Entre otras utilidades, es la forma de empaquetar un conjunto de data que por seguridad no deseamos que sea modificable.









# *************************** METODOS CONSTRUCTORES: list(mi_iletable), tuple(mi_iterable). 
# Existen metodos constructores de listas y tuplas, cuyo parametro es el iterable a comvertir.
# 💡Utilidad: hacer casting de un tipo de dato a otro por sus caracteristicas. Ejemplo: recibes 
# una tupla pero necesitas una lista para modificar sus ele, entonces haces el casting. 
#? Ejemplo:
print('--- METODOS CONSTRUCTORES ---')
lista_de_tupla = list(tupla_numeros)
print(tupla_numeros)
print(lista_de_tupla)

mi_lista = [True, False, 'hola']
mi_tupla_lita = tuple(mi_lista)
print(mi_tupla_lita)

# TODO: 3. OTROS TIPOS DE COLECCIONES ITERABLES
# Existen otros tipos de colecciones en Python que también son iterables (ademas de lista, tupla), como:
# cadena de texto (str), diccionario, conjunto. Los veremos luego.
list()
nombre = 'Edily'
lista_nom = list(nombre)
print(lista_nom)

str_fotos = 'https//..., htt...., '.join(', ') == ['https...', 'http..']
lista_fotos = []
if len(lista_fotos) == 0:
    print('No hay fotos que mirar')
else:
    print('Recorremos las fotos de la BBDD')
    
    

# TODO: El recorrido de las listas y tuplas para: 
# matepearlas y filtrarlas o extraer sus elementos se realiza con ciclos. (5_iterables_avanzado.py)
#? Explicacion de los ciclos: ir a: 3_ciclos.py
