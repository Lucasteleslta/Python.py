dia = int(input("digite o dia: "))
mes = int(input("digite o mês: "))
ano = int(input("digite o ano: "))

def formatar_data(dia, mes, ano):
    return f"{dia}/{mes}/{ano}"

if (dia > 31):
    print ("escreva um dia válido")
elif (mes > 12):
    print ("escreva um mes válido")
elif (ano > 9999):
    print ("escreva um ano válido")
elif (ano <= 0):
    print ("escreva um ano válido")
else: 
    print(formatar_data(dia, mes, ano))

