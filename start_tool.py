#!/usr/bin/python3
import requests
import os
from location import current_location,auto_move
from attack import clear_room
from account import details, get_cookies
import time

# Variables
header = {
            'accept': 'application/json, text/javascript, */*',
        }
last_location = ''

# Function
def cookie_to_header_string(cookie_dict):
    cookie_string = ""
    for key in cookie_dict.keys():
        cookie_string += key
        cookie_string += "="
        cookie_string += cookie_dict[key]
        cookie_string += "; "

    return cookie_string


# Logic
print(' Logging in')
outwar_cookies = get_cookies.get_cookies()
header['cookies'] = cookie_to_header_string(outwar_cookies).strip()

print(' Giving time for replication.')
time.sleep(10)

print(' Get account details')
level = details.get_level(header, outwar_cookies) - 1

print(' Getting current location')
location_data = current_location.get_current_location(header, outwar_cookies)

print(' Clearing room')
room_clearing = clear_room.clear_room(location_data, level, header, outwar_cookies)

while True:
    try:
        last_location = location_data['curRoom']
        print(' Leaving room:', last_location)

        
        location_data = auto_move.auto_move(header, outwar_cookies, location_data, last_location)
        print(' Entering room:', location_data['curRoom'])

        print(' Clearing room')
        clear_room.clear_room(location_data, level, header, outwar_cookies)

        level = details.get_level(header, outwar_cookies) - 1

        time.sleep(1)

    except Exception as some_error:
        print(' Something failed...', some_error)
        outwar_cookies = get_cookies.get_cookies()
        header['cookies'] = cookie_to_header_string(outwar_cookies).strip()


print (' Done.')
