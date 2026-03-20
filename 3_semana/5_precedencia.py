
#* Reglas de la Precedencia:
# 1. ()
# 2. Exponentes: veces que el la base se multiplica por si misma
# 3. *, /, //, %
# 4. +, -
# 5. Op. Comparacion <, <=, >, >=
# 6. Op. Igualdad ==, !==
# 7. Op. Logicos: NOT → AND → OR
# Paréntesis siempre alteran el orden natural, resolviendo primero lo que está dentro.
# REGLA: Si hay varios operadores del mismo nivel, se resuelven de izquierda a derecha.
# 💡Excepción: la potenciación se evalúa de derecha a izquierda. Recomendación: Usa paréntesis para dejar explícito el orden.
# Esta jerarquía se aplica tanto en matemáticas como en la mayoría de lenguajes de programación

#* mira la diferencia al usar ()
print( (2 + 2) * 10** 2 / 5) # 80.0
print( 400 / 5) # 80.0

print( 2 + 2 * 10** 2 / 5) #42.0
print( 2 + 40) #42.0