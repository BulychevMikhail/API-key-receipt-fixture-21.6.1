import json
import pytest
import requests
from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password, empty_email, empty_password
import os

pf = PetFriends()

@pytest.fixture()
def test_get_api_key(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в
    тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result
    print(status)
    print(result)

@pytest.fixture()
def test_get_all_pets_with_valid_key(test_get_api_key_for, filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key.
    Далее используя этого ключ запрашиваем список всех питомцев и проверяем
    что список не пустой. Доступное значение параметра filter - 'my_pets' либо '' """

    #_, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(test_get_api_key_for, filter)

    assert status == 200
    assert len(result['pets']) > 0


# def test_add_new_pet_with_valid_data(name='котэ', animal_type='кот',
#                                      age='44', pet_photo='images/cat1.jpg'):
#     """Проверяем что можно добавить питомца с корректными данными"""
#
#     # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
#     pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
#
#     # Запрашиваем ключ api и сохраняем в переменую auth_key
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#
#     # Добавляем питомца
#     status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
#
#     # Сверяем полученный ответ с ожидаемым результатом
#     assert status == 200
#     assert result['name'] == name, result['animal_type'] == animal_type and result['age'] == age
