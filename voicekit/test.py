import os
import sys

def speakThai(text):
	# text = t.split(',')
	stext = ""
	for i in range(len(text)):
	    stext += " ../thaivoices/thwords/" + text[i] + ".mp3"
	os.system('mpg123 -f 2000 ' + stext)


speakThai(['ฟัง','ธรรม'])