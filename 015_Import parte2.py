# Programa principal.py

# Importa o modulo inteiro
import minhas_funcoes
print(minhas_funcoes.saudacao("Alice"))
print(f"O dobro de 5 é: {minhas_funcoes.dobro(5)}")
print(f"Valor de PI: {minhas_funcoes.PI}")

print("-----------------------------------------------------------------------------------------------------------------")

# Importa membros especificos
from minhas_funcoes import saudacao, PI
print(saudacao("bob"))
print(f"PI novamente: {PI}")

print("-----------------------------------------------------------------------------------------------------------------")

# Importa com alias
import minhas_funcoes as mf
print(mf.saudacao("Carlos"))