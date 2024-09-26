sanduiche_01 = {
    "nome":"x-salada",
    "descrição": "pão,alface,tomate,cebola e queijo"
}
sanduiche_02 = {
    "nome":"classic",
    "descrição": "pão,carne e queijo "
}
sanduiche_03 = {
    "nome":"x-bacon",
    "descrição": "pão, carne, cheddar, bacon e cebola caramelizada"
}
sanduiche_04 = {
    "nome":"chicken",
    "descrição": "pão, frango, salada e maionese"
}

sandwich_orders = [sanduiche_01, sanduiche_02, sanduiche_03, sanduiche_04]
finished_sandwiches = []

for sanduiche in sandwich_orders:
    print("nome:", sanduiche["nome"])
    print("descrição:", sanduiche["descrição"])
    print()

escolha = str(input("Escolha um sanduíche dentre as opções acima: "))
    
sanduiche_escolhido = None
for sanduiche in sandwich_orders:
    if sanduiche["nome"] == escolha:
        sanduiche_escolhido = sanduiche["nome"]
        break

if sanduiche_escolhido:
    print("\npedido em andamento...")
    print(f"Estou preparando seu sanduíche {sanduiche_escolhido}...")
    finished_sandwiches.append(sanduiche_escolhido)
    for finished in finished_sandwiches:
        print("O seu sanduíche está pronto!")
        print(f"=> Sanduíche {finished} está finalizado.")
        print("\nObrigador por comprar com nossa empresa, tenha uma boa refeição. ")
        print ()
else:
    print("Escolha inválida! Por favor, escolha um sanduíche disponível.")


