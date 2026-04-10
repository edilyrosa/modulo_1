#& *************************************Tipo de dato SET
# Es una colección *desordenada* de elementos **únicos**.
# Es mutable (puedes añadir/quitar elementos) pero los elementos deben ser 
# hashables (no cambia mientras exista, son inmutable → int, str, tuple).
# (por ejemplo: números, strings, tuplas; NO listas ni diccionarios).
# Se crean entre corchetes {} o con el constructor.

#? ⭐ Creación:
set1 = {1, 2, 3, 3}               # literal
set2 = set([1, 2, 3, 3, 5, 5, 5])       # desde iterable (los duplicados se eliminan)
set3 = set(range(5))           # desde cualquier iterable

print(type(set1))
print(set2)
print(set3) #{ 0, 1, 2, 3, 4}

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

#? ejemplos
s1 = {1, 2, 2, 3}
s2 = set([3, 4, 5])
# union
union = s1 | s2
union2 = s1.union(s2) #{1, 2, 3, 4, 5}
print(union)
print(union2)

intersec = s1 & s2
intersec2 = s1.intersection(s2)
print(intersec)
print(intersec2) #{3}

dif = s1 - s2
dif2 = s1.difference(s2)
print(dif)
print(dif2) #{1,2}

s1.add(8) 
print(s1) #{8, 1, 2, 3}