#Exemplo de Geradores
def gerador_numeros_pares(limite):
    n = 0
    while n < limite:
        yield n
        n += 2

#Usando o gerador
for numero in gerador_numeros_pares(10):
    print(numero)

#Outro exemplo -: gerador de Fibonacci
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("\nSequencia Fibonacci")
for num in fibonacci_generator(7):
    print(num)