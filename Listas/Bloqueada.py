proibidas = ["spam", "propaganda", "golpe"]
palavrass = []
bloqueadas = 0
permitidas = 0
for i in range(1,6,1):
    palavras = input(f"Escreva a {i}° palavra: ")
    palavrass.append(palavras)
    palavra = palavras.lower().strip()
    if(palavra in proibidas):
        print("Palavra bloqueada !")
        bloqueadas = bloqueadas + 1
    else:
        print("Palavra permitida !")
        permitidas = permitidas + 1
print("---- Palavras ----")
for i in range(1,6,1):
    print(i, "-", palavrass[i - 1])
print(f"Foram bloqueados {bloqueadas} palavras.")
