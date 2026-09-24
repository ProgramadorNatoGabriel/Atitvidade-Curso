palavras = ["sol", "computador", "casa", "programação", "pé", "python"]
palavras_grandes = []

for i in range(1,7,1):
    quantidade = len(palavras[i - 1])
    if(quantidade >= 5):
        palavras_grandes.append(palavras[i - 1])

print("---- Palavras ----")
for i in range(len(palavras)):
 print(i + 1, "-", palavras[i])

print("\n---- Palavras Grandes ----")
for i in range(len(palavras_grandes)):
   print(i + 1, "-", palavras_grandes[i])