#Exempo de Operações com Strings

texto = "  Olá, Mundo!  "

print("-----------------------------------------------------------------------------------------------------------------")

# Concatenação
mensagem = "Bem" + "-vindo"
print(f"Mensagem concatenada: {mensagem}")

print("-----------------------------------------------------------------------------------------------------------------")

# Multiplicação
repetido = "abc" * 3
print(f"Texto repetido: {repetido}")

print("-----------------------------------------------------------------------------------------------------------------")

# Indexação e Fatiamento
print(f"Primeiro caractere: {texto[2]}") # 'O'
print(f"Fatiamento: {texto[5:10]}") # 'Mundo'

print("-----------------------------------------------------------------------------------------------------------------")

# Métodos
print(f"Maiúsculas: {texto.upper()}")
print(f"Minúsculas: {texto.lower()}")
print(f"Sem espaços extras: '{texto.strip()}'")
print(f"Substituir: {texto.replace('Mundo', 'Python')}")

palavras = "Python é uma linguagem poderosa".split()
print(f"Dividir em palavras: {palavras}")

junto = "-".join(["um", "dois", "tres"])
print(f"Juntar palavras: {junto}")

print("-----------------------------------------------------------------------------------------------------------------")

#Exemplo de Formatação de Strings:
nome = "Ana"
idade = 25

print("-----------------------------------------------------------------------------------------------------------------")

# Usando o metodo .format()
print("Olá, meu nome é {} e tenho {} anos.".format(nome, idade))
print("Olá, meu nome é {0} e tenho {1} anos. {0} gosta de programar.".format(nome, idade))
print("Olá, meu nome é {n} e tenho {i} anos.".format(n=nome, i=idade))

print("-----------------------------------------------------------------------------------------------------------------")

# Usando f-strings (recomendado)
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")

preco = 49.99
desconto = 0.10
preco_final = preco * (1 - desconto)
print(f"Preço original: R${preco:.2f}. Desconto de {desconto:.0%}. Preço final: R${preco_final:.2f}.")