#Exemplo de Métodos Especiais:

class Livro:    #Construtor da classe, chamado quando um objeto é criado.
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):  #Retorna uma representação em string "legível" do objeto, usada por print() e str().
        return f"Livro: {self.titulo} por {self.autor}"

    def __repr__(self):  #Retorna uma representação em string "oficial" do objeto, usada para depuração e por repr().
        return f"Livro(\"{self.titulo}\", \"{self.autor}\", {self.paginas})"

    def __len__(self):  #Retorna o comprimento do objeto, usado por len().
        return self.paginas

    def __add__(self, other):  #Define o comportamento do operador +.
        if isinstance(other, Livro):
            return self.paginas + other.paginas
        return  NotImplementedError

    def __eq__(self, other):  #Define o comportamento do operador ==.
        if isinstance(other, Livro):
            return self.titulo == other.titulo and self.autor == other.autor

print("-----------------------------------------------------------------------------------------------------------------")

# Criando objetos Livros
livro1 = Livro("O Pequeno Principe", "Antoine de Sanint-Exupéry", 96)
livro2 = Livro("1984", "George Orwell",328)
livro3 = Livro ("O Pequeno Principe", "Antoine de Sanint-Exupéry" , 96 )
print(livro1) #Usa __str__
print(livro2) #Usa __repr__

print(f"Numero de paginas do livro1: {len(livro1)}") #Usa __len__

print(f"Total de paginas (livro1 + livro2): {livro1 + livro2})") #Usa __add__

print(f"Livro1 e igual a Livro2? {livro1 == livro2}") #Usa __eq__
print(f"Livro1 é igual a Livro3? {livro1 == livro3}") #Usa __eq__