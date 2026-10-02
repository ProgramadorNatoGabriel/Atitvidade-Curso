def calcular_desconto(preço, desconto):
       desconto1 = desconto / 100
       resultado = preço * desconto1
       return preço - resultado
    
preço = float(input("Escreva o preço do produto: "))
desconto = float(input("Escreva o desconto do produto: "))
resultado = calcular_desconto(preço, desconto)
print(f"Preço: {preço} R$ \nDesconto: {desconto}% \nTotal: {resultado} R$")