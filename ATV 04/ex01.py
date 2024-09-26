lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52] 

maior_elemento = max(lista)
print (f"O maior elemento é: {maior_elemento}")

menor_elemento = min(lista)
print (f"O menor elemento é: {menor_elemento}")

numeros_pares = [num for num in lista if num % 2 == 0]
print(f"Os números pares são: {numeros_pares}")

primeiro_elemento = lista[0]
ocorrencias_primeiro = lista.count(primeiro_elemento)
print("Ocorrências do primeiro elemento ({}): {}".format(primeiro_elemento, ocorrencias_primeiro))

media = sum(lista) / len(lista)
print (f"A média é: {media}")

numeros_negativos = [num for num in lista if num > 0]
soma_negativos = sum(numeros_negativos)
print (f"A soma dos negativos é: {soma_negativos}")