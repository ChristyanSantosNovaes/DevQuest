#Exemplo de Condicionais

idade = 18

if idade >= 18:
    print("Voce é maior de idade.")
elif idade >= 13:
    print("Voce é adolecente.")
else:
    print("Voce é uma Criança.")

temperatura = 25

if temperatura > 30:
    print("Está muito quente!")
elif 20 <= temperatura <= 30:
    print("Temperatura agradavel.")
else:
    print("Está frio.")


#Exemplo de Laços

#Laço for
frutas = ["maçã", "banana", "cereja"]
for frutas in frutas:
    print(f"Eu gosto de frutas {frutas}.")

#Laço for com range()
for i in range(5):  # Gera números de 0 a 4
    print(f"Contagem: {i}.")

#Laço while
contador = 0
while contador < 3:
    print(f"Contador: {contador}.")
    contador += 1 # Incrementa o contador

#Break e Continue
for i in range(10):
    if i == 3:
        continue    # Pula para a proxima iteração se i for 3
    if i == 7:
        break       # Sai do laço se i for 7
    print(i)