#Exemplo de Tuplas

coordenadas = (10, 20)
cidades = ("Recife", "Salvador", "Fortaleza")
mista_tupla = ("item", 5, False)

print(f"Tupla de coordenadas: {coordenadas}")
print(f"Primeira cidade: {cidades[0]}")


#Exemplo de Sets              #CHAVES

frutas_set = {"Maçã", "Banana", "Cereja", "Maçã"}
numero_set = {1,2,3,4,5,}

print(f"Set de frutas {frutas_set}")
print(f"Contem Banana? {"Banana" in frutas_set}")

frutas_set.add("Uva")
frutas_set.remove("Banana")
print(f"Set modificado: {frutas_set}")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

uniao = set_a.union(set_b)
intersecao = set_a.intersection(set_b)
diferenca = set_a.difference(set_b)

print(f"União: {uniao}")
print(f"Interseção: {intersecao}")
print(f"Diferença: (A - B): {diferenca}")