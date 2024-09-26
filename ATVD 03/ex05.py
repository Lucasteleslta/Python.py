def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente - 1)

def resto(dividendo, divisor):
    if dividendo < divisor:
        return dividendo
    else:
        return resto(dividendo - divisor, divisor)

def quociente(dividendo, divisor):
    if dividendo < divisor:
        return 0
    else:
        return 1 + quociente(dividendo - divisor, divisor)

def produto(a, b):
    if b == 0:
        return 0
    else:
        return a + produto(a, b - 1)

def soma(n1, n2):
    if n2 == 0:
        return n1
    else:
        return n1 + n2

def main():
    print("Escolha a operação:")
    print("1: Fatorial")
    print("2: Potência")
    print("3: Resto da divisão")
    print("4: Quociente da divisão")
    print("5: Produto")
    print("6: Soma")

    escolha = int(input("Digite o número da operação (1-6): "))

    if escolha == 1:
        n = int(input("Digite um número natural para calcular o fatorial: "))
        print("Fatorial de", n, ":", fatorial(n))
    elif escolha == 2:
        base = int(input("Digite a base: "))
        expoente = int(input("Digite o expoente: "))
        print("Potência de", base, "^", expoente, ":", potencia(base, expoente))
    elif escolha == 3:
        dividendo = int(input("Digite o dividendo: "))
        divisor = int(input("Digite o divisor: "))
        print("Resto de", dividendo, "/", divisor, ":", resto(dividendo, divisor))
    elif escolha == 4:
        dividendo = int(input("Digite o dividendo: "))
        divisor = int(input("Digite o divisor: "))
        print("Quociente de", dividendo, "/", divisor, ":", quociente(dividendo, divisor))
    elif escolha == 5:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        print("Produto de", a, "x", b, ":", produto(a, b))
    elif escolha == 6:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print("Soma de", n1, "+", n2, ":", soma(n1, n2))
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()