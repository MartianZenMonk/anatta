#!/usr/bin/env python3

import argparse
import os
import queue
import sounddevice as sd
import vosk
import sys
import json
import random
import csv
import cv2
import gc
import psutil
import pty
import pyautogui
import time

import subprocess
from subprocess import call


from datetime import datetime

import pyttsx3
engine = pyttsx3.init() # object creation
engine.setProperty('voice','english-us') 
engine.setProperty('rate', 125)
engine.setProperty('volume',0.5)

freq = '../dataen/bell.mp3'#550 # Hz
freq2 = '../dataen/3bell.mp3'
dotLength  = 1 #60 # milliseconds
dashLength = 3 #dotLength * 3
pauseWords = 7 #dotLength * 7

alphaToMorse = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".",
                'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---", 'k': "-.-",
                'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-",
                'r': ".-.", 's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--",
                'x': "-..-", 'y': "-.--", 'z': "--..",
                '1': ".----", '2': "..---", '3': "...--", '4': "....-", '5': ".....",
                '6': "-....", '7': "--...", '8': "---..", '9': "----.", '0': "-----",
                ' ': "/", '.': ".-.-.-", ',': "--..--", '?': "..--..", "'": ".----.",
                '@': ".--.-.", '-': "-....-", '"': ".-..-.", ':': "---...", ';': "---...",
                '=': "-...-", '!': "-.-.--", '/': "-..-.", '(': "-.--.", ')': "-.--.-",
                'á': ".--.-", 'é': "..-.."}

def morsecode(message):
    
    if message == "":
        return

    # remembers characters that do not have standard morse code equivalent
    unabletoconvert = ""
    morse = ""
    for char in message.lower():
        if char in alphaToMorse:
            morse += alphaToMorse[char] + ' '
        else:
            unabletoconvert += char
    if len(unabletoconvert) != 0:
        print("These characters are unable to be converted:\n" + ' '.join(unabletoconvert))
    morse = morse[:-1]
    print(morse)
    morseaudio(morse)
        
def dot(dur):
    os.system("mpg123 -q -f 4000 " + freq)
    
def dash(dur):
    os.system("mpg123 -q -f 4000 " + freq2)

def beep(dur):
    """
    makes noise for specific duration.
    :param dur: duration of beep in milliseconds
    """
    #winsound.Beep(freq, dur)
    os.system("mpg123 --loop " + str(dur) + ' -f 2000 ' + freq)

def pause(dur):
    """
    pauses audio for dur milliseconds
    :param dur: duration of pause in milliseconds
    """
    time.sleep(dur*5)

def morseaudio(morse):
    """
    plays audio conversion of morse string using inbuilt windows module.
    :param morse: morse code string.
    """
    for char in morse:
        if char == ".":
            dot(dotLength) #beep(dotLength)
        elif char == "-":
            dash(dashLength) #beep(dashLength)
        elif char == "/":
            pause(pauseWords)
        else:
            # char is blank space
            pause(dashLength)

def speak(text):
        print(text)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        return None


def find_name(name):
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
            if pinfo['name'] == name:
                return True
            else:
                continue
        except psutil.NoSuchProcess:
            pass
    return False


# https://docs.opencv.org/4.5.2/d7/d4d/tutorial_py_thresholding.html
def motion_detect(proc):
    bk = False
    # Assigning our static_back to None
    static_back = None
    # List when any moving object appear
    motion_list = [ None, None ]
    video = cv2.VideoCapture(0)
    while True:
        # Reading frame(image) from video
        check, frame = video.read()
        # Initializing motion = 0(no motion)
        motion = 0

        # Converting color image to gray_scale image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Converting gray scale image to GaussianBlur
        # so that change can be find easily
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # In first iteration we assign the value
        # of static_back to our first frame
        if static_back is None:
            static_back = gray
            continue

        # Difference between static background
        # and current frame(which is GaussianBlur)
        diff_frame = cv2.absdiff(static_back, gray)

        # If change in between static background and
        # current frame is greater than 30 it will show white color(255)
        # thresh_frame = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        thresh_frame = cv2.threshold(diff_frame, 127, 255, cv2.THRESH_BINARY)[1]
        # thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
        thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

        # Finding contour of moving object
        _,cnts,_ = cv2.findContours(thresh_frame.copy(),
                        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in cnts:
            if cv2.contourArea(contour) < 10000:
                continue
            motion = 1

            (x, y, w, h) = cv2.boundingRect(contour)
            # print(str(w*h))
            # making green rectangle arround the moving object
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            # print(str(w*h))
            if w*h > 300000:
                bk = True

        # Appending status of motion
        motion_list.append(motion)

        if bk:
            break

        # cv2.imshow("Gray Frame", gray)
        # cv2.imshow("Difference Frame", diff_frame)
        # cv2.imshow("Threshold Frame", thresh_frame)
        cv2.imshow("Color Frame", frame)

        key = cv2.waitKey(1)
        # if q entered whole process will stop
        if key == ord('q'):
            break

    proc.kill()
    video.release()
    # Destroying all the windows
    cv2.destroyAllWindows()
        
    return None


with open('myhora-buddha-2564.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

today = datetime.today().strftime('%Y%m%d')
holyday = []
# print(len(data))
for i in range(len(data)):
    if i>0:
        if(int(data[i][1])>int(today)):
            holyday.append(data[i][1])
            
# print(holyday)

# gonna test this https://www.analyticsvidhya.com/blog/2021/07/building-a-hand-tracking-system-using-opencv/

"""VOICE"""

voices = ["english-us","english_rp+f3","english+m1","english+m3","english+f1"] # rate 150-200

sutta = {
    "sutta":[
        {"title":"Cankama Sutta",
            "content":[
                {"voice":"1","text":"These are the five rewards for one who practices walking meditation. Which five?"},
                {"voice":"1","text":"He can endure traveling by foot"},
                {"voice":"1","text":"he can endure exertion"},
                {"voice":"1","text":"he becomes free from disease"},
                {"voice":"1","text":"whatever he has eaten & drunk, chewed & savored, becomes well-digested"},
                {"voice":"1","text":"the concentration he wins while doing walking meditation lasts for a long time"},
                {"voice":"1","text":"These are the five rewards for one who practices walking meditation"}
                ]
         },
         {"title":"Moggallana Sutta",
            "content":[
                {"voice":"1","text":"the Blessed One said to Ven. Maha Moggallana,"},
                {"voice":"2","text":"Are you nodding, Moggallana? Are you nodding?"},
                {"voice":"3","text":"Yes, lord"},
                {"voice":"2","text":"Well then, Moggallana, whatever perception you have in mind when drowsiness descends on you, don't attend to that perception, don't pursue it. It's possible that by doing this you will shake off your drowsiness."},
                {"voice":"2","text":"But if by doing this you don't shake off your drowsiness, then recall to your awareness the Dhamma as you have heard & memorized it, re-examine it & ponder it over in your mind. It's possible that by doing this you will shake off your drowsiness."},
                {"voice":"2","text":"But if by doing this you don't shake off your drowsiness, then repeat aloud in detail the Dhamma as you have heard & memorized it. It's possible that by doing this you will shake off your drowsiness."},
                {"voice":"2","text":"But if by doing this you don't shake off your drowsiness, then pull both your earlobes and rub your limbs with your hands. It's possible that by doing this you will shake off your drowsiness."},
                {"voice":"2","text":"But if by doing this you don't shake off your drowsiness, then get up from your seat and, after washing your eyes out with water, look around in all directions and upward to the major stars & constellations. It's possible that by doing this you will shake off your drowsiness."},
                {"voice":"2","text":"But if by doing this you don't shake off your drowsiness, then attend to the perception of light, resolve on the perception of daytime, [dwelling] by night as by day, and by day as by night. By means of an awareness thus open & unhampered, develop a brightened mind. It's possible that by doing this you will shake off your drowsiness."},
                {"voice":"2","text":"But if by doing this you don't shake off your drowsiness, then — percipient of what lies in front & behind — set a distance to meditate walking back & forth, your senses inwardly immersed, your mind not straying outwards. It's possible that by doing this you will shake off your drowsiness."},
                {"voice":"2","text":"But if by doing this you don't shake off your drowsiness, then — reclining on your right side — take up the lion's posture, one foot placed on top of the other, mindful, alert, with your mind set on getting up. As soon as you wake up, get up quickly, with the thought, 'I won't stay indulging in the pleasure of lying down, the pleasure of reclining, the pleasure of drowsiness.' That is how you should train yourself."},
                {"voice":"2","text":"Furthermore, Moggallana, should you train yourself: 'I will not visit families with my pride lifted high.' That is how you should train yourself. Among families there are many jobs that have to be done, so that people don't pay attention to a visiting monk. If a monk visits them with his trunk lifted high, the thought will occur to him, 'Now who, I wonder, has caused a split between me and this family? The people seem to have no liking for me.' Getting nothing, he becomes abashed. Abashed, he becomes restless. Restless, he becomes unrestrained. Unrestrained, his mind is far from concentration."},
                {"voice":"2","text":"Furthermore, Moggallana, should you train yourself: 'I will speak no confrontational speech.' That is how you should train yourself. When there is confrontational speech, a lot of discussion can be expected. When there is a lot of discussion, there is restlessness. One who is restless becomes unrestrained. Unrestrained, his mind is far from concentration."},
                {"voice":"2","text":"It's not the case, Moggallana, that I praise association of every sort. But it's not the case that I dispraise association of every sort. I don't praise association with householders and renunciates. But as for dwelling places that are free from noise, free from sound, their atmosphere devoid of people, appropriately secluded for resting undisturbed by human beings: I praise association with dwelling places of this sort."},
                {"voice":"1","text":"When this was said, Ven. Moggallana said to the Blessed One"},
                {"voice":"3","text":"Briefly, lord, in what respect is a monk released through the ending of craving, utterly complete, utterly free from bonds, a follower of the utterly holy life, utterly consummate: foremost among human & heavenly beings?"},
                {"voice":"2","text":"There is the case, Moggallana, where a monk has heard, 'All phenomena are unworthy of attachment.' Having heard that all phenomena are unworthy of attachment, he fully knows all things. Fully knowing all things, he fully comprehends all things. Fully comprehending all things, then whatever feeling he experiences — pleasure, pain, neither pleasure nor pain — he remains focused on inconstancy, focused on dispassion, focused on cessation, focused on relinquishing with regard to that feeling. As he remains focused on inconstancy, focused on dispassion, focused on cessation, focused on relinquishing with regard to that feeling, he is unsustained by anything in the world. Unsustained, he is not agitated. Unagitated, he is unbound right within. He discerns: 'Birth is ended, the holy life fulfilled, the task done. There is nothing further for this world"},
                {"voice":"2","text":"It is in this respect, Moggallana, that a monk, in brief, is released through the ending of craving, utterly complete, utterly free from bonds, a follower of the utterly holy life, utterly consummate: foremost among human & heavenly beings."}
                ]
         }
         ]
    }

buddhism = {
    "buddha":[
        {"title":"Gautama Buddha",
            "content":[
                {"voice":"2","text":"Gautama Buddha, popularly known as the Buddha was a Śramaṇa who lived in ancient India, 5th to 4th century BCE"},
                {"voice":"2","text":"The Buddha was born into an aristocratic family in the Shakya clan but eventually renounced lay life."},
                {"voice":"2","text":"According to Buddhist tradition, after several years of mendicancy, meditation, and asceticism, he awakened to understand the mechanism which keeps people trapped in the cycle of rebirth."},
                {"voice":"2","text":"The Buddha then traveled throughout the Ganges plain teaching and building a religious community. The Buddha taught a middle way between sensual indulgence and the severe asceticism found in the Indian śramaṇa movement."},
                {"voice":"2","text":"He taught a training of the mind that included ethical training, self-restraint, and meditative practices such as jhana and mindfulness. The Buddha also critiqued the practices of Brahmin priests, such as animal sacrifice and the caste system. "},
                {"voice":"2","text":"Do you want to watch the 10 minutes video clip ?"}
                ]
         }
         ],
    "buddhism":[
        {"title":"Buddhism",
            "content":[
                {"voice":"2","text":""},
                {"voice":"2","text":""},
                {"voice":"2","text":""},
                {"voice":"2","text":""},
                {"voice":"2","text":""},
                {"voice":"2","text":""}
                ]
         }
         ]
    }


q = queue.Queue()
bot_name = "anat ta" # shall use rare vocabulary and add to list such as acumen, coronel
bot = False
focus = False
focus_event = []

# read zenstories file
with open('zenstories.json', 'r') as myfile:
    zdata=myfile.read()

# parse file
d = json.loads(zdata)
m = len(d["zen101"])
n = 0
del zdata
gc.collect()
sequence = [i for i in range(m)]
random.shuffle(sequence)


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def clear_q():
    with q.mutex:
        q.queue.clear()

def stop_player():
    if find_name('vlc'):
        print("killall vlc")
        os.system("killall vlc")
    if find_name('mpg123'):
        print("killall mpg123")
        os.system("killall mpg123")

def get_new_dhamma_files():
    new_files = []
    for file in os.listdir("../mars/dhamma"):
        if file.endswith(".mp3"):
            new_files.append(os.path.join("../mars/dhamma", file))

    # print(new_files)
    newfiles = " + ".join(str(x) for x in new_files) 
    # print(newfiles)
    return newfiles

def runtime_vocabulary():
    with open('vocabulary.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    new_vocab = " ".join(str(x[0]) for x in data) 
    new_vocab += ' '
    del data
    gc.collect()
    return new_vocab


def save_vocabulary(w):
    wlist = []
    wlist.append(w)
    writer = csv.writer(open("vocabulary.csv", "a"))
    writer.writerow(thislist)


def clear_q():
    time.sleep(1)
    with q.mutex:
        q.queue.clear()


def pure_alpha():
    speak("pure alpha sound, move your hand close to webcam to stop")
    os.system("mpg123 -f 1000 ../thaivoices/right_concentation.mp3")
    proc = subprocess.Popen(["mpg123","--loop","-1","../mars/pureAlpha.mp3"])
    motion_detect(proc)
    return None

def bell(l='3',vol='500'):
    subprocess.run(["mpg123","-q","-f",vol,"--loop",l,"../dataen/bell.mp3"])
    return None

def thwords(text):
    stext = ""
    for i in range(len(text)):
        stext += " ../thaivoices/thwords/" + text[i] + ".mp3"
    return stext

def thaiwords(text):
    stext = ""
    for i in range(len(text)):
        stext += " ../thaivoices/thai/" + text[i] + ".mp3"
    return stext

def thaiwordswav(text):
    stext = ""
    for i in range(len(text)):
        stext += " ../thaivoices/thai/" + text[i] + ".wav"
    return stext

def zhwords(text):
    stext = ""
    for i in range(len(text)):
        stext += " ../thaivoices/chinese/" + text[i] + ".mp3"
    return stext

def engwords(text):
    stext = ""
    for i in range(len(text)):
        stext += " ../thaivoices/english/" + text[i] + ".mp3"
    return stext


def relax_walk(t=5,vol='1000'):
    text  = ["พุท","โธ","พุท","โธ","เหยียบ","เหยียบ","รู้","ลม","หาย","ใจ","รู้","กาย","เคลื่อน","ไหว","รู้","ใจ","นึก","คิด","มี","จิต","เบิก","บาน"]
    text += ["พุท","โธ","พุท","โธ","เหยียบ","เหยียบ","ถอน","ความ","พอ","ใจ","และ","ความ","ไม่","พอ","ใจ","ใน","ใจ","ออก","เสีย","ได้"]
    text += ["พุท","โธ","พุท","โธ","เหยียบ","เหยียบ","จิต","เบิก","บาน","หาย","ใจ","เข้า","จิต","โล่ง","เบา","หาย","ใจ","ออก"]
    text += ["พุท","โธ","พุท","โธ","เหยียบ","เหยียบ","รู้","ลม","ยาว","รู้","ลม","สั้น","รู้","กาย","ทั้ง","ปวง","ทำ","กาย","ลม","ให้","ประ","ณีต"]
    tx   = thaiwords(text)
    tx_list = tx.split(' ')
    # print(tx_list)
    i = 1
    n = len(tx_list) - 1
    timeout = time.time() + 60*t   
    while True:
        if time.time() > timeout and i == n:
            break
        else:
            # os.system("cvlc --play-and-exit --gain 1 " + tx_list[i])
            os.system("mpg123 -q -f "+ vol + " " + tx_list[i])
        time.sleep(0.25)
        if i < n:
            i += 1
        else:
            i = 1
    # os.system("cvlc --play-and-exit --gain 1 " + tx_list[i])
    os.system("mpg123 -q -f "+ vol + " " + tx_list[i])
    time.sleep(1)
    del text
    del tx
    del tx_list
    gc.collect()
    clear_q()
    return None


def anapanasati(ts=5,vol='5000'):

    t  = 'พุท โธ พุท โธ เหยียบ เหยียบ รู้ ลม ยาว รู้ ลม สั้น รู้ กาย ทั้ง ปวง ทํา กาย ลม ให้ ประ ณีต '
    t += 'พุท โธ พุท โธ เหยียบ เหยียบ รู้ ปี ติ รู้ สุข รู้ เว ทะ นา ทํา เว ทะ นา ให้ ระ งับ '
    t += 'พุท โธ พุท โธ เหยียบ เหยียบ รู้ พร้อม ซึ่ง จิต ทํา ให้ จิต บัน เทิง ทํา จิต ให้ ตั้ง มั่น ทํา จิต ให้ ปล่อย ' 
    t += 'พุท โธ พุท โธ เหยียบ เหยียบ ตาม เห็น ความ ไม่ เที่ยง ตาม เห็น ความ คลาย กํา หนัด ตาม เห็น ความ ดับ ไม่ เหลือ ตาม เห็น ความ สลัด คืน'
    text = t.split(' ')
    # print(text)
    tx   = thaiwords(text)
    tx_list = tx.split(' ')
    # print(tx_list)
    i = 1
    n = len(tx_list) - 1
    timeout = time.time() + 60*ts   
    while True:
        if time.time() > timeout and i == n:
            break
        else:
            os.system("mpg123 -q -f "+ vol + " " + tx_list[i])
        time.sleep(0.25)
        if i < n:
            i += 1
        else:
            i = 1
    os.system("mpg123 -q -f "+ vol + " " + tx_list[i])
    time.sleep(1)
    del t
    del text
    del tx
    del tx_list
    gc.collect()
    clear_q()
    return None

def musk_walk(ts=5,vol='5000'):

    t  = 'พุท โธ พุท โธ เหยียบ เหยียบ ความ เห็น ชอบ สัม มา ทิฏ ฏิ ความ รู้ ใน ทุกข์ ความ รู้ ใน เหตุ ให้ เกิด ทุกข์ ความ รู้ ใน ความ ดับ แห่ง ทุกข์ ความ รู้ ใน ทาง ดำ เนิน ให้ ถึง ความ ดับ แห่ง ทุกข์ '
    t += 'พุท โธ พุท โธ เหยียบ เหยียบ ความ ดำริ ชอบ สัม มา สัง กัป โป ดำริ ใน การ ออก จาก กาม ดำริ ใน การ ไม่ มุ่ง ร้าย ดำริ ใน การ ไม่ เบียด เบียน '
    t += 'พุท โธ พุท โธ เหยียบ เหยียบ การ พูด จา ชอบ สัม มา วา จา เว้น จาก การ พูด ไม่ จริง เว้น จาก การ พูด ส่อ เสียด เว้น จาก การ พูด หยาบ เว้น จาก การ พูด เพ้อ เจ้อ '
    t += 'พุท โธ พุท โธ เหยียบ เหยียบ การ ทำ การ งาน ชอบ สัม มา กัม มัน โต เว้น จาก การ ฆ่า เว้น จาก การ ถือ เอา สิ่ง ของ ที่ เจ้า ของ ไม่ ได้ ให้ เว้น จาก การ ประพฤติ ผิด ใน กาม '
    t += 'พุท โธ พุท โธ เหยียบ เหยียบ การ เลี้ยง ชี วิต ชอบ สัม มา อา ชี โว ไม่ ทำ อา ชีพ ทุ จริต ทำ อา ชีพ สุ จริต '
    t += 'พุท โธ พุท โธ เหยียบ เหยียบ ความ เพียร ชอบ สัม มา วา ยา โม ไม่ ทำ ชั่ว ใหม่ เลิก ทำ ชั่ว ที่ ยัง ทำ อยู่ ทำ ความ ดี เพิ่ม รัก ษา ความ ดี ที่ ทำ ไว้ '
    t += 'พุท โธ พุท โธ เหยียบ เหยียบ ความ ระ ลึก ชอบ สัม มา สติ มี สติ ใน กาย มี สติ ใน เว ทะ นา มี สติ ใน จิต มี สติ ใน ธรรม มี ความ เพียร เผา กิเลส มี ความ รู้ สึก ตัว มี สติ ถอน ความ พอ ใจ และ ความ ไม่ พอ ใจ ใน ใจ ออก เสีย ได้ '
    t += 'พุท โธ พุท โธ เหยียบ เหยียบ ความ ตั้ง ใจ มั่น ชอบ สัม มา สมา ธิ เข้า ถึง ปฐม ฌาน มี วิตก วิจาร ปีติ สุข เข้า ถึง ทุติย ฌาน ไม่ มี วิตก วิจาร มี แต่ ปีติ สุข '
    t += 'เข้า ถึง ตติย ฌาน ไม่ มี ปีติ มี ความสุข ด้วย นามกาย เป็น ผู้ อยู่ อุ เบก ขา มี สติ อยู่ เป็น ปกติ สุข เข้า ถึง จตุตถ ฌาน ไม่ มี ทุกข์ ไม่ มี สุข มี แต่ ความ ที่ สติ เป็น ธรรมชาติ บริสุทธ์ เพราะ อุ เบก ขา แล้ว แล อยู่'


    text = t.split(' ')
    tx   = thaiwords(text)
    tx_list = tx.split(' ')
    # print(tx_list)
    i = 1
    n = len(tx_list) - 1
    timeout = time.time() + 60*ts  
    while True:
        if time.time() > timeout and i == n:
            break
        else:
            os.system("mpg123 -q -f "+ vol + " " + tx_list[i])
        time.sleep(0.25)
        if i < n:
            i += 1
        else:
            i = 1
    os.system("mpg123 -q -f "+ vol + " " + tx_list[i])
    time.sleep(1)
    del t
    del text
    del tx
    del tx_list
    gc.collect()
    clear_q()
    return None


def counting_walk(t=15,fast=False,l='th',vol='2000'):

    if l == 'en':
        tt = "percipient of what lies in front & behind, set a distance to meditate walking back & forth, your senses inwardly immersed, your mind not straying outwards."
        espeak(tt,vol)
        t1 = 0
        if int(vol) > 50:
            vol = '50'
        tx_list = ['0','1','2','3','4','5','6','7','8','9','10']
        cmd = "espeak -a " + vol + " "
    elif l == 'zh':
        os.system('mpg123 -q -f ' + vol + ' ../thaivoices/chinese_walk.mp3')
        t1 = 1
        tx = zhwords(['1','2','3','4','5','6','7','8','9','10'])
        tx_list = tx.split(' ')
        cmd = 'mpg123 -q -f ' + vol + ' '
    elif l == 'wav':
        os.system('mpg123 -q -f ' + vol + ' ../thaivoices/before_walking.mp3')
        t1 = 0.5
        tx = thaiwordswav(['1','2','3','4','5','6','7','8','9','10'])
        tx_list = tx.split(' ')
        cmd = 'aplay '
    else:
        os.system('mpg123 -q -f ' + vol + ' ../thaivoices/before_walking.mp3')
        t1 = 1
        tx = thaiwords(['01','02','03','04','05','06','07','08','09','10'])
        tx_list = tx.split(' ')
        cmd = 'mpg123 -q -f ' + vol + ' '

    i  = 1
    n = 5
    bell('1')
    timeout = time.time() + 60*t
    while True:
        print(n)        
        if time.time() > timeout and i < 11:
            break
        else:
            if fast:
                os.system(cmd + tx_list[i])
                time.sleep(t1)
                i += 1
            else:
                os.system(cmd + tx_list[i])
                time.sleep(t1)
                os.system(cmd + tx_list[i])
                time.sleep(t1)
                i += 1

        if i>n and n < 10:
            n += 1
            i = 1  
        elif i>10:
            n = 5
            i = 1  
    return None 


def kanaanub(t=15,fast=False,l='th',vol='10'):

    if l == 'en':
        tt = "percipient of what lies in front & behind, set a distance to meditate walking back & forth, your senses inwardly immersed, your mind not straying outwards."
        speak(tt)
        t1 = 0
        tx_list = ['0','1','2','3','4','5','6','7','8','9','10']
    elif l == 'zh':
        tt = "Shezhi yiduan juli, laihui zoudong, rang ganguan chanjan zai neixin shen chu, bu xiang wai zoushen."
        speak(tt)
        t1 = 0
        tx_list = ['Ling','Yi','Er','San','Si','Wu','Liu','Qi','Ba','Jiu','Shi']       
    else:
        os.system('mpg123 -q -f 1000 ../thaivoices/before_walking.mp3')
        t1 = 0
        tx_list = ['soon','noong','song','sam','see','ha','hok','jed','pad','kao','sib']

    cmd = "espeak -s 150 -a " + vol + " "

    i  = 1
    n = 5
    bell('1')
    timeout = time.time() + 60*t
    while True:
        print(n)        
        if time.time() > timeout and i < 11:
            break
        else:
            if fast:
                os.system(cmd + tx_list[i])
                time.sleep(t1)
                i += 1
            else:
                os.system(cmd + tx_list[i])
                time.sleep(t1)
                os.system(cmd + tx_list[i])
                time.sleep(t1)
                i += 1

        if i>n and n < 10:
            n += 1
            i = 1  
        elif i>10:
            n = 5
            i = 1  
    return None 


def remind_breathing(t=30,vol='500',l='th',t1=0):
    bell('1',vol)
    if l == 'zh':
        text = ['欢快地吸气','呼气并感到放松']
        tx   = zhwords(text)
    elif l == 'en':
        text = ['cheerful_breathing_in','relieved_breathing_out']
        tx   = engwords(text)
    elif l == 'th1':
        text = ["พุท","โธ","พุท","โธ","หาย","ใจ","เข้า","พุท","หาย","ใจ","ออก","โธ"]
        tx   = thwords(text)
    else:
        text = ["จิต","เบิก","บาน","หาย","ใจ","เข้า","จิต","โล่ง","เบา","หาย","ใจ","ออก"]
        tx   = thwords(text)

    timeout = time.time() + 60*t   
    while True:
        if time.time() > timeout:
            break
        else:
            os.system("mpg123 -q -f "+ vol + " " + tx)
            time.sleep(t1)
    bell('1',vol)
    clear_q()
    return None

def with_opencv(filename):

    video = cv2.VideoCapture(filename)

    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    sec = frame_count / fps

    return sec


def cheer_up():
    speak("play cheerful video clip")
    stop_player()               
    cheerful  = ['--stop-time 120 ../sound/timelapse/flowers.mp4','--start-time 8 --stop-time 208 ../sound/timelapse/cacti.mp4']
    cheerful += ['--start-time 10 --stop-time 205 ../sound/timelapse/Bug-Eating-Plants.mp4','--start-time 30 --stop-time 630 ../sound/timelapse/universe.mp4']
    cheerful += ['../sound/timelapse/from-iss.mp4','--start-time 37 --stop-time 228 ../sound/timelapse/universe.mp4']
    cheerful += ['../sound/timelapse/nerve.mp4','--stop-time 305 ../sound/timelapse/nox.mp4']
    i = random.randint(0,7)              
    try:
        command = "cvlc -f --video-on-top --play-and-exit " + cheerful[i]
        subprocess.run(command, stdout=subprocess.PIPE, shell=True)
        stop_player()
    except:
        speak("sorry can not play video clip")
    return None

def funny_animals():
    animals = ['--gain 0 ../sound/animals/panda1.mp4']
    try:
        command = "cvlc -f --video-on-top --play-and-exit " + animals[0]
        subprocess.run(command, stdout=subprocess.PIPE, shell=True)
        stop_player()
    except:
        speak("sorry can not play video clip")
    return None

# International Code of Signals
ics  = 'a alfa b bravo c charlie d delta e echo f foxtrot g golf h hotel i india j juliet k kilo l lima m mike n november o oscar p papa '
ics += 'q quebec r romeo s sierra t tango u uniform v victor w whiskey x xray y yankee z zulu'
ics_list = ics.split(' ')
del ics
gc.collect()


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    '-m', '--model', type=str, metavar='MODEL_PATH',
    help='Path to the model')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-r', '--samplerate', type=int, help='sampling rate')
args = parser.parse_args(remaining)

try:
    if args.model is None:
        args.model = "model"
    if not os.path.exists(args.model):
        print ("Please download a model for your language from https://alphacephei.com/vosk/models")
        print ("and unpack as 'model' in the current folder.")
        parser.exit(0)
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, 'input')
        # soundfile expects an int, sounddevice provides a float:
        args.samplerate = int(device_info['default_samplerate'])

    #TEST
    # cheer_up()
    # kanaanub(1,False,'zh','60')
    # counting_walk(1,False,'wav')
    # funny_animals()
    remind_breathing(1,'2000','th1')
    # a = with_opencv('../sound/timelapse/flowers.mp4')
    # print(a)
    # musk_walk()
    # relax_walk(1,'5000')

    model = vosk.Model(args.model)
   
    with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device, dtype='int16',
                            channels=1, callback=callback):
            print('#' * 80)
            print('Hello my name is ',bot_name,' please call my name before speak to me ;)')
            print('Press Ctrl+C to stop')
            print('#' * 80)

            new_vocab = runtime_vocabulary()

            runv  = '["acumen anat alpha ta hey begin buddha buddhist chanting close day dhamma do down eighty face holy how mantra '
            runv += 'meditation mindfulness news no now on off open play please quiet sermons seventy shutdown silent sitting sixty '
            runv += 'mouse left right scroll click exit center sky star page browse technique wise new playing speak kill all pali '
            runv += 'morning evening practice om tibetan ohm blooming flower the sun heart clip thai my water morse code real chapter '
            runv += 'one two three four five six seven eight nine ten zero fifteen twenty thirty forty fifty sixty repeat mode '
            runv += 'letter a b c d e f g h i j k l m n o p q r s t u v w x y z relax walk cheerful clip '
            runv += new_vocab
            # runv += 'is am are be was were do does did done had have has can could shall should might may maybe '
            runv += 'show sleep start stop story sutra tell time to turn up volume wake walking what when who yes zen fire fox"]'
            
            rec = vosk.KaldiRecognizer(model, args.samplerate, runv)

            stop_player()
            engine.say('Hello my name is '+ bot_name +' please call my name before speak to me')
            engine.runAndWait()
            engine.stop()

            # master, slave = os.openpty()
            
            global proc
            n = 0
            proc_name = ''
            proc_ck = False
            repeat  = False
            yesno   = False

            with q.mutex:
                q.queue.clear()

            while True:
                data = q.get()
                # print(q.qsize())    
                if rec.AcceptWaveform(data):
                    w = rec.Result()
                    # print(w)
                    z = json.loads(w)
                    words = z["text"].split()

                    if bot_name == z["text"] or ("hey" in words and "acumen" in words):
                        bot = True
                        speak("yes sir")
                        clear_q()
                        words = []

                    elif not bot:
                        if len(words)==0:
                            print("[-_-]")
                        else:
                            print("[^_^]o ")
                            print(words) 
                            if "hello" in words:
                                speak("Hello!") 
                            # elif "hey" in words:
                            #     speak('Hi!')

                    if not yesno and bot and repeat and len(words) > 0:
                        speak("Do you said " + z["text"] + "?") 
                        right_words = words
                        words = []
                        yesno = True
                        clear_q()
                    elif yesno:
                        if "no" in words:
                            words = []
                            yesno = False
                            speak("ok, please speak again")
                            clear_q()
                        elif "yes" in words:
                            words = right_words
                            yesno = False
                        else:
                            words = []
                            text  =  " ".join(str(x) for x in right_words) 
                            speak("Do you said " + text + "?")
                            speak("please answer yes or no")
                            clear_q()
                   
                    if bot or focus:
                        print(z["text"])
                        print("Listening...")

                        if focus:
                            if "yes" in words:
                                proc = subprocess.Popen(focus_event)
                                focus = False
                                focus_event = []
                            elif "no" in words:
                                focus = False
                                focus_event = []

                        elif "repeat" in words and "mode" in words:
                            if "on" in words:
                                repeat = True
                                speak("Repeat mode on")
                            elif "off" in words:
                                repeat = False
                                speak("Repeat mode off")
                            bot = False

                        elif "relax" in words and "walk" in words:
                            relax_walk(5)

                        elif "cheerful" in words and "clip" in words:
                            cheer_up()

                        elif "kill" in words and "all" in words:
                            if "fire" in words and "fox" in words:
                                os.system("killall firefox")
                                speak("kill all firefox done")
                            bot = False

                        elif "morse" in words and "code" in words:
                                stop_player()
                                morsecode('sati sati sati')

                        elif "wise" in words and "one" in words:
                            if not proc_ck and "play" in words:
                                stop_player()
                                proc = subprocess.Popen(["mpg123","-d","3","-q","--loop","-1","../thaivoices/buddho2.mp3"])
                                proc_ck = True
                                bot = False
                            elif not proc_ck and "real" in words:
                                stop_player()
                                proc = subprocess.Popen(["mpg123","-q","--loop","-1","../thaivoices/samesame.mp3"])
                                proc_ck = True
                                bot = False
                            elif "stop" in words:
                                if proc_ck:
                                    proc.kill()
                                    proc_ck = False
                                bot = False

                        elif "alpha" in words and "meditation" in words:
                            pure_alpha()
                            bot = False

                        elif "chanting" in words and "thai" in words:
                            speak("Thai chanting")
                            proc = subprocess.Popen(["mpg123","-z","--list","THchanting.txt"])        
                            # print("Thai Chanting") 
                            # proc = subprocess.Popen(["vlc","--random","--loop","--playlist-autostart","THchanting.xspf"]) 
                            bot = False
                            motion_detect(proc)
                            clear_q()

                        elif "my" in words and "dhamma" in words:
                            
                            files= get_new_dhamma_files()
                            cmd = "mpg123 -d 1.5 "+files
                            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
                            motion_detect(proc)
                            stop_player()
                            clear_q()

                        elif "who" in words and "buddha" in words:
                            lines = buddhism["buddha"][0]["content"]
                            # print(lines)
                            for i in range(len(lines)):
                                x = int(lines[i]["voice"])
                                # print(voices[x])
                                engine.setProperty('voice',voices[x]) 
                                engine.say(lines[i]["text"])
                                engine.runAndWait()
                                engine.stop()
                            focus_event = ["vlc","-f","--video-on-top","--play-and-exit","../mars/buddha-story.mp4"]
                            focus = True
                            bot = False     

                        elif "show" in words and "face" in words:
                            command = "export DISPLAY=:0.0; python3 ../mars/testgif.py -p ../mars/face.gif"
                            proc = subprocess.Popen(command, shell=True)
                            proc_name = "testgif.py"
                            bot = False
                            proc_ck = True 

                        elif "my" in words and "sun" in words:
                            command = "export DISPLAY=:0.0; python3 testgif.py -p ../sound/sun.gif"
                            proc = subprocess.Popen(command, shell=True)
                            proc_name = "testgif.py"
                            bot = False
                            proc_ck = True 

                        elif "heart" in words and "chanting" in words:
                            speak("play heart sutra with lyrics")
                            stop_player()                
                            try:
                                command = "export DISPLAY=:0.0; vlc -f --loop --video-on-top ../dataen/chanting/heart-sutra.mp4"
                                proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                                bot = False
                                proc_ck = True 
                            except:
                                speak("sorry can not play video clip")

                        elif "the" in words and "sun" in words: 
                            proc = subprocess.Popen(["vlc","--loop","--video-on-top","../sound/sun1.mp4"])
                            # proc = subprocess.Popen(["mplayer","-fs","-loop","0","../mars/sun.mp4"])
                            bot = False
                            proc_ck = True

                        elif "the" in words and "water" in words: 
                            proc = subprocess.Popen(["vlc","--loop","-f","--video-on-top","../mars/water-droplets.mp4"])
                            # proc = subprocess.Popen(["mplayer","-fs","-loop","0","../mars/sun.mp4"])
                            bot = False
                            proc_ck = True

                        elif "blooming" in words and "flower" in words: 
                            proc = subprocess.Popen(["vlc","-f","--stop-time","154.1","--loop","--video-on-top","../sound/BloomingFlowers.mp4"])
                            # proc = subprocess.Popen(["mplayer","-fs","-loop","0","../sound/BloomingFlowers.mp4"])
                            bot = False
                            proc_ck = True
                            
                        elif "play" in words and ("sermons" in words or "dhamma" in words):
                            speak("play Thai dhamma")
                            proc = subprocess.Popen(["mpg123","-z","--list","THdhamma4all.txt"])
                            # print("play daily sermons") 
                            # proc = subprocess.Popen(["vlc","--random","--loop","--playlist-autostart","THdhamma.xspf"])
                            bot = False
                            motion_detect(proc)
                            clear_q()
                        elif "meditation" in words and ("start" in words or "begin" in words or "time" in words):
                            print("start meditation bell ring every 15 minutes") 
                            proc = subprocess.Popen(["vlc","--loop","../dataen/bell15min.mp3"])
                            bot = False
                        elif "stop" in words and "play" in words:
                            if proc_ck:
                                proc.kill()
                                proc_ck = False
                                speak("kill the process")
                            if len(proc_name) > 0:
                                os.system("pkill -f " + proc_name)
                                speak("kill " + proc_name)
                                proc_name = ''
                            stop_player()
                            speak("done")
                            bot = False
                        elif "quiet" in words or "silent" in words or "sleep" in words:
                            speak("ok")
                            print("stop listening")
                            bot = False
                        elif "volume" in words and "up" in words:
                            call(["amixer","-D","pulse","sset","Master","90%"])
                            bot = False
                            engine.say("set volume to 90%")
                            engine.runAndWait()
                            engine.stop()
                        elif "volume" in words and "down" in words:
                            call(["amixer","-D","pulse","sset","Master","50%"])
                            bot = False
                            engine.say("set volume to 50%")
                            engine.runAndWait()
                            engine.stop()
                        elif "volume" in words and "sixty" in words:
                            call(["amixer","-D","pulse","sset","Master","60%"])
                            bot = False
                            engine.say("set volume to 60%")
                            engine.runAndWait()
                            engine.stop()
                        elif "volume" in words and "seventy" in words:
                            call(["amixer","-D","pulse","sset","Master","70%"])
                            bot = False
                            engine.say("set volume to 70%")
                            engine.runAndWait()
                            engine.stop()
                        elif "volume" in words and "eighty" in words:
                            call(["amixer","-D","pulse","sset","Master","80%"])
                            bot = False
                            engine.say("set volume to 80%")
                            engine.runAndWait()
                            engine.stop()
                        elif "buddha" in words and "holy" in words and "day" in words: #easy version haha
                            y = list(str(holyday))
                            yy = y[2]+y[3]+y[4]+y[5]
                            mm = y[6]+y[7]
                            dd = y[8]+y[9]
                            # print(yy,mm,dd)
                            import datetime
                            x = datetime.datetime(int(yy),int(mm),int(dd))
                            z = x.strftime("%B %A %d")
                            print(holyday[0])
                            engine.say(z)
                            engine.runAndWait()
                            engine.stop()
                            bot = False
                        elif "what" in words and "time" in words:
                            today = datetime.today().strftime('%H %M')
                            print(today)
                            engine.say(today)
                            engine.runAndWait()
                            engine.stop()
                            bot = False
                        elif "what" in words and "day" in words:
                            today = datetime.today().strftime('%B %A %d')
                            print(today)
                            engine.say(today)
                            engine.runAndWait()
                            engine.stop()
                            bot = False
                        elif "zen" in words and "story" in words:
                            nn = sequence[n]                                         
                            speak(d["zen101"][nn]["title"])
                            lines = d["zen101"][nn]["story"]
                            # print(lines)
                            for i in range(len(lines)):
                                x = int(lines[i]["voice"])
                                engine.setProperty('voice',voices[x]) 
                                speak(lines[i]["text"])
                            n = n + 1
                            engine.setProperty('voice',voices[2]) 
                            bot = False
                        elif "play" in words and "sutra" in words:
                            i = random.randint(0,1)
                            lines = sutta["sutta"][i]["content"]
                            # print(lines)
                            for i in range(len(lines)):
                                x = int(lines[i]["voice"])
                                # print(voices[x])
                                engine.setProperty('voice',voices[x]) 
                                engine.say(lines[i]["text"])
                                engine.runAndWait()
                                engine.stop()
                                engine.setProperty('voice',voices[2]) 
                                bot = False
                        elif "shutdown" in words and "now" in words:
                            # print("Shutdown the system")
                            engine.say("The system is Shutting down")
                            engine.runAndWait()
                            engine.stop()
                            os.system("shutdown now")
                            break

                        elif "open" in words and "sky" in words:
                            speak("open stellarium - A real-time realistic planetarium ")
                            command = "stellarium"
                            subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                            screenWidth, screenHeight = pyautogui.size()
                            pyautogui.moveTo(int(screenWidth/2), int(screenHeight/2))
                            bot = False
                        elif "close" in words and "sky" in words:
                            if find_name('stellarium'):
                                speak("Quit stellarium")
                                os.system("pkill -f stellarium")
                            bot = False

                        elif "browse" in words and "meditation" in words and "technique" in words:
                            speak("open Meditation technique on youtube")
                            command = "firefox -safe-mode https://www.youtube.com/playlist?list=PLUh8U5np7D-7FMh6ONGwnaltFppPBwTVI"
                            subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                            screenWidth, screenHeight = pyautogui.size()
                            pyautogui.moveTo(int(screenWidth*5/8), int(screenHeight*19/32))
                            bot = False

                        elif "open" in words and "fire" in words and "fox" in words:
                            speak("open firefox web browser")
                            command = "firefox -safe-mode https://free.facebook.com/"
                            subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                            screenWidth, screenHeight = pyautogui.size()
                            pyautogui.moveTo(int(screenWidth*5/8), int(screenHeight*19/32))
                            bot = False
                        elif "close" in words and "fire" in words and "fox" in words:
                            if find_name('firefox'):
                                os.system("pkill -f firefox")
                            bot = False
                        elif "buddha" in words and "mantra" in words:
                            speak("buddho mantra")
                            proc = subprocess.Popen(["mpg123","-d","3","-q","--loop","-1","../thaivoices/buddho.mp3"])
                            motion_detect(proc)
                            bot=False
                        #MOUSE CONTROL https://pypi.org/project/PyAutoGUI/
                        elif "mouse" in words and "center" in words:
                            screenWidth, screenHeight = pyautogui.size()
                            pyautogui.moveTo(int(screenWidth/2), int(screenHeight/2))
                        elif "mouse" in words and "up" in words:
                            pyautogui.move(0, -23)
                        elif "mouse" in words and "down" in words:
                            pyautogui.move(0, 25)
                        elif "mouse" in words and "left" in words:
                            pyautogui.move(-52, 0)
                        elif "mouse" in words and "right" in words:
                            pyautogui.move(50, 0)
                        elif "scroll" in words  or "page" in words and "up" in words:
                            pyautogui.scroll(5)
                            for s in range(5):
                                pyautogui.scroll(1)
                                time.sleep(0.5)
                        elif "scroll" in words or "page" in words and "down" in words:
                            # pyautogui.scroll(-7)
                            for s in range(7):
                                pyautogui.scroll(-1)
                                time.sleep(0.5)
                        elif "mouse" in words and "click" in words:
                            pyautogui.click(button='left')
                        elif "mouse" in words and "exit" in words:
                            speak("stop mouse control")
                            bot = False
                        elif "speak" in words:
                            listToStr = ' '.join(map(str, words))
                            listToStr = listToStr.replace("speak",'')
                            speak("You said, " + listToStr)
                            time.sleep(3)
                            with q.mutex:
                                q.queue.clear()
                            
            else:
                pass
                # if not bot:
                #     x = rec.PartialResult()
                #     print(x)
                # else:
                #     pass

except KeyboardInterrupt:
    print('\nDone')
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))


# JUST TEST
