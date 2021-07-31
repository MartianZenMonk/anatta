import os
import sys
import json
import time

def speakThai(text):
	stext = ""
	for i in range(len(text)):
	    stext += " ../thaivoices/thwords/" + text[i] + ".mp3"
	os.system('mpg123 ' + stext)


def speaken(text):
	stext = ""
	for i in range(len(text)):
	    stext += " ../dataen/" + text[i] + ".mp3"
	os.system('mpg123 ' + stext)


while True:

	speakThai(['ขวา','ย่าง','หนอ'])
	time.sleep(1)
	speakThai(['ซ้าย','ย่าง','หนอ'])
	time.sleep(1)

	speaken(['lifting','moving','treading'])
	time.sleep(1)
	speaken(['lifting','moving','treading'])
	time.sleep(1)

# read zenstories file
# with open('zenstories.json', 'r') as myfile:
#     zdata=myfile.read()

# # parse file
# d = json.loads(zdata)

# print (len(d["zen101"]))