
def divide_elementos_de_lista(lista, divisor):
    # intento generar este código
    try:
        return [i / divisor for i in lista]
    # manejo el error que se llama ZeroDivisionError (lo obtuve del error generado sin try catch al dividir entre 0)
    # BUENA PRÁCTICA: tratar exceptions (errores) de manera específica. En este caso, es el caso específico de que me dividan entre 0; no tengo en cuenta si me dan un valor string por ejemplo
    except ZeroDivisionError as e:
        print(e)
        # BUENA PRÁCTICA: no sólo informar la excepción con un print statemente, sino también dar un resultado para no truncar el programa. En este caso, se informa el error, y posteriormente se entrega la lista original, sin dividirla.
        return lista

lista = list(range(10))
divisor = 2

print(divide_elementos_de_lista(lista, divisor))

