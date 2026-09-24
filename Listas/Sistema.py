carrinho = []

resposta = 6
while resposta != 0:
    print("\n1 - Adicionar produto \n2 - Remover produto \n3 - Mostrar carrinho \n4 - Procurar Produto \n5 - Mostrar quantidade de produtos \n0 - Sair")
    resposta = int(input("\nEscolha o número da opção que deseja: "))

    if(resposta == 1):
        produto = input("\nEscreva o nome do produto que deseja: ")
        product = produto.strip().capitalize()
        carrinho.append(product)

    if(resposta == 2):
        remover = input("\nEscreva o nome do produto que deseja remover da lista: ")
        removerr = remover.strip().capitalize()
        if(removerr in carrinho):
           carrinho.remove(removerr)
    if(resposta == 3):
        print("---- Carrinho ----")
        for i in range(len(carrinho)):
            print(i + 1, "-", carrinho[i])
    if(resposta == 4):
        procurar = input("\nEscreva o nome do produto que deseja achar: ")
        achar = procurar.strip().capitalize()
        if(achar in carrinho):
           print("Produto encontrado !")
           print(procurar)
        else:
           print("produto não encontrado !")
    if(resposta == 5):
        quantidade = len(carrinho)
        print(f"Você possui {quantidade} produtos em seu carrinho !")