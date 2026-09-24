compras = ["arroz", "feijão", "leite","pão","café"]
print("---- Lista de compras ----")
for i in range(1,6,1):
 print(i, "-", compras[i - 1])

compras[2] = "Suco"

print("\n---- Lista de compras ----")
for i in range(1,6,1):
 print(i, "-", compras[i - 1])