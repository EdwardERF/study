# Este programa le dejará al usuario elegir bajo qué metodo quiere hallar la raiz cuadrada (enumeración exhaustiva, aproximacion, o busqueda binaria)
import enumeracion_exhaustiva
import aproximacion_soluciones
import busqueda_binaria

print('HALLAR LA RAIZ CUADRADA - SELECCIONE OPCION (1, 2 o 3)')
print('1 - Enumeración exhaustiva')
print('2 - Aproximación de solucion')
print('3 - Busqueda binaria')

selection = int(input('Su eleccion: '))

try:
    objetivo = int(input('A que valor le quiere hallar a la raiz cuadrada?: '))
except ValueError:
    print('Valor incorrecto')

if selection == 1:
    enumeracion_exhaustiva.enumeracion_exhaustiva(objetivo)
elif selection == 2:
    aproximacion_soluciones.aproximacion_soluciones(objetivo)
elif selection == 3:
    busqueda_binaria.busqueda_binaria(objetivo)
else:
    print('Error - Las opciones posibles son 1, 2 o 3')
