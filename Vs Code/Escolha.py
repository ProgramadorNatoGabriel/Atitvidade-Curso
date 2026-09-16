alunos = ["Ana", "Carlos", "Maria", "Pedro", "João"]

print(f"{alunos[0]} \n{alunos[1]} \n{alunos[2]} \n{alunos[3]} \n{alunos[4]}")
nome = input("Escolha um dos nomes da lista acima: ") 
if nome in alunos:
    print(f"O nome {nome} está na lista.")
else:
    print(f"O nome {nome} não está na lista.")