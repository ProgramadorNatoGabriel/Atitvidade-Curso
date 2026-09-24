mochila = ["caderno", "caneta", "lápis", "borracha", "régua"]

print("---- Itens na mochila ----")
for i in range(1, 6, 1):
    print(i, "-", mochila[i - 1])

remover = input("Escreva o nome do item que quer retirar da mochila: ")

rem = remover.lower().strip()
if(rem in mochila):
    mochila.remove(rem)

print("---- Lista atualizada ----")

for i in range(len(mochila)):
    print(i + 1, "-", mochila[i ])