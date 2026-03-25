
#?⭐ ya sabemos recorrer, filtrar y mapear los iterables con los ciclos.

#? ⭐ Operador "in" 
#& 💡Recorrer iterables con Operador "in" 

    
#& 💡Tmabien podemos saber si un elemento existe en el iterable con Operador "in"



#?⭐⭐⭐ Lista compacta: 
# Forma resumida de crear una lista, es muy utilizadas profesionalmente, acostumbrate a esta sintaxis
# EJEMPLO: Vamos a crear una lista compacta con elementos que NO son múltiplos de 2


    
#? ⭐ Desempaquetamiento de los iterables




#& *************************************Tipo de dato SET
# Es una colección *desordenada* de elementos **únicos**.
# Es mutable (puedes añadir/quitar elementos) pero los elementos deben ser 
# hashables (no cambia mientras exista, son inmutable → int, str, tuple).
# (por ejemplo: números, strings, tuplas; NO listas ni diccionarios).
# Se crean entre corchetes {} o con el constructor.

#? ⭐ Creación:


#? ⭐ Propiedades y operaciones comunes:
#   - Añadir: s.add(x)
#   - Quitar: s.remove(x)       # lanza KeyError si x no existe
#             s.discard(x)      # no lanza si x no existe
#   - Extraer arbitrario: s.pop() # como están desordenados, devuelve cualquier elemento
#   - Limpiar: s.clear()
#   - Unión: s | t     (o s.union(t))
#   - Intersección: s & t  (o s.intersection(t))
#   - Diferencia: s - t  (o s.difference(t))
#   - Diferencia simétrica: s ^ t (o s.symmetric_difference(t))
#   - Subconjunto/sobconjunto: s.issubset(t), s.issuperset(t)
#   - Disjuntos: s.isdisjoint(t)

#? Ejemplos:




#TODO: INVESTIGA: Slicing de los iterables: para extraer (retornando) todo o parte de sus elementos.
# mi_lista[inicio: fin: paso] 
# 1. inicio: índice desde donde comienza el corte.
# Incluye el elemento en esta posición, Si se omite es indice 0.
# Puede ser negativo, contando desde el final (-1 es el último elemento).
# 2. fin: índice donde termina el corte. 
# Excluye el elemento en esta posición, Si se omite va hasta el final.
# También puede ser negativo para contar desde el final (-1 es el último elemento).
# 3. paso: Indica de cuánto en cuánto se avanza para tomar elementos.
# Por defecto es 1 → Toman elementos consecutivos de inicio a fin, -1 los toma a la inversa.
# No puede ser 0 (causa Error). 

# [1,2,3,4, 5, 77, 100] → 2 a 5
# [1,2,3,4, 5, 77, 100] → 0 a 3
# [1,2,3,4, 5, 77, 100] → 0 a 3 de 2 en 2