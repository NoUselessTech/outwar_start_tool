#!/usr/bin/python3
import requests
from location import current_location,auto_move
from attack import clear_room
from account import details
import time

# Variables
header = {
            'accept': 'application/json, text/javascript, */*',
            'cookie': "ow_play=1102; ow_go=2; ow_userid=852454; ow_serverid=2; lightbox=1; LogQueries12=1; cuserid2=1852077; owip=69.42.249.193; ow_adcode=world; cf_clearance=MigYgLN1vQvZHgvaoVgCpYRZa1QfYcJDPdR_gwEq7l8-1661317865-0-150; token=5cdda1208d44bf3da47a0c3a30f83252; rg_sess_id=4a8db71806330953d2f35d08cb2c509c"
        }
level = details.get_level(header) - 1
last_location = ''

# Functions
#
# https://torax.outwar.com/userstats.php // Get Current level

# Logic
print(' Getting current location')
location_data = current_location.get_current_location(header)

print(' Clearing room')
room_clearing = clear_room.clear_room(location_data, level, header)

while True:
    try:
        last_location = location_data['curRoom']
        print(' Leaving room:', last_location)

        location_data = auto_move.auto_move(header, location_data, last_location)
        print(' Entering room:', location_data['curRoom'])

        print(' Clearing room')
        clear_room.clear_room(location_data, level, header)

        level = details.get_level(header) - 1

        time.sleep(1)

    except:
        print(' Stop going into forbidden areas.')
print (' Done.')
