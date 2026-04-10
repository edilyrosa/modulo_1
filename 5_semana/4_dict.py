
#************************** LOS TIPO DE DATO DICT (diccionarios).
# son pares 'key':value, la key puede ser TDD inmutables: str, int, bool, tuple
personaje = {
    'id': 1,
    'nombre': 'Mujer Maravilla',
    'edad': 30,
    'edad': 20,
    'peso': 50.5,
    'poderes': ['programar', 'fuerza', 'volar'],
    'hobbies': ('Salvar el mundo', 'criar ganado', 'leer'),
    2:'dos',
    False:'falso',
    ('nota', 'materia'): ['20', 'math'],
    #[1, 2, 3]: 'lista' #! TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
}
# persona= {1, 3}
# edad = 30
# edad = 'treinta'
# print(edad)
#? ⭐ Acceso a sus valores, mediante sus claves o keys
print(personaje['id'])      # 1
print(personaje['nombre'])  # 'Mujer Maravilla'
print(personaje['poderes']) #['programar', 'fuerza', 'volar']
print(personaje['poderes'][-1]) # 'volar'
print(personaje['hobbies'][0]) #Salvar el mundo
print(personaje[2]) #Salvar el mundo
print(personaje[False]) #Salvar el mundo
print(personaje[('nota', 'materia')]) #['20', 'math']
print(personaje[('nota', 'materia')][-1]) #'math'
#!print(persona[1, 2, 3]) #1
#print(persona[id]) #!KeyError: <built-in function id>

#? sabemos tu tipo
print(type(personaje)) #<class 'dict'>
print(type(personaje[False])) #<class 'str'>


#? ⭐ Metodos mas importantes
print(personaje.keys()) # dict_keys(['id', 'nombre', 'edad', 'peso', 'poderes', 'hobbies', 2, False, ('nota', 'materia')])
print(personaje.values()) # dict_values([1, 'Mujer Maravilla', 30, 50.5, ['programar', 'fuerza', 'volar'], ('Salvar el mundo', 'criar ganado', 'leer'), 'dos', 'falso', ['20', 'math']])
print(personaje.items()) # dict_items([('id', 1), ('nombre', 'Mujer Maravilla'), ('edad', 30), ('peso', 50.5), ('poderes', ['programar', 'fuerza', 'volar']), ('hobbies', ('Salvar el mundo', 'criar ganado', 'leer')), (2, 'dos'), (False, 'falso'), (('nota', 'materia'), ['20', 'math'])])


#? ⭐ Se accede a los values a traves de la key y get()
#print(personaje['nacionalidad']) #! KeyError: 'nacionalidad'
print(personaje.get('edad')) #None
print(personaje.get('nacionalidad')) #None
print(personaje.get('nacionalidad', 'Este key no existe')) #Este key no existe


#? ⭐ Se recorre los values a traves de la key y get(), con for
for key in personaje:
    # print(key, '-', personaje[key]) 
    print(key, '-', personaje.get(key)) 

for v, k in personaje.items(): # [(k:v), (k:v), ()]
    print(k, '---', v)
    
    
for v in personaje.values(): #
    print(v)
    
    
for clave in personaje.keys(): # 
    print(clave)

    
#? ⭐ modificar el valor de una key
print('AQUIIIIIIIIIIIIIIIII', personaje['edad'])
personaje['edad'] = 31
print('AQUIIIIIIIIIIIIIIIII', personaje['edad'])
print(personaje)

#? ⭐ agregar una nueva key al dict
personaje['nacionalidad'] = 'Amazonica'
print(personaje)


#? ⭐ eliminar key/value y vaciarlo
personaje.pop('peso') # elimina la key 'peso' y su valor
personaje.popitem()
personaje.clear()
print(personaje)


#? ⭐ Dict compacto
# Crear nuevo diccionario con elementos cuyo valor sea mayor a 5
dict_original = {
    'a': 1, 
    'b': 6, 
    'c': 3, 
    'd': 8
}

dict_filtrado = {p:j for p,j in dict_original.items() if j > 3 }
# mi_lista = [e for e in [1, 2, 4] if e > 2 ]
# mi_lista = tuple(e for e in [1, 2, 4] if e > 2 )
print(dict_filtrado)




# #TODO: ⛹🏽‍♂️⛹🏽‍♀️💡EJERCICIO PROPUESTO PARA CASA: mapeando un dict para encontra TDD num y aplicar descuento.💡⛹🏽‍♂️⛹🏽‍♀️
persona_ejercicio = {
    'nombre': 'Ana',
    'femenina': True,
    102: 100,
    'hobbies': ['leer', 'viajar', 'codear'],
    'contacto': {
        'email': 'ana@ejemplo.com',
        'telefono': '555-1234'
    },
    ('latitud', 'longitud'): [40.7128, -74.006],
    (1, 2, 3): [10, 20, 30]
}
# # Instrucciones:
# # Recorre el diccionario dict _ejercicio con un ciclo for.
# # Para cada elemento, verifica si el valor asociado es un número (ya sea entero o decimal).
# # Usa la función: isinstance(valor, (int, float)) para hacer esta comprobación.
# # ⭐isinstance(valor, (int, float)) -> verifica si valor es un de tipo int o float. Retorna bool.
# # Si el valor es numérico, calcula y aplica un descuento del 20% a ese valor.
# # Por cada valor numérico modificado, imprime un mensaje en el siguiente formato:
# # La clave es "clave", se le aplica un descuento del 20% a su valor original VALOR_ORIGINAL,
# # resultando en VALOR_CON_DESCUENTO.

print(isinstance('edily', str))
print(isinstance(100, str))
print(isinstance(100, (int, float)))




# TODO: PROXIMO: 
    #? FUNCIONES en: funciones.py