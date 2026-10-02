estoque = [15, 2, 8, 0, 20, 4, 11]
def contar_sem_estoque(estoques):
    zero = 0
    for estoque in estoques:
        if(estoque == 0):
            zero += 1
    return zero

def contar_estoque_baixo(estoques):
    acima_de_zero = 0
    for estoque in estoques:
        if(estoque > 0 and estoque < 6):
            acima_de_zero += 1
    return acima_de_zero

def maior_estoque(estoques):
    resultado = 0
    for estoque in estoques:
        if(estoque > resultado):
            resultado = estoque
    return resultado

resultado = contar_sem_estoque(estoque)
resultado1 = contar_estoque_baixo(estoque)
resultado2 = maior_estoque(estoque)

print(f"Produtos sem estoque: {resultado} \nProdutos com estoque baixo: {resultado1} \nProduto com maior estoque {resultado2}")