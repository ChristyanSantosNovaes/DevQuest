#Exemplo Básico de Decorator:
def meu_decorator(funcao):
    def wrapper():
        print("Algo está acontecendo antes da função ser chamada.")
        funcao()
        print("Algo está acontecendo depois da função ser chamada.")
    return wrapper

@meu_decorator
def minha_funcao():
    print("A função original está sendo executada.")

minha_funcao()

#Exemplo de Decorator com Argumentos:
def repetir(num_vezes):
    def decorator_repetir(funcao):
        def wrapper(*args, **kwargs):
            for _ in range(num_vezes):
                funcao(*args, **kwargs)
        return wrapper
    return decorator_repetir

@repetir(num_vezes=3)
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Pedro")