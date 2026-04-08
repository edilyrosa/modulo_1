#& *************************************Tipo de dato SET
# Es una colección *desordenada* de elementos **únicos**.
# Es mutable (puedes añadir/quitar elementos) pero los elementos deben ser 
# hashables (no cambia mientras exista, son inmutable → int, str, tuple).
# (por ejemplo: números, strings, tuplas; NO listas ni diccionarios).
# Se crean entre corchetes {} o con el constructor.

#? ⭐ Creación:
s = {1, 2, 3}               # literal
s = set([1, 2, 3, 3])       # desde iterable (los duplicados se eliminan)
s = set(range(5))           # desde cualquier iterable

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
s1 = {1, 2, 2, 3}
s2 = set([3, 4, 5])
print('💡Set (duplicados eliminados):', s1)

print('UNION DE SETS')
union = s1 | s2
union_metodo = s1.union(s2)
print('💡s1 union s2:', union) # {1, 2, 3, 4, 5}
print('💡s1 union s2 con metodo:', union)

print('INTERSECION DE SETS')
intersection = s1 & s2
intersecion_metodo = s1.intersection(s2)
print('💡s1 interseccion s2:', intersection) # {3}
print('💡s1 interseccion s2 con metodo:', intersecion_metodo)

print('DIFERENCIA DE SETS')
diferencia = s1 - s2
difencia_metodo = s1.difference(s2)
print('💡s1 diferencia s2:', diferencia) # {1, 2}
print('💡s1 diferencia s2:', difencia_metodo)
