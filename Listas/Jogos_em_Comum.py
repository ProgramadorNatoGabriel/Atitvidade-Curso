jogos_joao = ["Minecraft", "FIFA", "Fortnite", "GTA", "Valorant"]
jogos_pedro = ["GTA", "Rocket League", "Minecraft", "CS", "Valorant"]
jogos_em_comum = []
for i in range(1, 6, 1):
    if(jogos_joao[i - 1] in jogos_pedro):
        jogos_em_comum.append(jogos_joao[i - 1])

print("---- Jogos João ----")
for i in range(len(jogos_joao)):
    print(i + 1, "-", jogos_joao[i])

print("\n---- Jogos Pedro ----")
for i in range(len(jogos_pedro)):
    print(i + 1, "-", jogos_pedro[i])

print("\n---- Jogos em Comum ----")
for i in range(len(jogos_em_comum)):
    print(i + 1, "-", jogos_em_comum[i])