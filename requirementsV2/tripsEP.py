import json
from helpers.workers import params, postdata, int_oneway_pl
import requests


def test_trips_status_code():
    url = params()['baseUrl'] + '/v2/trips?affiliateId=' + params()['affiliateId'] + '&key=' + params()['key']
    data = json.dumps(int_oneway_pl())
    header = postdata()['headers']
    resp = requests.request("POST", url, headers=header, data=data)
    assert resp.status_code == 200
