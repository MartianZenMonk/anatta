import os
import sys
import json
import time
import random

es_voices = ["englisg+f1","english+f2","english+m1","english+m3","english+m2","english_rp+m2"]

def espeak(t,a='',v='',s='',*args):

    if v == '':
        v = es_voices[2]

    if a == '':
        a = '10'

    if s == '':
        s = '125'

    text = 'espeak -s ' + s + ' -a ' + a + ' -v ' + v + ' "' + str(t) + '"'
    print(t)
    os.system(text)
    return None


def word2int(w):

    if w == "one":
        return 1
    elif w == "two":
        return 2
    elif w == "three":
        return 3
    elif w == "four":
        return 4
    elif w == "five":
        return 5
    elif w == "six":
        return 6
    elif w == "seven":
        return 7
    elif w == "eight":
        return 8
    elif w == "nine":
        return 9
    elif w == "zero":
        return 0

def int2word(n):

    if n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n == 3:
        return "three"
    elif n == 4:
        return "four"
    elif n == 5:
        return "five"
    elif n == 6:
        return "six"
    elif n == 7:
        return "seven"
    elif n == 8:
        return "eight"
    elif n == 9:
        return "nine"
    elif n == 0:
        return "zero"

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


t = "อนิจจาวะตะสังขารา, สังขารทั้งหลายไม่เที่ยงหนอ, อุปปาทะวะยะธัมมิโน, มีอันเกิดขึ้นและเสื่อมไปเป็นธรรมดา, อุปปัชชิตะวานิรุชฌันติ, บังเกิดขึ้นแล้วย่อมดับไป, เตสังวูปะสะโมสุโข, การเข้าไประงับสังขารเหล่านั้นเสียได้เป็นความสุข"


# while True:

# 	speakThai(["ยกส้นหนอ","ยกหนอ","ย่างหนอ","ลงหนอ","ถูกหนอ","กดหนอ"])
# 	time.sleep(1)
# 	speakThai(["ยกส้นหนอ","ยกหนอ","ย่างหนอ","ลงหนอ","ถูกหนอ","กดหนอ"])
# 	time.sleep(1)

# 	speaken(["heelup","lifting","moving","lowering","touching","pressing"])
# 	time.sleep(1)
# 	speaken(["heelup","lifting","moving","lowering","touching","pressing"])
# 	time.sleep(1)

# read zenstories file
# with open('zenstories.json', 'r') as myfile:
#     zdata=myfile.read()

# # parse file
# d = json.loads(zdata)

# print (len(d["zen101"]))

# a = random.randint(0,9)
# b = random.randint(0,9)
# espeak("what is "+ str(a) + " plus "+ str(b))
# c = a + b
# sc = ''
# lc = list(str(c))
# for i in lc:
#     sc += int2word(int(i))

# print(sc)