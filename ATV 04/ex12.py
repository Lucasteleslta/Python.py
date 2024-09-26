animal_01 = {
    "Espécie": "cachorro",
    "nome": "Thor",
    "idade": "8 anos",
    "nome do dono": "Lucas"
}

animal_02 = {
    "Espécie": "gato",
    "nome": "Garfield",
    "idade": "11 anos",
    "nome do dono": "Jon Arbuckle"
}

animal_03 = {
    "Espécie": "rato",
    "nome": "ratatouille",
    "idade": "2 anos",
    "nome do dono": "Linguini"
}

animal_04 = {
    "Espécie": "passaro",
    "nome": "Loro José",
    "idade": "35 anos",
    "nome do dono": "Ana maria Braga"
}

animal_05 = {
    "Espécie": "coelho",
    "nome": "Floquinho",
    "idade": "1 ano",
    "nome do dono": "Malu"
}

pets= [animal_01, animal_02, animal_03, animal_04,animal_05]

for animal in pets:
    print("Espécie:", animal["Espécie"])
    print("nome:", animal["nome"])
    print("Idade:", animal["idade"])
    print("nome do dono:", animal["nome do dono"])
    print()
