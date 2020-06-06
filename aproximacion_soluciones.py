# Aproximación de soluciones
# Es similar a enumeración exhaustiva, pero no necesita respuesta exacta
# Se acepta un margen de error al cual se le llama EPSILON
# EPSILON puede aceptar mayor o menor margen de error, pero esta balanza conlleva en más o menos recursos requeridos

# numero al que se le calculará la raiz cuadrada
objetivo = int(input('Escoge un numero: '))

# margen de error para encontrar esa raiz cuadrada
epsilon = 0.01

# valor que se irá sumando secuencialmente hasta encontrar la raiz cuadrada
paso = epsilon**2

# se comenzará a buscar a la raiz cuadrada desde 0.0 en adelante
respuesta = 0.0

# mientras que respuesta al cuadrado no sea igual al objetivo (con un margen de error de 0.01, es decir epsilon), este while se seguirá ejecutando
# respuesta <= objetivo: codigo defensivo; si respuesta es mayor a objetivo, el while seguirá infinitamente, y nunca encontrará a la raíz cuadrada (la raíz cuadrada nunca sería mas grande que el objetivo)
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')