def criptografar(numero):
    if len(numero) != 4 or not numero.isdigit():
        return "Número inválido! Deve ser um número de quatro dígitos."

    digitos = [int(digito) for digito in numero]

    digitos = [(digito + 7) % 10 for digito in digitos]

    digitos[0], digitos[2] = digitos[2], digitos[0]
    digitos[1], digitos[3] = digitos[3], digitos[1]

    numero_criptografado = ''.join(map(str, digitos))
    return numero_criptografado


def descriptografar(numero):
    if len(numero) != 4 or not numero.isdigit():
        return "Número inválido! Deve ser um número de quatro dígitos."

    digitos = [int(digito) for digito in numero]
    
    digitos[0], digitos[2] = digitos[2], digitos[0]
    digitos[1], digitos[3] = digitos[3], digitos[1]

    digitos = [(digito - 7) % 10 for digito in digitos]

    numero_descriptografado = ''.join(map(str, digitos))
    return numero_descriptografado

numero = input("Digite um número de 4 dígitos para criptografar: ")
numero_criptografado = criptografar(numero)
print(f"Número criptografado: {numero_criptografado}")

numero_para_descriptografar = input("Digite um número de 4 dígitos criptografado para descriptografar: ")
numero_descriptografado = descriptografar(numero_para_descriptografar)
print(f"Número descriptografado: {numero_descriptografado}")
