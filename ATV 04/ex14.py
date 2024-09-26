def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return True
    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogadas = 0

    while True:
        exibir_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1, 2): "))
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1, 2): "))

        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
            print("Posição inválida! Tente novamente.")
            continue

        if tabuleiro[linha][coluna] != " ":
            print("Essa posição já está ocupada! Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1

        if verificar_vitoria(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        if jogadas == 9:
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

jogo_da_velha()
