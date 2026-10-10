notas = [7.5, 5.0, 8.5, 6.0, 9.0, 4.5, 7.0]
media = []
def calcular_media(notas):
    soma = 0
    quantidade = len(notas)
    for numero in notas:
        soma = numero + soma
    resultado = soma / quantidade
    media.append(resultado)
    return "A média da turma é: " + str(resultado)

def contar_acima_media(notas, media):
    acima = 0
    for nota in notas:
        if(nota > media[0]):
            acima = acima + 1
    return "\nPossui " + str(acima) + " notas acima da média"

resultado = calcular_media(notas)
resultado1 = contar_acima_media(notas, media)
print(resultado, resultado1 )