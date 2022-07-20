# import pytest
# from api import PetFriends
# from settings import valid_email, valid_password, invalid_email, invalid_password, empty_email, empty_password
#
# @pytest.fixture()
# def get_key():
#     pf = PetFriends()
#     status, key, _ = pf.get_api_key(valid_email, valid_password)
#     assert status == 200
#     assert 'key' in key
#     return key