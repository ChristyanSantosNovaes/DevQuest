#Exemplo de Lista                   #COLCHETES

frutas = ["maçã", "banana", "cereja", "maçã"]   # Pode repetir mesmo dados
numeros = [1, 2, 3, 4, 5]
mista = ["texto", 10, True, 3.14]

print(f"Lista de frutas: {frutas}")
print(f"Primeira fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")
print(f"Fatiamento (do segundo ao terceiro): {frutas[1:3]}")

frutas.append("laranja") # Adiciona um item
frutas.remove("banana") # Remove um item
print(f"Lista modificada: {frutas}")

#Exemplo de Dicionário:             #CHAVES

pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "cidade": "São Paulo"
}

print(f"Dicionário pessoa: {pessoa}")
print(f"Nome da pessoa: {pessoa["nome"]}")

pessoa["idade"] = 31 # Altera um valor
pessoa["profissao"] = "Engenheiro" # Adiciona um novo par

print(f"Dicionário modificado: {pessoa}")
print(f"Chaves: {pessoa.keys()}")
print(f"Valores: {pessoa.values()}")
