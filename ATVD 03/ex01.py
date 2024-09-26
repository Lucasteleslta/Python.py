m = int(input("digite a altura do retangulo:"))
n = int(input("digite a largura do retangulo:"))

def retangulo(altura=m, largura=n, caractere="*"):
    linha = caractere * largura
    for i in range(altura):
        print (linha)

retangulo (m, n, "*")