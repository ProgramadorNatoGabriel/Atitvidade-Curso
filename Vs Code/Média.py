numeros = []
resultado = 0
for countdown in range(1, 6 , 1):
    numero = int(input(f"Digite o {countdown}° numero: "))
    numeros.append(numero)
    resultado = resultado + numero


quantidade = len(numeros)
final = resultado / quantidade
print(numeros)
print(f"A soma dos números digitados é igual a: {resultado}")
print(f"Quantidade de números digitados: {quantidade}")
print(f"A média dos números digitados é igual a: {final}")