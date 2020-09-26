import requests
import pytest
import json
from assertpy import assert_that, soft_assertions


def test_default_categories(authenticate):
    """
        Check if default categories has correct names
    """
    # Send reqest and parse response
    access_token = authenticate
    url = 'https://api.allegro.pl/sale/categories'
    headers = {
        "Authorization": "Bearer " + access_token,
        "Accept": "application/vnd.allegro.public.v1+json"
    }
    temp = requests.get(url=url, headers=headers)
    categories = json.loads(temp.content.decode("utf-8").replace("'", '"'))['categories']

    # Iterate through categories and validate ID and Names
    # TODO fill all expected categories to below list
    expected_categories = ['Dom i Ogród', 'Dziecko', 'Elektronika']
    assert_that(len(categories), "There is different amount of categories than expected").is_equal_to(13)
    with soft_assertions():
        for cat in categories:
            d = cat["name"]
            #print("")
            assert_that(expected_categories, "Category does not exist in expected categories").contains(str(cat["name"]))


def test_nested_categories(authenticate):
    """
        Check if default categories has correct names
    """
    # Send reqest and parse response
    access_token = authenticate
    url = 'https://api.allegro.pl/sale/categories'
    headers = {
        "Authorization": "Bearer " + access_token,
        "Accept": "application/vnd.allegro.public.v1+json"
    }
    #params = {'parent.id': '954b95b6-43cf-4104-8354-dea4d9b10ddf'}
    params = {'parent.id': '11763'}

    temp = requests.get(url=url, headers=headers, params=params)
    categories = json.loads(temp.content.decode("utf-8").replace("'", '"'))['categories']

    print("")
    # Iterate through categories and validate ID and Names
    # TODO create assertion based on below for child category (update list of expected)
    # expected_categories = ['Dom i Ogród', 'Dziecko', 'Elektronika']
    # assert_that(len(categories), "There is different amount of categories than expected").is_equal_to(13)
    # with soft_assertions():
    #     for cat in categories:
    #         d = cat["name"]
    #         #print("")
    #         assert_that(expected_categories, "Category does not exist in expected categories").contains(str(cat["name"]))
