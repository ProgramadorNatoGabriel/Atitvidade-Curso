def devolução_livros(livros_emprestados, livros_emprestados2, livros):
    print("\n---- LIVROS EMPRESTADOS ----")
    
    if len(livros_emprestados2) == 0:
        print("Não há livros emprestados no momento.")
        return

    for i in range(len(livros_emprestados2)):
        print(f"{i + 1} - {livros_emprestados2[i][0]}")
        
    try:
        resposta = int(input("\nEscreva o número do livro desejado para devolução: "))
    except ValueError:
        print("Por favor, digite apenas números inteiros válidos.")
        return
    
    
    indice = resposta - 1
    
    if 0 <= indice < len(livros_emprestados2):
        print("\n---- INFORMAÇÕES DO COMPRADOR ----")
        print("Nome do livro emprestado: " + livros_emprestados2[indice][0])
        print("Autor do livro: " + livros_emprestados2[indice][1])
        print("Data de devolução do livro: " + livros_emprestados2[indice][2])
        print("Nome do comprador: " + livros_emprestados2[indice][3])
        
        livros.append([livros_emprestados2[indice][0], livros_emprestados2[indice][1], livros_emprestados2[indice][2], livros_emprestados2[indice][3]])
        livros_emprestados2.pop(indice)
        livros_emprestados.pop(indice)
        
        
        print("\nLivro devolvido com sucesso e retornado ao estoque!")
    else:
        print("Número inválido! Escolha um número que esteja listado.")