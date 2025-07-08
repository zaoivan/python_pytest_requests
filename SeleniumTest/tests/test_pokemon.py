import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN' # USER_TOKEN
HEADERS = {'trainer_token' : TOKEN, 'Content-Type' : 'application/json'}
TRAINER_ID = '5282'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['id'] == TRAINER_ID

# Фикстура, параметризация. Один тест, но с перебором параметров
@pytest.mark.parametrize('key, value', [('id', TRAINER_ID), ('city', 'Степногорск')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value