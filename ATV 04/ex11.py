pessoa_01 = {
    "primeiro nome": "Lucas",
    "sobrenome": "Teles",
    "idade": 20,
    "cidade": "Brasília"
}

pessoa_02 = {
    "primeiro nome": "maria",
    "sobrenome": "luíza",
    "idade": 19,
    "cidade": "São Paulo"
}

pessoa_03 = {
    "primeiro nome": "Jake",
    "sobrenome": "Peralta",
    "idade": 37,
    "cidade": "Nova York "
}

people = [pessoa_01, pessoa_02, pessoa_03]

for pessoa in people:
    print("Primeiro Nome:", pessoa["primeiro nome"])
    print("Sobrenome:", pessoa["sobrenome"])
    print("Idade:", pessoa["idade"])
    print("Cidade:", pessoa["cidade"])
    print()

