def factorial(n):
    """Calcula el factorial de n
    
    n int > 0
    return n!
    """
    if n == 1:
        return 1
    
    return n * factorial(n - 1) # Aquí es donde vuelve a generarse el 'loop'.
    # Muy importante el Scope para comprender lo que pasa aquí.

n = int(input('Escribe un entero: '))

print(factorial(n))