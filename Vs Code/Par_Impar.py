numeros = []
par = 0
impar = 0
for countdown in range(1, 11, 1):
    numero = int(input(f"Digite o {countdown}º número: "))
    numeros.append(numero)
    if (numero % 2 == 0):
        par += 1
    else:
        impar += 1
print(numeros)
print(f"Quantidade de números pares: {par}")
print(f"Quantidade de números ímpares: {impar}")