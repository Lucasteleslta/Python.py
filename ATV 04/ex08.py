lista_01 = [1, 2, 3, 4, 4, 5, 6, 7]
lista_02 = [5, 6, 7, 8, 9, 10, 11]

valores_comuns = set(lista_01) & set(lista_02) 
valores_apenas_na_lista_01 = ( set(lista_01) ^ set(lista_02)) - set(lista_02)
valores_apenas_na_lista_02 = ( set(lista_01) ^ set(lista_02)) - set(lista_01)
valores_nao_repetidos = ( set(lista_01) ^ set(lista_02)) 

print (f"Valores comuns das listas: {valores_comuns}")
print (f"Valores só existentes na primeira lista: {valores_apenas_na_lista_01}")
print (f"Valores só existentes na segunda lista: {valores_apenas_na_lista_02}") 
print (f"Valores não repetidos das listas: {valores_nao_repetidos}")
