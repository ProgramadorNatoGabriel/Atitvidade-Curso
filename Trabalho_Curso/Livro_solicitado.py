def livros_solicitados(livros_solicitado):
    if len(livros_solicitado) == 0:
        print("\n------------------------")
        print("\nNenhum livro cadastrado.")
        print("------------------------")
    for livro in livros_solicitado:
        print("\n------------------------")
        print("\nLivro solicitado: ", livro[0])
        print("Autor: ", livro[1])
        print("Ano do pedido: ", livro[2])
        print("------------------------\n")