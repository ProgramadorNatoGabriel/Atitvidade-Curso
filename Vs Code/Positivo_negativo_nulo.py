numeros = []
positivo = 0
negativo = 0
nulo = 0
for countdown in range(1, 9, 1):
    numero = int(input(f"Digite o {countdown}º número: "))
    numeros.append(numero)
    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1
    else:
        nulo += 1
print(f"Quantidade de números positivos: {positivo}")
print(f"Quantidade de números negativos: {negativo}")
print(f"Quantidade de números nulos: {nulo}")