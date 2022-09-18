# Outwar Script

## Version Notes

```
# --- --- --- --- --- --- #
# Author: Connor Peoples  #
# Username: NoUselessTech #
# Version: 0.1            #
# --- --- --- --- --- --- #
```
## Overview

The intention of this script is to let a character run around aimlessly clearning any room of any mobs that are one level lower than the current character level. It's really dumb and will run in circles, but usually does an OK job trying to get around.

## Setup

While this script does assume running on macOS or Linux, it should work OK on Windows as well. Aside from running the script, you will need to do some minimal setup. Regardless of your OS, you will need to setup an environmental variable.

### macOS / linux

Use the following commands: `export outwar_user=<username>`

Use the following commands: `export outwar_pass=<password>`

### Windows

Use the following commands: `setx outwar_user <username>`

Use the following commands: `setx outwar_pass <password>`

## Running Script

Once the environment variables are set, navigate to the root folder of the repo. From there, run `start_tool.py`
