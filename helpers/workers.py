import json
import os
import random

import yaml


def params():
    configfilepath = os.path.dirname(os.path.abspath('config.yaml')) + '/config.yaml'
    with open(configfilepath) as file:
        params = yaml.load(file, Loader=yaml.FullLoader)
    return params


def postdata():
    json_file_path = os.path.dirname(os.path.abspath('postData.json')) + '/postData.json'
    with open(json_file_path) as jFile:
        jsonFile = json.load(jFile)
    return jsonFile


def int_oneway_pl():
    origin_country_codes = params()['origin_country_codes']
    dest_country_codes = params()['dest_country_codes']
    json_file = {
        "data": {
            "type": "TRIP",
            "attributes": {
                "category": "ONE_WAY_TRIP",
                "segments": [
                    {
                        "segmentType": "OUTBOUND",
                        "origin": {
                            "countryCode": '' + random.choice(origin_country_codes) + ''
                        },
                        "destination": {
                            "countryCode": '' + random.choice(dest_country_codes) + ''
                        },
                        "travelMode": "AIR",
                        "departureDate": "2022-02-22",
                        "departureTime": "12:59",
                        "arrivalDate": "2021-02-22",
                        "arrivalTime": "12:59"
                    }
                ]
            }
        }
    }
    return json_file


def dms_rndtrip_pl():
    origin_airport_code = params()['origin_airport_code']
    dest_airport_code = params()['dest_airport_code']
    json_file = {
        "data": {
            "type": "TRIP",
            "attributes": {
                "category": "ROUND_TRIP",
                "segments": [
                    {
                        "segmentType": "OUTBOUND",
                        "segmentSubType": "TRANSIT",
                        "origin": {

                            "airportCode": '' + random.choice(origin_airport_code) + ''
                        },
                        "destination": {

                            "airportCode": '' + random.choice(dest_airport_code) + ''
                        },
                        "departureDate": "2021-08-28T20:37:30.442Z",
                        "departureTime": "00:00",
                        "arrivalDate": "2021-08-28T20:37:30.442Z",
                        "arrivalTime": "00:00",
                        "travelMode": "AIR"
                    },
                    {
                        "segmentType": "OUTBOUND",
                        "origin": {

                            "airportCode": '' + random.choice(origin_airport_code) + ''
                        },
                        "destination": {
                            "airportCode": '' + random.choice(dest_airport_code) + ''
                        },
                        "departureDate": "2021-08-28T20:37:30.442Z",
                        "departureTime": "00:00",
                        "arrivalDate": "2021-08-28T20:37:30.442Z",
                        "arrivalTime": "00:00",
                        "travelMode": "AIR"
                    },
                    {
                        "segmentType": "RETURN",
                        "origin": {
                            "airportCode": '' + random.choice(origin_airport_code) + ''
                        },
                        "destination": {
                            "airportCode": '' + random.choice(dest_airport_code) + ''
                        },
                        "departureDate": "2021-09-04T20:37:30.442Z",
                        "departureTime": "00:00",
                        "arrivalDate": "2021-09-04T20:37:30.442Z",
                        "arrivalTime": "00:00",
                        "travelMode": "AIR"
                    }
                ],
                "travellers": [
                    {
                        "nationality": "D",
                        "vaccinations": [
                            {
                                "type": "COVID_19",
                                "status": "FULLY_VACCINATED"
                            }
                        ]
                    }
                ]
            }
        }
    }
