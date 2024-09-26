n = int(input("Digite um número inteiro não negativo: "))

for i in range(n, 0, -1):
    print (i, end = " ") 
    
print()

def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat

if n >= 0:
    print(f"O fatorial de {n} é {fatorial(n)}")
else:
    print("Por favor, digite um número inteiro não negativo.")

