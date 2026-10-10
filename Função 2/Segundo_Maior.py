numeros = [15, 8, 22, 10, 30, 18]

def segundo_maior(numeros):
    primeiro = numeros[0]
    segundo = numeros[1]
    if(primeiro < segundo):
        primeiro = segundo
        segundo = primeiro
    for numero in numeros:
         if(numero > primeiro):
            segundo = primeiro
            primeiro = numero
    return segundo

resultado = segundo_maior(numeros)
print(resultado)
