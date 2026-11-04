import requests

nimi = input("Anna pokemonin nimi: ")

pyyntö = "https://pokeapi.co/api/v2/pokemon/" + nimi
vastaus = requests.get(pyyntö).json()

print("Pokemonin tyyppi on:", vastaus["types"][0]["type"]["name"])