codigo_produto = int(input("Digite o código do produto: "))
peso_kg = float(input("Digite o peso do pruduto em kg: "))
origem = int(input("Digite um número entre 1 e 3 de acordo com o código do seu país: ")) 

gramas = peso_kg * 1000
print(f"O peso do produto é:", gramas, "gramas")

if (codigo_produto) == 0:
    print("Digite um codigo de números positivos entre 1 e 10 digitos")

elif (codigo_produto) > 10:
    print("Digite um codigo de números positivos entre 1 e 10 digitos")

elif (origem > 3): 
    print("Digite um número entre 1 e 3")

elif (origem <= 0): 
    print("Digite um número entre 1 e 3")

else: 
    if (codigo_produto < 5):
        preço_grama = 10
        valor_produto = gramas * preço_grama
        print(f"O valor do produto comprado é:", valor_produto)

        if (origem == 1):
            imposto = (valor_produto * 0) / 100
            valor_total = valor_produto + imposto 
            print(f"O valor do imposto é: ", imposto)
            print(f"O valor total, preço total do produto mais imposto é: ", valor_total)

        elif (origem == 2):
            imposto = (valor_produto * 15) / 100
            valor_total = valor_produto + imposto 
            print(f"O valor do imposto é: ", imposto)
            print(f"O valor total, preço total do produto mais imposto é: ", valor_total)

        else:
            imposto = (valor_produto * 25) / 100
            valor_total = valor_produto + imposto 
            print(f"O valor do imposto é: ", imposto)
            print(f"O valor total, preço total do produto mais imposto é: ", valor_total)

    elif (codigo_produto < 8):
        preço_grama = 25
        valor_produto = gramas * preço_grama
        print(f"O valor do produto comprado é:", valor_produto)

        if (origem == 1):
            imposto = (valor_produto * 0) / 100
            valor_total = valor_produto + imposto 
            print(f"O valor do imposto é: ", imposto)
            print(f"O valor total, preço total do produto mais imposto é: ", valor_total)

        elif (origem == 2):
            imposto = (valor_produto * 15) / 100
            valor_total = valor_produto + imposto 
            print(f"O valor do imposto é: ", imposto)
            print(f"O valor total, preço total do produto mais imposto é: ", valor_total)

        else:
            imposto = (valor_produto * 25) / 100
            valor_total = valor_produto + imposto 
            print(f"O valor do imposto é: ", imposto)
            print(f"O valor total, preço total do produto mais imposto é: ", valor_total)
    
    else:
        preço_grama = 35
        valor_produto = gramas * preço_grama
        print(f"O valor do produto comprado é:", valor_produto)

        if (origem == 1):
            imposto = (valor_produto * 0) / 100
            valor_total = valor_produto + imposto 
            print(f"O valor do imposto é: ", imposto)
            print(f"O valor total, preço total do produto mais imposto é: ", valor_total)

        elif (origem == 2):
            imposto = (valor_produto * 15) / 100
            valor_total = valor_produto + imposto 
            print(f"O valor do imposto é: ", imposto)
            print(f"O valor total, preço total do produto mais imposto é: ", valor_total)

        else:
            imposto = (valor_produto * 25) / 100
            valor_total = valor_produto + imposto 
            print(f"O valor do imposto é: ", imposto)
            print(f"O valor total, preço total do produto mais imposto é: ", valor_total)        