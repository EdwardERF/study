# uno de los primeros algoritmos que se deben tratar a la hora de solucionar problemas
# 'adivina y verifica'
# no es el algoritmo más eficiente, pero es muy eficaz, y las computadoras de hoy en día son muy potentes, que no es complicación utilizarlo.

def enumeracion_exhaustiva(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raíz cuadrada exacta')