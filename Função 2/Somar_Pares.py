numeros = [10, 7, 4, 9, 20, 3, 6, 11]
def somar_pares(numeros):
    soma = 0
    for numero in numeros:
        if (numero %2 == 0):
            soma = soma + numero
    return "A soma dos números pares é: "+ str(soma)

resultado = somar_pares(numeros)
print(resultado)