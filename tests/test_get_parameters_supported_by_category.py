import requests
import pytest
import json
from assertpy import assert_that, soft_assertions


# TODO make that expected categories as a external file
testdata = [
    ("709", ["Stan", "Waga (z opakowaniem)", "EAN", "Kod producenta"]),
    ("5", ["Fail_me"]),
]


@pytest.mark.parametrize("id, expected_params", testdata)
def test_get_parapeters_support_by_cat(authenticate, id, expected_params):
    """
        Check if default categories has correct names
    """
    # Send reqest and parse response
    access_token = authenticate
    cat_id = id
    url = 'https://api.allegro.pl/sale/categories/{cat_id}/parameters'.format(cat_id=cat_id)
    headers = {
        "Authorization": "Bearer " + access_token,
        "Accept": "application/vnd.allegro.public.v1+json"
    }
    temp = requests.get(url=url, headers=headers)
    params = json.loads(temp.content.decode("utf-8").replace("'", '"'))['parameters']

    assert_that(len(params), "There is different amount of categories than expected").is_equal_to(len(expected_params))

    params_names = []
    for par in params:
        params_names.append(par["name"])

    assert_that(params_names, "Category parameters are not correct").is_equal_to(expected_params)

    print("")
