def cadastrar_livro_emprestado(livros, livros_emprestados, livros_emprestados2):
    emprestado = input("\nEscreva o nome do livro que está sendo emprestado: ")
    autor = input("Digite o autor do livro: ")
    devolução = input("Escreva a data de devolução (xx/xx/xxxx): ")
    comprador = input("Digite o nome do comprador: ")
    
    encontrado = False
    for livro in livros:
        if emprestado.lower() in livro[0].lower():
            print("\nLivro foi marcado como emprestado.")
            livros.remove(livro)
            livros_emprestados.append([emprestado])
            livros_emprestados2.append([emprestado, autor, devolução, comprador])
            encontrado = True
            break
            
    if not encontrado:
        print("Livro não encontrado no estoque geral.")