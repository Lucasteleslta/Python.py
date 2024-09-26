import math

def calcular_cos_taylor(x, termos):
    cos_x = 0
    for n in range(termos):
        termo = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
        cos_x += termo
    return cos_x

x = float(input("Digite o valor de x (em radianos): "))

termos = int(input("Digite o número de termos para a série de Taylor: "))

resultado = calcular_cos_taylor(x, termos)

print(f"O valor aproximado de cos({x}) usando {termos} termos da série de Taylor é: {resultado}")
