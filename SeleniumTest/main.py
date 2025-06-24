import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3fa93733d59fefd19563e329c54e52be'
HEADERS = {'trainer_token' : TOKEN, 'Content-Type' : 'application/json'}

body_create_pokemon = {
        "name": "generate",
        "photo_id": -1
}
response_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body_create_pokemon)
print(response_create_pokemon.text)
pokemon_id = response_create_pokemon.json()['id']
print(pokemon_id)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = {"pokemon_id" : pokemon_id})
print(response_add_pokeball.text)

body_edit_pokemon = {
        "pokemon_id" : pokemon_id,
        "name" : "generate",
        "photo_id" : -1
}
response_edit_pokemon = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_edit_pokemon)
print(response_edit_pokemon.text)