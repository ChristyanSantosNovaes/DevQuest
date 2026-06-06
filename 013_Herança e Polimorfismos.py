#Exemplo de Herança:
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        raise NotImplementedError ("Subclasses devem implementar este metodo")

    def comer(self):
        print(f"{self.nome} está comendo")

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  #Chama o construtor da classe pai
        self.raca = raca

    def fazer_som(self):
        return "Au Au!"

    def buscar(self):
        print(f"{self.nome} está buscando a bolinha")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome)
        self.cor = cor

    def fazer_som(self):
        return "Miau!"

#Criando objetos das classes filhas
cachorro1 = Cachorro("Rex", "Labrador")
gato1 = Gato("Felix", "Preto")

print(f"{cachorro1.nome} ({cachorro1.raca}): {cachorro1.fazer_som()}")
cachorro1.comer()
cachorro1.buscar()

print(f"{gato1.nome} ({gato1.cor}): {gato1.fazer_som()}")
gato1.comer()

print("-----------------------------------------------------------------------------------------------------------------")

#Exemplo de Polimorfismo:

def descrever_animal(animal):
    print(f"O animal {animal.nome} faz: {animal.fazer_som()}")

descrever_animal(cachorro1)
descrever_animal(gato1)

print("-----------------------------------------------------------------------------------------------------------------")

# Uma lista de animais de diferentes tipos
animais = [Cachorro("Bob","Poogle"), Gato("Mimi", "Branco"), Cachorro("Max", "Pastor alemão")]

for animal in animais:
    descrever_animal(animal)