preços = [10, 25, 80, 15, 120, 45]
def contar_acima_do_valor(preços, limite):
    resultado = 0
    for preço in preços:
        
        if(preço < limite):
            resultado = resultado + 1
    return resultado

limite = int(input("Escreva um valor limite que não pode ser ultrapassado: "))
resultado = contar_acima_do_valor(preços, limite)
print(resultado)