import random

def jogo_da_forca():
    palavras = ['porsche']
    palavra = random.choice(palavras).lower()
    letras_adivinhadas = []
    tentativas = 10

    print("Jogo da Forca!")
    print("_ " * len(palavra))  

    while tentativas > 0:
        letra = input("Adivinhe uma letra: ").lower()

        if letra in letras_adivinhadas:
            print("Você já adivinhou essa letra. Tente outra!")
            continue
        elif letra not in palavra:
            tentativas -= 1
            print(f"A letra '{letra}' não está na palavra. Você ainda tem {tentativas} tentativas.")
        else:
            print(f"Bom trabalho! A letra '{letra}' está na palavra.")

        letras_adivinhadas.append(letra)
        
        palavra_atual = ''.join([letra if letra in letras_adivinhadas else '_' for letra in palavra])
        print("Palavra: ", ' '.join(palavra_atual))

        if '_' not in palavra_atual:
            print("Parabéns! Você adivinhou a palavra:", palavra)
            break
    else:
        print("Você ficou sem tentativas! A palavra era:", palavra)

jogo_da_forca()
