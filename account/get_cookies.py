#!/usr/bin/python3
import requests
import time

def get_cookies(username, password):
    login_url = 'https://outwar.com/index.php'
    server_id = 1
    login_body = {
        'serverid': server_id,
        'login_username': username,
        'login_password': password
    }

    login_request = requests.post(url=login_url, data=login_body, allow_redirects=False)
    return(requests.utils.dict_from_cookiejar(login_request.cookies))
