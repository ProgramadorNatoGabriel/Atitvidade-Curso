convidados = []

for i in range(1, 9, 1):
    pessoas = input(f"Escreva o {i}° nome: ")
    pessoa = pessoas.lower().strip()
    if(pessoa in convidados):
        print("O nome já está na lista !")
    else:
        convidados.append(pessoa)
        

for i in range(len(convidados)):
    print(i + 1, "-", convidados[i])