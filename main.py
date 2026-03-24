print("Hola, soy Manuel")

zelda = {
    "Link": "El protagonista, es un caballero y no habla",
    "Zelda": "Es la princesa y Link tiene que salvarla",
    "Ganon": "Es el malo y quiere tener el reino de Zelda"
}

pregunta = input("Escribe la palabra que no entiendas con mayuscula en la primera letra")

if pregunta in zelda.keys():
    print(zelda[pregunta])
else:
    print("La palabra no esta en el dicionario")
