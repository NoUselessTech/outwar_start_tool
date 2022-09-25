#!/usr/bin/python3
import requests
import time
import os
from urllib.parse import urlparse, parse_qs

def get_cookies():
    username = os.environ["outwar_user"]
    password = os.environ["outwar_pass"]
    login_url = 'https://outwar.com/index.php'
    server_id = 1
    login_body = {
        'serverid': server_id,
        'login_username': username,
        'login_password': password
    }

    login_request = requests.post(url=login_url, data=login_body, allow_redirects=False)
    url_info = urlparse(login_request.headers["Location"])
    query = parse_qs(url_info.query)

    outwar_cookies = requests.utils.dict_from_cookiejar(login_request.cookies)
    outwar_cookies['ow_userid'] = query["suid"][0] 
    outwar_cookies['ow_serverid'] = query["serverid"][0]
    return(outwar_cookies)
