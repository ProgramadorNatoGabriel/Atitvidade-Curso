precos = [25.0, 80.0, 15.0, 120.0, 45.0]
promoção = []
desconto = 0.10

print("---- Preços ----")
for i in range(len(precos)):
    print(i + i, "-", precos[i-1])


for countdown in range(1,6,1):
    if(precos[countdown - 1] > 50):
        resultado = precos[countdown - 1] * desconto
        precos[countdown - 1] = precos[countdown - 1] - resultado
        promoção.append(precos[countdown - 1])

print("---- Desconto ----")
for i in range(len(promoção)):
    print(i + 1, "-", promoção[i - 1])