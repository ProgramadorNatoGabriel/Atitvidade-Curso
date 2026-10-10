vendas = [150, 300, 80, 500, 120, 450, 0, 200]
media = []
def cacular_total(vendas):
    soma = 0
    for numero in vendas:
        soma = soma + numero
    return "O total vendido foi de: R$ " + str(soma)

def calcular_media_vendas(vendas):
    soma = 0
    quantidade = len(vendas)
    for numero in vendas:
        soma = soma + numero
    media1 = soma / quantidade
    media.append(media1)
    return "\nA média das vendas foi de: R$ " + str(media1)

def maior_venda(vendas):
    soma = 0
    for numero in vendas:
        if(soma < numero):
            soma = numero
    return "\nA maior venda foi de: R$ " + str(soma)

def contar_acima_media(vendas, media):
    acima_media = 0
    for numero in vendas:
        if(numero > media[0]):
            acima_media = acima_media + 1
    return "\nVendas acima da média: " + str(acima_media)

resultado = cacular_total(vendas)
resultado1 = calcular_media_vendas(vendas)
resultado2 = maior_venda(vendas)
resultado3 = contar_acima_media(vendas, media)

print(resultado, resultado1, resultado2, resultado3)

 