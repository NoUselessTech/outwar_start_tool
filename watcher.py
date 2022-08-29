#!/usr/bin/python3
import os
import time

# variables
target = './start_tool.py'
last_save = ''
current_save = ''

# logic

print(' But who watches the watchers? ')

while True:
    print(' ... ')

    current_save = os.path.getmtime(target)

    if current_save != last_save:
        os.system(target)
        last_save = current_save
        current_save = ''
    
    time.sleep(10)
