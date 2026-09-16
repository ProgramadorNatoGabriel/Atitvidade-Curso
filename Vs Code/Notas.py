notas = []
resultado = 0
aprovado = 0
reprovado = 0
for countdown in range(1,11,1):
    nota = float(input(f"Digite a {countdown}ª nota: "))
    notas.append(nota)
    resultado = resultado + nota
    if(nota > 6):
        aprovado = aprovado + 1
    else:
        reprovado = reprovado + 1
quantidade = len(notas)
media = resultado / quantidade
print(f"Notas {notas}")
print(f"Média: {media}")
print(f"Aprovados: {aprovado}")
print(f"Reprovados: {reprovado}")