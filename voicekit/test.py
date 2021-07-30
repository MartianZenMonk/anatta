import os
import sys
import json

def speakThai(text):
	stext = ""
	for i in range(len(text)):
	    stext += " ../thaivoices/thwords/" + text[i] + ".mp3"
	os.system('mpg123 -d 2 ' + stext)


# speakThai(['ฟัง','ธรรม','ค่ะ'])

# read zenstories file
with open('zenstories.json', 'r') as myfile:
    zdata=myfile.read()

# parse file
d = json.loads(zdata)

print (len(d["zen101"]))