numeros = []

resultado = 0
for countdown in range(1,8,1):
    numero = int(input(f"Digite o {countdown}° número: "))
    numeros.append(numero)
    if(resultado < numero):
        resultado = numero
print(f"Números digitados: {numeros}")
print(f"O maior número é: {resultado}")