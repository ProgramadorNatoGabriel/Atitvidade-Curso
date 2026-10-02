numeros = [12, 7, 9, 20, 14, 3, 8, 11]
def contar_pares(numeros):
    par = 0
    for numero in numeros:
        if(numero % 2 == 0):
            par = par + 1
    return par
            


resultado = contar_pares(numeros)
print(f"Possui {resultado} números pares. ")