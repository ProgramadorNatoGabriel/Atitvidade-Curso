def verificar_cadastros_emprestados(livros_emprestados, livros_emprestados2):
    print("\n---- LISTA DE LIVROS EMPRESTADOS ----")
    
    # Verifica se a lista está vazia
    if len(livros_emprestados2) == 0:
        print("Nenhum livro emprestado no momento.")
        return
        
    # Percorre todos os empréstimos cadastrados
    for i, item in enumerate(livros_emprestados2):
        print(f"\n--- Empréstimo #{i + 1} ---")
        print("Nome do livro emprestado: " + item[0])
        print("Autor do livro: " + item[1])
        print("Data de devolução do livro: " + item[2])
        print("Nome do comprador: " + item[3])
        print("-" * 30)