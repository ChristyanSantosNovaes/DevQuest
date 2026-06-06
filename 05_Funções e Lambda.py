#Exemplo de Funções

def saudar(nome="Visitante"):
    """Função que saudar"""
    return f"Olá, {nome}! Bem-Vindo."

def calcular_area_retangulo(largura, altura):
    """Calcula a area de retangulo."""
    return largura * altura

print(saudar("Maria"))
print(saudar())

area = calcular_area_retangulo(5, 10)
print(f"A Area do Retangulo é: {area}")

print("-----------------------------------------------------------------------------------------------------------------")

#Funções Lambda:

somar = lambda a, b: a + b
print(f"somar de 3 e 5: {somar(3, 5)}")

print("-----------------------------------------------------------------------------------------------------------------")

#Usando Lambda com filter()

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pare = list(filter(lambda x: x % 2 == 0, lista_numeros))
print(f"Numeros pares: {pare}")

print("-----------------------------------------------------------------------------------------------------------------")

#Usando Lambda com map()
quadrados = list(map(lambda x: x ** 2, lista_numeros))
print(f"Quadrados: {quadrados}")
