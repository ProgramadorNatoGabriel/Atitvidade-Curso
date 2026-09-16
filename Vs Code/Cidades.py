Cidades = []
for countdown in range(1,6,1):
    cidade = input(f"Escreva o nome da {countdown}° cidade: ")
    Cidades.append(cidade)

print(f"{Cidades[0]}\n{Cidades[1]}\n{Cidades[2]}\n{Cidades[3]}\n{Cidades[4]}")