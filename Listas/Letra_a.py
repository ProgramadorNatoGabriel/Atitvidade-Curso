palavras = []
letra_a = []

for i in range(1, 9, 1):
    palavra = input(f"Escreva a {i}° palavra: ")
    palavras.append(palavra)
    if(palavra[0] == "a" or palavra[0] == "A"):
        letra_a.append(palavra)

print("---- Palavras ----")
for i in range(1, 9, 1):
    print(i, "-", palavras[i - 1])

print("\n ---- Começam com A ----")
for i in range(len(letra_a)):
    print(i + 1, "-", letra_a[i])
