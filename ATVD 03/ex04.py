def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def resto(a, b):
    return a % b

def potencia(base, expoente):
    return base ** expoente

def raiz(n):
    if n < 0:
        raise ValueError("Não é possível calcular a raiz de um número negativo.")
    return n ** 0.5

def fatorial(n):
    if n < 0:
        raise ValueError("Fatorial não é definido para números negativos.")
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def logaritmo(n, base):
    if n <= 0 or base <= 1:
        raise ValueError("Logaritmo não é definido para números não positivos ou base menor ou igual a 1.")
    resultado = 0
    while n >= base:
        n /= base
        resultado += 1
    return resultado

def cosseno(x):
    resultado = 0
    for n in range(10):
        resultado += ((-1) ** n) * (x ** (2 * n)) / fatorial(2 * n)
    return resultado

def seno(x):
    resultado = 0
    for n in range(10):
        resultado += ((-1) ** n) * (x ** (2 * n + 1)) / fatorial(2 * n + 1)
    return resultado

def tangente(x):
    return seno(x) / cosseno(x)

def aplicar_operacao(num1=None, num2=None, operacao=None):
    if operacao is None:
        raise ValueError("Uma operação deve ser especificada.")
    
    if operacao in [soma, subtracao, multiplicacao, divisao, resto, potencia]:
        if num1 is None or num2 is None:
            raise ValueError("Dois números devem ser fornecidos para esta operação.")
        return operacao(num1, num2)
    
    elif operacao in [raiz, fatorial]:
        if num1 is None:
            raise ValueError("Um número deve ser fornecido para esta operação.")
        return operacao(num1)
    
    elif operacao in [logaritmo, cosseno, seno, tangente]:
        if num1 is None:
            raise ValueError("Um número deve ser fornecido para esta operação.")
        return operacao(num1) if operacao != logaritmo else operacao(num1, num2)

def main():
    print("Escolha uma operação:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("5: Resto")
    print("6: Potência")
    print("7: Raiz")
    print("8: Fatorial")
    print("9: Logaritmo")
    print("10: Cosseno")
    print("11: Seno")
    print("12: Tangente")

    escolha = int(input("Digite o número da operação (1-12): "))
    
    if escolha in [1, 2, 3, 4, 5, 6]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        operacoes = {
            1: soma,
            2: subtracao,
            3: multiplicacao,
            4: divisao,
            5: resto,
            6: potencia
        }
        
        resultado = aplicar_operacao(num1, num2, operacoes[escolha])
    
    elif escolha in [7, 8, 10, 11, 12]:
        num1 = float(input("Digite o número: "))
        
        operacoes = {
            7: raiz,
            8: fatorial,
            10: cosseno,
            11: seno,
            12: tangente
        }
        
        resultado = aplicar_operacao(num1, operacao=operacoes[escolha])
        
    elif escolha == 9:
        num1 = float(input("Digite o número: "))
        base = float(input("Digite a base: "))
        resultado = aplicar_operacao(num1, base, logaritmo)
    
    else:
        print("Opção inválida.")
        return
    
    print(f"O resultado é: {resultado}")

if __name__ == "__main__":
    main()
