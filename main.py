meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "TRYHARD": "Una persona muy bueno en un juego"
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")


if word in meme_dict.keys():
    print(meme_dict[word])
else:
    palabra_nueva = input("Uy, saber vos")
