def calcular_digito(cpf_parcial, pesos):
    soma = sum(int(cpf_parcial[i]) * pesos[i] for i in range(len(cpf_parcial)))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def cpf(n, d):
    n_str = str(n)
    d_str = str(d)

    dv1 = calcular_digito(n_str, pesos=range(10, 1, -1))
    cpf_completo = n_str + str(dv1)

    dv2 = calcular_digito(cpf_completo, pesos=range(11, 1, -1))

    return d_str == f"{dv1}{dv2}"

def main():
    cpf_parcial = input("Digite os 9 primeiros dígitos do CPF: ")
    digitos_verificadores = input("Digite os 2 dígitos verificadores: ")

    if len(cpf_parcial) != 9 or len(digitos_verificadores) != 2 or not cpf_parcial.isdigit() or not digitos_verificadores.isdigit():
        print("CPF inválido. Certifique-se de que os 9 primeiros dígitos e os 2 dígitos verificadores estão corretos.")
    else:
        resultado = cpf(cpf_parcial, digitos_verificadores)
        if resultado:
            print("O CPF é válido.")
        else:
            print("O CPF é inválido.")

if __name__ == "__main__":
    main()
