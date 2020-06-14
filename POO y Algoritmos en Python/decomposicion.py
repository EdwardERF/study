
class Automovil:

    def __init__(self, modelo, marca, color, year, country):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.year = year
        self.country = country
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)
        self._categoria = 'default'

        if year <= 1970:
            self._categoria = 'clasico'

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.injecta_gasolina(10)
        else:
            self._motor.injecta_gasolina(3)

        self._estado = 'en_movimiento'

class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def injecta_gasolina(self, cantidad):
        pass