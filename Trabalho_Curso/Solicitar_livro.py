def solicitar_livro(livros_solicitado):
    livro = input("\nQual Livro Deseja Solicitar? ").lower().strip()
    autor =  input("Autor do Livro: ").capitalize().strip()
    data = input("Ano da solicitação: (xx/xx/xxxx) ").strip()
    
    livros_solicitado.append([livro, autor, data])
    print("Livro solicitado com sucesso !")
    
    