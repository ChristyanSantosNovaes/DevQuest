#Exemplo de Escopo:    #LEGB (Local, Enclosing, Global, Built-in).
variavel_global = "Eu sou Global"

def funcao_externa():
    variavel_external = "Eu sou Externa"

    def funcao_interna():
        variavel_local = "Eu sou Local"
        print(variavel_local) # Acessa Local
        print(variavel_external) # Acessa Enclosing
        print(variavel_global) # Acessa Global

    funcao_interna()
    # print(variavel_local) # NameError: variavel_local não está definida aqui

funcao_externa()
print(variavel_global)
# print(variavel_externa) # NameError: variavel_externa não está definida aqui

#Exemplo de Closures:
def criar_contador():
    contador = 0 # Variável no escopo envolvente

    def incrementar():
        nonlocal contador # Declara que contador não é local, mas do escopo envolvente
        contador += 1
        return contador
    return incrementar

contador1 = criar_contador()
print(contador1())
print(contador1())

contador2 = criar_contador()
print(contador2())
print(contador2())