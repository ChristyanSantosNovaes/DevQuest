#Exemplo de Context Managers (com arquivos):

with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Conteudo de exemplo com o 'with'.")
print("Arquivo 'exemplo.txt' escrito e fechado automaticamente!")

with open("exemplo.txt", "r") as arquivo:
    print(f"Conteudo lido: {arquivo.read()}")

#Exemplo de Context Manager Personalizado (usando classe):

class MeuGerenciadorDeTexto:
    def __init__(self, nome):
        self.nome = nome

    def __enter__(self):
        print(f"Entrando no contexto: {self.nome}")
        return self.nome.upper() # Retorna um valor que pode ser atribuído a 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Saindo do contexto: {self.nome}")
        if exc_type:
            print(f"Ocorreu uma exceção: {exc_type}, {exc_val}")
        return False # Retorna False para propagar a exceção, True para suprimir

print("\n--- Usando MeuGenciadorDeTexto ---")
with MeuGerenciadorDeTexto("Recurso A") as recurso:
    print(f"Dentro do contexto, usando: {recurso}")

print("\n--- Usando MeuGenciadorDeTexto com erro ---")
with MeuGerenciadorDeTexto("Recurso B") as recurso:
    print(f"Dentro do contexto, usando: {recurso}")
    raise ValueError("Algo de errado!")

print("\n--- Fim dos exemplos de Context Managers ---")