import requests
import pytest
import json
from assertpy import assert_that, soft_assertions


# TODO make that expected categories as a external file
testdata = [
    ("11763", "Dziecko"),
    ("5", "Fail_me"),
]

@pytest.mark.parametrize("id, expected_cat", testdata)
def test_get_category_by_id(authenticate, id, expected_cat):
    """
        Check if default categories has correct names
    """
    # Send reqest and parse response
    access_token = authenticate
    cat_id = id
    url = 'https://api.allegro.pl/sale/categories/{cat_id}'.format(cat_id=cat_id)
    headers = {
        "Authorization": "Bearer " + access_token,
        "Accept": "application/vnd.allegro.public.v1+json"
    }
    #params = {'parent.id': '954b95b6-43cf-4104-8354-dea4d9b10ddf'}

    temp = requests.get(url=url, headers=headers)
    category = json.loads(temp.content.decode("utf-8").replace("'", '"'))

    assert_that(category["name"], "There is different amount of categories than expected").is_equal_to(expected_cat)
    print("")

