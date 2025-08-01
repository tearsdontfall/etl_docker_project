import pandas as pd
import requests
import os

def extract_data(params, report_type="history.json", *args, **kwargs):
    base_url = "http://api.weatherapi.com/v1"

    report_type = report_type
    # key = params['key']
    # dt = params['dt']

    url = base_url + f"/{report_type}"

    safety_br = 5
    while safety_br > 0:
        safety_br -= 1
        req = requests.get(url=url, params=params)

        if req.status_code == 200:
            print('Code 200')
            response = req.json()
            break
        else:
            print(f"Error: {req.status_code}")
            print(f"{req.text}")
            return None
            break

    return response
