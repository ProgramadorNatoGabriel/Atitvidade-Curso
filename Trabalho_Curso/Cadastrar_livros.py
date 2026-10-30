def cadastrar_livros(livros):
 livro = input("\nDigite o nome do livro: ").strip().lower()
 autor = input("Digite o nome do autor: ").strip().capitalize()
 gen = input("Gênero do Livro: ").strip().capitalize()
 pag = int(input("Numero de paginas: "))
 livros.append([livro, autor, gen, pag])
 print("Livro cadastrado com sucesso !\n")
 