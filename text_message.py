#!/usr/bin/env python3
# Import Nexmo-API library.
# (If you get error, please run "pip3 install --user nexmo")
import nexmo

# Read file line-by-line.
with open("secret.txt", "r") as f:
    lines = f.readlines()
    line = [x.strip() for x in lines] # This strips newline characters. (\n)

# Create Nexmo client with our secret keys from file.
client = nexmo.Client(key=lines[0], secret=lines[1])

# 3rd line in file will be the phone number we will text.
TO_NUMBER = lines[2]

# Create message as a Python dictionary.
MessageDict = {'from': 'Remind Me', 'to': TO_NUMBER, 'text': 'testing 1234 is this working'}

# Send message!
client.send_message(messageDict)
