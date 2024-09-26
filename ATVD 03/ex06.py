n = int(input("Digite um número: "))

def fibonacci(n):
    print ("1", end=", ")
    [i, j] = [0, 1]
    for k in range (1, n):
        print(i+j, end=", ")
        [i, j] = [j, i+j]
    return j
print (f"O enesimo termo é: {fibonacci(n)}")
