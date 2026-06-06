#Exemplo de Compreensão

#Cria uma lista de quadrados de numeros de 0 a 9
quandrados = [x**2 for x in range(10)]
print(f"Quadrados: {quandrados}.")

#Criar uma ista de numeros pares de 0 a 9
pares = [x for x in range(10) if x % 2 == 0]
print(f"Pares: {pares}.")

#Converter uma lista de strings para maiusculas
frutas = ["maçã", "banana", "cereja"]
frutas_maiusculas = [fruta.upper() for fruta in frutas]
print(f"Frutas Maiusculas: {frutas_maiusculas}.")

#Compreensão de lista aninhada (para matrizes)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in matriz for num in row]
print(matriz)
print(f"Lista achatada: {flat_list}.")

#Compreensão de Dicionário (Dictionary Comprehension)
#{chave_expressao: valor_expressao for item in iteravel if condicao}
quadrados_dict = {x: x**2 for x in range(5)}
print(f"Dicionário de quadrados: {quadrados_dict}")

#Compreensão de Set (Set Comprehension)
#{expressao for item in iteravel if condicao}
pares_set = {x for x in range(10) if x % 2 == 0}
print(f"Set de pares: {pares_set}")