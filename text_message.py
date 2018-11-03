import nexmo

f = open("secrets.txt","r")
lines = f.readlines()

line = [x.strip() for x in lines]

client = nexmo.Client(key=lines[0], secret=lines[1])





client.send_message({
'from': 'Acme Inc', 
'to': TO_NUMBER,
'text': 'A text messae sent using the Nexmo SMS API',

})