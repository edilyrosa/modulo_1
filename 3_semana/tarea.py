print('verificacion de que usuario puede conducir')

tiene_licencia = input('tiene licencia? (si/no): ') == "si"
edad = int(input('ingrese su edad: '))
emancipado = input('está emancipado? (si/no): ') == "si"

if tiene_licencia and (edad >= 18 or emancipado):
    print('puede conducir')
else:
    print('no puede conducir')