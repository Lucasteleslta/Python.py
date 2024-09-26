numero = input("Digite um número de 6 dígitos: ")

if len(numero) == 6 and numero.isdigit():
    soma = sum(int(digito) for digito in numero)
    d = soma % 10
    
    print(f"O número da conta é: {numero}-{d}")
else:
    print("Por favor, insira um número válido de 6 dígitos.")
