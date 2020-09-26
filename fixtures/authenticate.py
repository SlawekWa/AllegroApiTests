import base64
import requests
import pytest


@pytest.fixture(scope="module", autouse=True)
def authenticate():
    base_url = 'https://allegro.pl/auth/oauth/token?grant_type=client_credentials'
    username = 'provide client id'
    password = 'provide client secret'

    credentials = (username + ':' + password).encode('utf-8')
    base64_encoded_credentials = base64.b64encode(credentials).decode('utf-8')

    headers = {
        'Authorization': 'Basic ' + base64_encoded_credentials
    }
    temp = requests.post(url=base_url, headers=headers)

    return temp.json()['access_token']
