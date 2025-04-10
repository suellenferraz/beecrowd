# Animal

TipoDoAnimal = input()
Especie = input()
Alimentacao = input()

if TipoDoAnimal == "vertebrado":
    if Especie == "ave":
        if Alimentacao == "carnivoro":
            print("aguia")
        elif Alimentacao == "onivoro":
            print("pomba")
    elif Especie == "mamifero":
        if Alimentacao == "onivoro":
            print("homem")
        elif Alimentacao == "herbivoro":
            print("vaca")
elif TipoDoAnimal == "invertebrado":
    if Especie == "inseto":
        if Alimentacao == "hematofago":
            print("pulga")
        elif Alimentacao == "herbivoro":
            print("lagarta")
    elif Especie == "anelideo":
        if Alimentacao == "hematofago":
            print("sanguessuga")
        elif Alimentacao == "onivoro":
            print("minhoca")


