cores = ["azul", "verde", "amarelo", "vermelho", "preto"]

print("---- Cores ----")
for i in range(1,6,1):
    print(i, "-", cores[i - 1])
print("\n---- Cores Invertidas ----")
for i in range(1,6,1):
    print(i, "-", cores[5 - i])
