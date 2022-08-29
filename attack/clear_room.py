#!/usr/bin/python3

import requests
import time

# Functions
def clear_room(room_info, max_level, header):

    root_url = "https://torax.outwar.com/somethingelse.php?lightbox=1&r=world&attackid="
    
    for enemy in room_info['roomDetailsNew']:
        if int(enemy['level']) <= max_level:
            print(' Attacking:', enemy['name'])

            attack_url = root_url + enemy['encid']

            attack_status = requests.get(url=attack_url, headers=header)

            time.sleep(2)

    return True
