

# *************************** 1. LAS LISTAS: (array, vector, arreglo)
# son colecciones ordenadas de datos, el orden es secuencial y preciso.
# Cada dato coleccionado es un elemento.
# La lista puede contener cualquier tipo de dato, incluso otras listas.
# Al elemento se accede por su posición (índice, que comienza desde 0), para:
# Obtenerlo, establecerlo, Modificarlo y Eliminarlo, entonces las listas son mutables.
# Se sabe su tamaño con la función con len(my_list).
#! Acceder a una posición fuera de rango, genera un error.


#?⭐ Creación de una lista: Se representa, conteniendo a sus elementos entre corchetes [] lista_numeros

#& 💡Utilidad de las listas: 
# Entre otras utilidades, es la forma de empaquetar un conjunto de data relacionada para, 
# por ejemplo, transportarla de un sistema a otro: https://jsonplaceholder.typicode.com/users

#?⭐ Acceso: medidante su índice (posición)


#?⭐ Modificación de un elemento


#?⭐ Saber el TDD de las Listas


#?⭐ Longitud


#?⭐ Metodo append(ele)
# Este metodo agrega el elemento paratro al final de la lista.
lista_vacia = []
# lista_vacia[0] = 'hola'  #! Esto produce IndexError: list assignment index out of range
# Esto ocurre porque la lista inicialmente no tiene elementos y no se puede asignar directamente a un índice inexistente.
# Para agregar elementos a una lista vacía debes usar métodos como:
# append() para añadir al final


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


#& 💡Utilidad de las tuplas: 
# Entre otras utilidades, es la forma de empaquetar un conjunto de data que por seguridad no deseamos que sea modificable.

#?⭐ Acceso: meidante su índice (posición)

#?⭐ ❌ NO podemos Modificar las tuplas


#?⭐ Saber el TDD de las Tuplas


#?⭐ Longitud


# *************************** METODOS CONSTRUCTORES: list(mi_iletable), tuple(mi_iterable). 
# Existen metodos constructores de listas y tuplas, cuyo parametro es el iterable a comvertir.
# 💡Utilidad: hacer casting de un tipo de dato a otro por sus caracteristicas. Ejemplo: recibes 
# una tupla pero necesitas una lista para modificar sus ele, entonces haces el casting. 
#? Ejemplo:
print('--- METODOS CONSTRUCTORES ---')



# TODO: 3. OTROS TIPOS DE COLECCIONES ITERABLES
# Existen otros tipos de colecciones en Python que también son iterables (ademas de lista, tupla), como:
# cadena de texto, diccionario, conjunto. Los veremos luego.


# TODO: El recorrido de las listas y tuplas para: 
# matepearlas y filtrarlas o extraer sus elementos se realiza con ciclos. (5_iterables_avanzado.py)
#? Explicacion de los ciclos: ir a: 3_ciclos.py
