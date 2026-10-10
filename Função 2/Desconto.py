def calcular_compra(valor):
    if(valor < 100):
        return "Valor: " + str(valor) + "\nValor final: " + str(valor) + "\nValor economizado: R$ 0.00"
    elif(valor < 300):
        resultado = valor * 0.05
        resultado1 = valor - resultado
        return "Valor: " + str(valor) + "\nValor final: " + str(resultado1) + "\nValor economizado: " + str(resultado)
    elif(valor < 500):
        resultado = valor * 0.10
        resultado1 = valor - resultado
        return "Valor: " + str(valor) + "\nValor final: " + str(resultado1) + "\nValor economizado: " + str(resultado)
    else:
        resultado = valor * 0.15
        resultado1 = valor - resultado
        return "Valor: " + str(valor) + "\nValor final: " + str(resultado1) + "\nValor economizado: " + str(resultado)
    
valor = float(input("Escreva o valor da compra: "))
resposta = calcular_compra(valor)
print(resposta)