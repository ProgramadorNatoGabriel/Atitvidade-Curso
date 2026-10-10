valores = [20, 50, 80, 10, 100, 60, 25]
valor = []
def media_acima_limite(valores, limite):
    soma = 0
    for numero in valores:
        if (numero > limite):
            soma = soma + numero
            valor.append(numero)
            quantidade = len(valor)
            resultado = soma / quantidade
    if(soma == 0):
        return 0
    return "A média é: " + str(resultado)
limite = int(input("Coloque o limite para ter uma média dos números acima: "))
resultado = media_acima_limite(valores, limite)
print(resultado)