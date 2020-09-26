import base64
import requests
import pytest


@pytest.fixture(scope="module", autouse=True)
def authenticate():
    base_url = 'https://allegro.pl/auth/oauth/token?grant_type=client_credentials'
    username = '616a5068584f4545bb3180e7fec4bf83'
    password = 'y05Zj1Eh39cf38ZO3UCUyGmUuTxwsmqVGYwy6zoiOG77NkNarNYiJJDeGUDZ91k1'

    credentials = (username + ':' + password).encode('utf-8')
    base64_encoded_credentials = base64.b64encode(credentials).decode('utf-8')

    headers = {
        'Authorization': 'Basic ' + base64_encoded_credentials
    }
    temp = requests.post(url=base_url, headers=headers)

    return temp.json()['access_token']
