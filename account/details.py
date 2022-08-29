#!/usr/bin/python3
import requests

def get_level(header):
    base_url = 'https://torax.outwar.com/userstats.php'
    profile_request = requests.get(url=base_url, headers=header)
    profile_data = profile_request.json()

    return int(profile_data['level'])
