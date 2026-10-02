def converter_minutos(horas):
    return horas * 60

hora = int(input("Escreva uma quantidade em horas para ser retornado em minutos: "))
resultado = converter_minutos(hora)
print(f"{hora} horas da {resultado} minutos.")