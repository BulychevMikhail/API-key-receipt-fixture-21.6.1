import pytest
import requests
import requests_toolbelt
from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password, empty_email, empty_password

pf = PetFriends()

@pytest.fixture()
def get_api_key(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в
    тезультате содержится слово key"""
    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result
    return result
