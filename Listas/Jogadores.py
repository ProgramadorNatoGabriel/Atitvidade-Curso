jogadores = ["Lucas", "Pedro", "Marcos", "Rafael", "Bruno"]

print("---- Jogadores ----")
for i in range(1,6,1):
    print(i, "-", jogadores[i - 1])

posição = int(input("Escreva o número do jogador que deseja alterar: "))

jogadores[posição - 1] = jogador = input("Coloque o nome do novo jogador: ")

print("---- Jogadores ----")
for i in range(1,6,1):
    print(i, "-", jogadores[i - 1])