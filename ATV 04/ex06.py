lugares_vagos = [10,2,1,3,0]

def controle_cinema():
    while True:
        sala = int(input("Digite o número da sala (1 a 5) ou 0 para sair: "))

        if sala == 0:
            print("Sistema encerrado")
            break

        if sala < 1 or sala > 5:
            print("Número da sala inválido. Tente novamente.")
            continue
        
        lugares_desejados = int(input(f"Quantos lugares você deseja na sala {sala}? "))
        
        if lugares_desejados < 1:
            print("Quantidade de lugares deve ser maior que 0.")
            continue

        indice_sala = sala - 1  
        
        if lugares_desejados <= lugares_vagos[indice_sala]:
            lugares_vagos[indice_sala] -= lugares_desejados
            print(f"Venda realizada! Lugares restantes na sala {sala}: {lugares_vagos[indice_sala]}")
        else:
            print(f"Desculpe, não há lugares suficientes na sala {sala}. Lugares disponíveis: {lugares_vagos[indice_sala]}")

controle_cinema()
