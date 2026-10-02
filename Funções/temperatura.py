def classificar_temperatura(temperatura):
    if(temperatura < 18):
        return "Clima frio"
    elif(temperatura < 28):
        return "Clima agradavél"
    else:
        return "Clima quente"

clima = int(input("Escreva uma temperatura: "))
resultado = classificar_temperatura(clima)
print(resultado)
   