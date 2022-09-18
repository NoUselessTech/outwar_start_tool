#!/usr/bin/python3
import requests
import random
import time

def auto_move(header, outwar_cookies, current_location, last_location):
    base_move_url = "https://torax.outwar.com/ajax_changeroomb.php?lastroom="
    move_url = ''

    options = []
    directions = ['north', 'south', 'east', 'west']

    for direction in directions:
        if current_location[direction] not in ["0", "26137", "28027"]:
            options.append(current_location[direction])

    next_room = random.choice(options)
    move_url = base_move_url + current_location['curRoom']
    move_url += '&room=' + next_room

    location_data = requests.get(url=move_url, headers=header, cookies=outwar_cookies)
    time.sleep(1)
    return location_data.json()
