def verificar_acesso(usuario, senha):
    if(usuario == "admin" and senha == 1234):
        print("Acesso permitido.")
    elif(usuario != "admin" and senha == 1234):
        print("Úsuario incorreto")
    elif(usuario == "admin" and senha != 1234):
        print("Senha incorreta")
    else: 
        print("Úsuario e senha incorretos")

print("---- Login ----")
usuario = input("Escreva o nome de úsuario: ")
senha = int(input("Escreva a senha: "))

verificar_acesso(usuario, senha)

