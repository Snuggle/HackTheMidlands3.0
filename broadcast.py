#!/usr/bin/env python3

import nexmo

# Open secret.txt
with open("secret.txt", "r") as f:
    lines = f.readlines()
    # Strip whitespace.
    line = [x.strip() for x in lines]

# Get API ID and secret token.
client = nexmo.Client(key=lines[0], secret=lines[1])
client_name = 'Remind Me'

# Get people's numbers from secret.txt
NUMBER_LIST = lines[2:5]

# Messages to send!
TEXT = "Hey! Here's just a quick message to say thank-you for coming and being a part of our group at HackTheMidlands3.0!\n\n" \
"I wish you all the best of luck and thank you for being awesome people. 💕"

SECONDARY_TEXT = "Also, Abdul, please don't forget to delete/cancel the droplet server you have at DigitalOcean so you don't get charged in 1 year. It should be in the settings somewhere, look for 'Destroy'."

# Send message to each number!
for NUMBER in NUMBER_LIST:
    client.send_message({
    'from': client_name, 
    'to': NUMBER,
    'type': 'unicode',
    'text': TEXT,
    })

# Remind Abdul to delete DigitalOcean.
client.send_message({
    'from': client_name, 
    'to': NUMBER_LIST[3],
    'type': 'unicode',
    'text': SECONDARY_TEXT,
    })
