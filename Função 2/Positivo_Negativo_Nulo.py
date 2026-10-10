numeros = [8, -3, 0, 12, -7, 5, 0, -1, 9, 4]

def analisar_numeros(numeros):
    positivo = 0
    negativo = 0
    nulos = 0
    for numero in numeros:
        if(numero > 0):
            positivo = positivo + 1
        elif(numero == 0):
            nulos = nulos + 1
        else:
            negativo = negativo + 1
    return "Positivos: " + str(positivo) + "\nNegativos: " + str(negativo) + "\nNulos: " + str(nulos)

resultado = analisar_numeros(numeros)
print(resultado)