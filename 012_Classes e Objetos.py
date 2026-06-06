#Exemplo de Classes e Objetos:

class Carro:
    #Atributo de classe (compartilhado por todas as instancias)
    rodas = 4

    def __init__(self, marca, modelo, ano):
        #Atributos da instancia
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"O {self.marca} {self.modelo} acelerou para {self.velocidade} km/h")

    def frear(self, decremento):
        self.velocidade -= decremento
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"O {self.marca} {self.modelo} freou para {self.velocidade} km/h")

# Criando objetos (instancias da classe Carro)
meu_carro = Carro("Toyota", "Corolla", 2022)
carro_amigo = Carro("Honda", "Civic", 2023)

print(f"Meu carro: {meu_carro.marca} {meu_carro.modelo}, Ano: {meu_carro.ano}")
print(f"Carro do meu amigo: {carro_amigo.marca} {carro_amigo.modelo}, Ano: {carro_amigo.ano}")

meu_carro.acelerar(50)
carro_amigo.acelerar(60)
meu_carro.frear(20)


print(f"Numero de rodas (atributo de classe): {Carro.rodas}")