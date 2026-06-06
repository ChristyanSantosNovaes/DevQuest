#Exemplo de Leitura e Escrita de Arquivos:

# Escrevendo em um arquivo
with open("meu_arquvio.txt", "w") as arquivo:
    arquivo.write("Esta é a primeira linha.\n")
    arquivo.write("Esta é a segunda linha.\n")
    arquivo.writelines(["Terceira linha.\n", "Quarta linha.\n"])
    print("Dados escritos em meu_arquivo.txt")

print("---------------------------------------------------------------------------------")

# Lendo o arquivo completo
with open("meu_arquvio.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("\nConteudo completo do arquivo:")
    print(conteudo)

print("---------------------------------------------------------------------------------")

# Lendo linha por linha
with open("meu_arquvio.txt", "r") as arquivo:
    print("\nConteudo linha por linha:")
    for linha in arquivo:
        print(linha.strip()) # .strip() remove o caractere de nova linha

print("--------------------------------------------------------------------------------")

# Adicionando ao arquivo
with open("meu_arquvio.txt", "a") as arquivo:
    arquivo.write("Esta é uma nova linha adicionada.\n")
print("Nova linha adicionada a meu_arquivo.txt")

print("---------------------------------------------------------------------------------")

with open("meu_arquvio.txt", "r") as arquivo:
    print("\nConteudo apos adição:")
    print(arquivo.read())