def calcular_soma(N):
    if N <= 0:
        print("Por favor, insira um número inteiro positivo.")

    soma = 0

    for i in range(1, N + 1):
        soma += 1 / i
    return soma

N = int(input("Digite um valor inteiro e positivo N: "))
resultado = calcular_soma(N)

print(f"A soma da série até {N} é: {resultado}")
