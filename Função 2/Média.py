def calcular_situacao(nota1, nota2, nota3):
    resultado = (nota1 + nota2 + nota3) / 3
    if(resultado < 5):
        return "Sua média foi: " + str(resultado) + "\nSituação: Reprovado."
    elif(resultado < 7):
        return "Sua média foi: " + str(resultado) + "\nSituação: Recuperação."
    else:
        return "Sua média foi: " + str(resultado) + "\nSituação: Aprovado."

nota1 = int(input("Escreva o primeiro número: "))
nota2 = int(input("Escreva o segundo número: "))
nota3 = int(input("Escreva o terceiro número: "))
resposta = calcular_situacao(nota1, nota2, nota3)
print(resposta)