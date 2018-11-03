#!/usr/bin/env python3

import nexmo

with open("secret.txt", "r") as f:
    lines = f.readlines()
    line = [x.strip() for x in lines]

client = nexmo.Client(key=lines[0], secret=lines[1])

TO_NUMBER = lines[2]

client.send_message({
'from': 'Remind Me', 
'to': TO_NUMBER,
'text': 'testing 1234 is this working',

})