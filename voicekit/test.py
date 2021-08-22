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


word  = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
word += ["eleven","twelve","thirteen","forteen","fifteen","sixteen"]
number = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def word2int(w):
    
    try:
        n = word.index(w)
        return number[n]
    except:
        return None


def int2word(i):
    
    try:
        n = number.index(i)
        return word[n]
    except:
        return None

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
