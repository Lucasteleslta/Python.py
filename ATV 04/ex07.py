palavra = str(input("Escreva uma palavra: "))

print(f"O dicionário da palavra {palavra} é:")

for n, i in enumerate (palavra, start=1):
    print(f"{n} => {i}")