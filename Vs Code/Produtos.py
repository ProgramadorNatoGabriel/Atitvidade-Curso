produtos = []
continuar = "Sim"
while continuar != "não" and continuar != "nao":
    produto = input("Digite o nome do produto: ")
    produtos.append(produto)
    resposta = input("Deseja continuar? (sim/nao):")
    continuar = resposta.lower().strip()


print(("------ Produtos Cadastrados ------"))
print(produtos)
quantidade = len(produtos)
print(f"Quantidade de produtos cadastrados: {quantidade}")
