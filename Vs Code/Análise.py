alunos = ["João", "Maria", "Pedro", "Ana", "Lucas", "Beatriz", "Rafael", "Juliana", "Gustavo", "Fernanda"]
notas = []
resultado = 0
aprovados = 0
reprovados = 0
total = 0
acima_media = 0
for countdown in range(1, 11, 1):
    nota = float(input(f"Digite a nota do {countdown}° {alunos[countdown-1]}: "))
    notas.append(nota)
    resultado = resultado + nota
    if(nota > 6):
        aprovados = aprovados + 1
    else:
        reprovados = reprovados + 1
    if(nota == 10):
        total = total + 1
    if(nota > 7):
        acima_media = acima_media + 1
quantidade = len(notas)
media = resultado / quantidade

print(f"As notas digitadas foram: {notas}")

print(f"A quantidade de notas digitadas foi: {quantidade}")
print(f"A soma das notas digitadas é igual a: {resultado}")
print(f"A média das notas digitadas é igual a: {media}")

print(f"A quantidade de alunos aprovados foi: {aprovados}")
print(f"A quantidade de alunos reprovados foi: {reprovados}")
print(f"A quantidade de alunos com nota 10 foi: {total}")
print(f"A quantidade de alunos com nota acima da média foi: {acima_media}")