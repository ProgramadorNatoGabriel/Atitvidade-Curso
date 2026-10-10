numeros = [5, 12, 8, 20, 3, 15, 7]

def diferenca_maior_menor(numeros):
    maior = 0
    menor = 0
    for numero in numeros:
        if(maior < numero):
            maior = numero
    menor = maior
    for numero in numeros:
        if(menor > numero):
            menor = numero
    diferenca = maior - menor
    return "O maior número é " + str(maior) + "\nO menor número é " + str(menor) + "\nDiferença: " + str(diferenca)

resultado = diferenca_maior_menor(numeros)
print(resultado)