def pesquisar_livros(livros):
    livro1 = input("Livro Pesquisado: ").lower().strip()
    for livro in livros:
        if(livro1 in livro):
            print("\nO livro está cadastrado ! ")
            break
        else:
            print("\nLivro não cadastrado !")
        print("------------------------\n")
        