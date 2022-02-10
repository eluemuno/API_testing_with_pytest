import random
from helpers.workers import params

import requests


def test_restrictions_status_code():
    url = params()['baseUrl'] + '/v2/restrictions?key=' + params()['key'] + '&filter[country]=' + \
          random.choice(params()['dest_country_codes'])
    resp = requests.request("GET", url)
    assert resp.status_code == 200
