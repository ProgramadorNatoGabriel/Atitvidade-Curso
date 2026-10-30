from menu import mostrar_menu
from Cadastrar_livros import cadastrar_livros
from Solicitar_livro import solicitar_livro
from Verificar_livros import Livros_Cadastrados
from Livro_solicitado import livros_solicitados
from Pesquisar_livro import pesquisar_livros
from pesquisar_livros_solicitados import pesquisar_livros_cadastrados
from Emprestado import cadastrar_livro_emprestado
from Verificar_Emprestimos import verificar_cadastros_emprestados
from Devolução import devolução_livros
true = False
livros = []
livros_solicitado = []
livros_emprestados = []
livros_emprestados2 = []
while true != True:
    mostrar_menu()
    resposta = int(input("Escolha uma opção: "))
    
    if(resposta == 1):
        cadastrar_livros(livros)
    elif(resposta == 2):
        solicitar_livro(livros_solicitado)
    elif(resposta == 3):
        Livros_Cadastrados(livros)
    elif(resposta == 4):
        livros_solicitados(livros_solicitado)
    elif(resposta == 5):
        pesquisar_livros(livros)
    elif(resposta == 6):
        pesquisar_livros_cadastrados(livros_solicitado)
    elif(resposta == 7):
        cadastrar_livro_emprestado(livros, livros_emprestados, livros_emprestados2)
    elif(resposta == 8):
        verificar_cadastros_emprestados(livros_emprestados, livros_emprestados2)
    elif(resposta == 9):
        devolução_livros(livros_emprestados, livros_emprestados2, livros)
    elif(resposta == 10):
        print("Saindo do programa...")
        true = True
        
        