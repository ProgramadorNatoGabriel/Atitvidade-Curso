
def Livros_Cadastrados(livros):
    if len(livros) == 0:
        print("\nNenhum livro cadastrado")
        return
    print("\n---- LIVROS ----")

    for livro in livros:
        print("Livro: ", livro[0])
        print("Autor: ", livro[1])
        print("Gênero: ", livro[2])
        print("Páginas: ", livro[3])
        print("------------------------\n")