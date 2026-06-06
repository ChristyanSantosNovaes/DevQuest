# Indentação e Sintaxe

def saudacao(nome):
    if nome:                     #Quatro Espaços, respeitar indentação
        print(f"Olá, {nome}!")
    else:
        print("Olá, mundo!")

saudacao("Alice")
saudacao("")

#Exemplo de Comentário:

# Este é um comentário de linha única
x = 10  # Atribui o valor 10 à variável x

"""Este é um docstring.
Pode abranger várias linhas
e é usado para documentar o código.
"""

def soma(a, b):
    """Esta função retorna a soma de dois números."""
    return a + b