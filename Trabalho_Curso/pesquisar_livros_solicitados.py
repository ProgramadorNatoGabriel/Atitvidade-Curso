def pesquisar_livros_cadastrados(livros_solicitado):
  livro1 = input("Livro Pesquisado: ").lower().strip()
  for livro in livros_solicitado:
          if(livro1 in livro):
              print("\nO livro está cadastrado ! ")
              break
              
          else:
              print("\nLivro não cadastrado !")
          print("------------------------\n")