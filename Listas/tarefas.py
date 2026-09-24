tarefas = []

for i in range(1, 6, 1):
    tarefa = input(f"Cadastre a {i}° tarefa: ")
    tarefas.append(tarefa)

print("---- Suas tarefas ----")
for i in range(1,6,1):
    print(i, "-", tarefas[i - 1])