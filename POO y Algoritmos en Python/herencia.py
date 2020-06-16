
# SUPER CLASE:
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

# SUBCLASE:
class Cuadrado(Rectangulo):

    def __init__(self, lado):
        # Aqui utilizamos función super(), la cual obtiene datos de la superclase (Rectángulo en este caso)
        # Lo correcto es, cuando creamos una subclase, también inicializar el constructor de la superclase con la función super()
        super().__init__(lado, lado)

if __name__ == '__main__':

    rectangulo = Rectangulo(base=3, altura=4)
    print(f'El area del rectangulo es {rectangulo.area()}')

    cuadrado = Cuadrado(lado=5)

    # Aqui estamos usando el método area(), sin haberlo declarado dentro de la clase cuadrado. 
    # El método se está heredando de la superclase Rectángulo.
    print(f'El area del cuadrado es {cuadrado.area()}')