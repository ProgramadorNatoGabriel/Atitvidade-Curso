estoque = [10, 3, 0, 7, 2, 15, 1, 0, 8]

def analisar_estoque(estoque):
    sem_estoque = 0
    estoque_baixo = 0
    estoque_normal = 0
    for produto in estoque:
        if(produto == 0):
           sem_estoque = sem_estoque + 1
        elif(produto < 4):
            estoque_baixo = estoque_baixo + 1
        else:
            estoque_normal = estoque_normal + 1
    return "Produtos sem estoque: " + str(sem_estoque) + "\nProdutos com estoque baixo: " + str(estoque_baixo) + "\nProduto com estoque normal: " + str(estoque_normal)

resultado = analisar_estoque(estoque)
print(resultado)