lista_inicial = [1,2,3,4,5,6,7,8] 
lista_nova = [6,7,8,9,10,11,12,13]

elementos_que_nao_mudaram = set(lista_nova) & set(lista_inicial)
print(f"Os elementos que não mudaram são: {elementos_que_nao_mudaram}")

novos_elementos = ( set(lista_inicial) ^ set(lista_nova)) - set(lista_inicial)
print(f"Os novos elementos são: {novos_elementos}")

elementos_removidos = ( set(lista_inicial) ^ set(lista_nova)) - set(lista_nova)
print(f"Os elementos removidos são: {elementos_removidos}")