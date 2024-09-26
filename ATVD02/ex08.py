def metodo_babilonico(N, iteracoes=12):
    k = 1.0

    raiz_real = N ** 0.5
    print(f"Raiz real de {N}: {raiz_real:.6f}")
    
    for i in range(1, iteracoes + 1):

        k_novo = 0.5 * (k + N / k)

        print(f"Iteração {i}: k = {k_novo:.6f}")
        k = k_novo
    
    return k

N = float(input("Digite o valor de N: "))

raiz_aproximada = metodo_babilonico(N)

print(f"Valor aproximado da raiz quadrada de {N} após 12 iterações: {raiz_aproximada:.6f}")
