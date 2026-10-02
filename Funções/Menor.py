Preços = [35.90, 12.50, 89.90, 22.00,15.75]
def menor_preço(preços):
    resultado = 1000000
    for preço in preços:
        if(preço < resultado):
            resultado = preço
    return resultado
resultado = menor_preço(Preços)
print(f"Menor valor {resultado}")