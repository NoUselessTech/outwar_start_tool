import requests

def get_current_location(header):
    get_location_url = 'https://torax.outwar.com/ajax_changeroomb.php?room=0&lastroom=0'
    request_location = requests.get(url=get_location_url, headers=header)
    return request_location.json()
