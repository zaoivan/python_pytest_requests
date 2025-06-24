import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3fa93733d59fefd19563e329c54e52be'
HEADERS = {'trainer_token' : TOKEN, 'Content-Type' : 'application/json'}
TRAINER_ID = '5282'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['id'] == TRAINER_ID
#'{"status":"success","data":[{"id":"5282","trainer_name":"FrankleStone","level":"5",
# "pokemons":["311137","298315","296087","302194","317008","304980","301568","301695","298314","317006","317007","287317","287482","302195","287307","312155","303490","311138","287310","341489","304227","287485","312157","290465","304908","304907","287312","303499","304982","287481","287303","311173","287315","298318","301485","287305","287309","311136","341488","341588","341587","302158","341586","302157","302156","302196","303497","312156","303489","303488","304226","303498","287300","287311","287316","287299","286811","287306","287308","287298","287301","287302","287304","304228","288539","290372","304909","304926","304981","298065","298066","298312","298064","298067","298317","307918","301697","301696","301558"],
# "pokemons_alive":["341588"],"pokemons_in_pokeballs":[],"get_history_battle":"0","is_premium":false,"premium_duration":0,"avatar_id":1,"city":"Степногорск"}]}'

# Фикстура, параметризация. Один тест, но с перебором параметров
@pytest.mark.parametrize('key, value', [('id', TRAINER_ID), ('city', 'Степногорск')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value