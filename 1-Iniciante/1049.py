# -*- coding: utf-8 -*

animal1 = input()
animal2 = input()
animal3 = input()

lista = {
    "vertebrado":{
        "ave":{
            "carnivoro" : "aguia",
            "onivoro" : "pomba"
        },
        "mamifero":{
            "onivoro" : "homem",
            "herbivoro":"vaca"
        }
    },
    "invertebrado":{
        "inseto":{
            "hematofago" : "pulga",
            "herbivoro" : "lagarta"
        },
        "anelideo":{
            "hematofago" : "sanguessuga",
            "onivoro" : "minhoca"
        }
    }
}

opcao1 = lista[animal1]
opcao2 = opcao1[animal2]
animal_correspondente = opcao2[animal3]

print(animal_correspondente)