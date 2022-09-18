#!/usr/bin/python3
import requests

def get_level(header, outwar_cookies):

    base_url = 'https://torax.outwar.com/userstats.php'
    profile_request = requests.get(url=base_url, headers=header, cookies=outwar_cookies)
    profile_data = profile_request.json()

    return int(profile_data['level'])
