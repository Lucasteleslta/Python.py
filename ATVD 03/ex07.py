def calcular_estatisticas(*numeros):
    media = sum(numeros) / len(numeros)
    valor_maximo = max(numeros)
    valor_minimo = min(numeros)
    
    return media, valor_maximo, valor_minimo

def main():
    numeros = input("Digite os números separados por espaço: ")
    lista_numeros = [float(num) for num in numeros.split()]

    try:
        media, maximo, minimo = calcular_estatisticas(*lista_numeros)
        print(f"Para a lista {lista_numeros}: Média = {media}, Máximo = {maximo}, Mínimo = {minimo}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
