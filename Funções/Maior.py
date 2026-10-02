def maior_numero(a, b, c):
    if(a > b and a > c):
        return "O maior número é: " + str(a)
    elif(b > a and b > c):
        return "O maior número é: " + str(b)
    elif(c > a and c > b):
        return "O maior número é: " + str(c)
    else:
        return "Dois números ou mais são iguais"

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: ")) 
c = int(input("Digite o terceiro número: "))
resultado = maior_numero(a, b, c)
print(resultado)