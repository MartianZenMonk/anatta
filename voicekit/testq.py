#!/usr/bin/env python3

import argparse
import os
import queue
import sounddevice as sd
import vosk
import sys
import json
import random
import pty
import gc
import time
import csv
import socket
import cv2
import psutil
import subprocess
from subprocess import call
import datetime as dt
from datetime import datetime
from aiy.board import Board, Led
from aiy.leds import (Leds, Pattern, PrivacyLed, RgbLeds, Color)

# sd._terminate()
# time.sleep(5)
# sd._initialize()
# sd.default.latency = 'low'

import pyttsx3
engine = pyttsx3.init() # object creation
engine.setProperty('voice','english-us') 
engine.setProperty('rate', 125)
engine.setProperty('volume',0.1)


def speak(text):
        print(text)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        return None


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


try:
    import httplib
except:
    import http.client as httplib

def have_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False


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
word += ["eleven","twelve","thirteen","forteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
number = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

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


# flite Voices available: kal awb_time kal16 awb rms slt  
def speakf(v,t,*args):
        os.system('flite -voice ' + v + ' -t "' + str(t) + '"')
        return None

voices = ["kal", "slt", "rms", "awb", "awb_time", "kal16"]


q = queue.Queue()

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
    if q.qsize() > 15:
        with q.mutex:
            q.queue.clear()
    else:
        q.put(bytes(indata)) 


def clear_q():
    time.sleep(1)
    with q.mutex:
        q.queue.clear()

# see leds_example.py

def ledc(c='', f='alpha'):
    Color.ORANGE = (100, 5, 0)
    # print('Set blink pattern: period=500ms (2Hz)')
    if f == 'alpha':
        leds.pattern = Pattern.blink(100) # Alpha 10 Hz
    else:
        leds.pattern = Pattern.blink(500) # Delta 2 Hz

    if c == 'r':
        leds.update(Leds.rgb_on(Color.RED))
    elif c == 'rr':
        leds.update(Leds.rgb_pattern(Color.RED))

    elif c == 'g':
        leds.update(Leds.rgb_on(Color.GREEN))
    elif c == "gg":
        leds.update(Leds.rgb_pattern(Color.GREEN))

    elif c == 'b':
        leds.update(Leds.rgb_on(Color.BLUE))
    elif c == 'bb':
        leds.update(Leds.rgb_pattern(Color.BLUE))

    elif c == 'y':
        leds.update(Leds.rgb_on(Color.YELLOW))
    elif c == 'yy':
        leds.update(Leds.rgb_pattern(Color.YELLOW))

    elif c == 'p':
        leds.update(Leds.rgb_on(Color.PURPLE))     
    elif c == 'pp':
        leds.update(Leds.rgb_pattern(Color.PURPLE))

    elif c == 'c':
        leds.update(Leds.rgb_on(Color.CYAN))
    elif c == 'cc':
        leds.update(Leds.rgb_pattern(Color.CYAN))

    elif c == 'd':
        # dark or black = rgb(0,0,0)
        leds.update(Leds.rgb_on(Color.BLACK))
    elif c == 'dd':
        leds.update(Leds.rgb_pattern(Color.BLACK))
    elif c == 'o':
        leds.update(Leds.rgb_on(Color.ORANGE))
    elif c == 'oo':
        leds.update(Leds.rgb_pattern(Color.ORANGE))
    elif c == 'off':
        board.led.state = Led.OFF

    else:
        leds.update(Leds.rgb_on(Color.WHITE))

    return None


def killPlayer():
    if find_name('mpg123'):
        os.system("killall mpg123")
    if find_name('vlc'):
        os.system("killall vlc")
    return None


def pkill_proc_name(name=''):
    global proc_name
    if name == '':
        pass
    else:
        proc_name = name

    if len(proc_name) > 0:
        os.system("pkill -f " + proc_name)
        proc_name = ''
        # espeak("kill " + proc_name,'4')
        
    return None


def delay(t):
    board.button.wait_for_press(60*t)
    return None


def press_for_stop(c='',proc=0,t=0):
    ledc(c)
    if t == 0 :
        board.button.wait_for_press()
    else:
        board.button.wait_for_press(60*t)
    proc.kill()
    pkill_proc_name()
    killPlayer()
    with q.mutex:
        q.queue.clear()
    return None


def get_help():
    text =  '''
            You have to start with words anat ta,
            and then you can say,
            repeat (mode) on off,
            daily dependent origination,
            buddha thinking,
            nature truth chanting,
            breathing chanting,
            dependent origination chanting,
            8 fold path Thai, 8 fold path English,
            English chanting, Thai chanting,
            meditaion time, play radio, 
            mantra 1 2 3 4 5 6 or 10 15 20 30 40 50 minutes,
            play 1 3 6 stage,
            buddha dhamma, play dhamma, play sutra, my dhamma
            what time, what day, buddha day, zen story,
            red green blue yellow or sound and or alpha light on,
            pure or breathing alpha meditation,
            math meditation,
            walking practice,
            sitting practice,
            moring practice,
            wise one or alpha,
            please shutdown or anat ta stop,
            '''
    speak(text)
    time.sleep(3)
    with q.mutex:
        q.queue.clear()
    return None


def shutdown():
    os.system("mpg123 -f 1000 ../thaivoices/dead.mp3")
    espeak("The system is shutting down, wait until the green light in the box turn off",'10')
    board.led.state = Led.OFF
    os.system("sudo shutdown now")
    return None


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

#TEST
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
        thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
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
            if w*h > 200000:
                bk = True

        # Appending status of motion
        motion_list.append(motion)

        if bk:
            break

        #cv2.imshow("Gray Frame", gray)
        #cv2.imshow("Difference Frame", diff_frame)
        #cv2.imshow("Threshold Frame", thresh_frame)
        # cv2.imshow("Color Frame", frame)
        # key = cv2.waitKey(1)
        # if q entered whole process will stop
        # if key == ord('q'):
        #     break

    proc.kill()
    video.release()
    # Destroying all the windows
    # cv2.destroyAllWindows()
        
    return None


def speakThai(text):
    stext = ""
    for i in range(len(text)):
        stext += " ../thaivoices/thwords/" + text[i] + ".mp3"
    os.system('mpg123 -d 2 -f 2000 ' + stext)


def enwords(text):
    stext = ""
    for i in range(len(text)):
        stext += " ../dataen/" + text[i] + ".mp3"
    return stext


def thwords(text):
    stext = ""
    for i in range(len(text)):
        stext += " ../thaivoices/thwords/" + text[i] + ".mp3"
    return stext


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


def buddha_day():
    with open('myhora-buddha-2564.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    day = datetime.today().strftime('%Y%m%d')
    holyday = []
    thholyday = []

    for i in range(len(data)):
        if i > 0:
            if(int(data[i][1]) > int(day)):
                holyday.append(data[i][1])
                thholyday.append(data[i][0])
    t = thholyday[0].replace("(", " ")
    x = t.split()
    
    bdaytext = ""
    for i in range(len(x)-1):
      bdaytext += " ../thaivoices/thwords/" + x[i] + ".mp3"

    if have_internet():
        today = dt.datetime.now()
        z = today.strftime("%B %A %d %H %M")
        speak("Today is" + z)
        t = "วันนี้,วัน,weekday/%w,ที่,59/%d,เดือน,month/%m,เวลา,59/%H,นาฬิกา,59/%M,นาที"
        t = t.replace("%w",today.strftime('%w'))
        t = t.replace("%d",today.strftime('%d'))
        t = t.replace("%m",today.strftime('%m'))
        t = t.replace("%H",today.strftime('%H'))
        t = t.replace("%M",today.strftime('%M'))
        text = t.split(',')
        stext = ""
        for i in range(len(text)):
                stext += " ../thaivoices/thwords/" + text[i] + ".mp3"
        os.system("mpg123 -q -f 2100 "+stext)

    y = list(str(holyday))
    yy = y[2]+y[3]+y[4]+y[5]
    mm = y[6]+y[7]
    dd = y[8]+y[9]
    x = dt.datetime(int(yy), int(mm), int(dd))
    z = x.strftime("%B %A %d")
    speak("next Buddha holy day is " + z)
    t = "วันพระ,หน้า,คือ,วัน,weekday/%w,ที่,59/%d,เดือน,month/%m"
    t = t.replace("%w",x.strftime('%w'))
    t = t.replace("%d",x.strftime('%d'))
    t = t.replace("%m",x.strftime('%m'))
    text = t.split(',')
    stext = ""
    for i in range(len(text)):
            stext += " ../thaivoices/thwords/" + text[i] + ".mp3" 
    os.system("mpg123 -q -f 2100 "+stext) 
    os.system("mpg123 -q -f 2100 "+bdaytext) 
    del data
    del stext
    del bdaytext
    del t
    del text
    gc.collect()
    return None


def fast_buddho(c='off', t=30, vol='2000'):

    ledc(c)

    if t==0:
        proc = subprocess.Popen(["mpg123","-d","3","-f",vol,"-q","--loop","-1","../thaivoices/buddho.mp3"])
        press_for_stop(c,proc)
    else:
        proc = subprocess.Popen(["mpg123","-d","3","-f",vol,"-q","--loop","-1","../thaivoices/buddho.mp3"])
        delay(t)
        proc.kill()
        clear_q()
   
    return None


def bell(l='3',vol='500'):
    subprocess.run(["mpg123","-q","-f",vol,"--loop",l,"../dataen/bell.mp3"])
    return None


def relax_thai(vol="500"):

    text  = ["ทำ","ตัว","ผ่อน","คลาย","หาย","ใจ","ยาว","ยาว","คลาย","ความ","กังวล","ตั้ง","จิต","มั่น","รู้","ลม","หาย","ใจ"]
    text += ["เข้า","ออก","สั้น","ยาว","หยาบ","ละเอียด","เกิด","ดับ","ไม่","เที่ยง","หนอ","แล"]
    text += ["ไม่","มี","ทุกข์","ไม่","มี","สุข","มี","แต่","ความ","ที่","สติ","เป็น","ธรรมชาติ","บริสุทธิ์","เพราะ","อุเบกขา","แล้ว","แล","อยู่"]
    stext = thwords(text)
    # print(stext)
    os.system("mpg123 -q -f " + vol + " " + stext)
    del stext
    gc.collect()
    return None


def pure_alpha(c='yy'):
    ledc(c)
    speak("pure alpha sound, push button for stop")
    os.system("mpg123 -f 1000 ../thaivoices/right_concentation.mp3")
    proc = subprocess.Popen(["mpg123","-q","--loop","-1","../mars/pureAlpha1hr.mp3"])
    press_for_stop(c,proc)
    return None


def alpha_wave(t):
    proc = subprocess.Popen(["mpg123","-q","--loop","-1","../sound/pureAlpha.mp3"])
    delay(t)
    proc.kill()
    clear_q()
    return None


#BHAVANA
def remind_breathing(t=30,vol='500'):
    bell('3',vol)
    text = ["หาย","ใจ","เข้า","พุท","หาย","ใจ","ออก","โธ"]
    tx   = thwords(text)
    timeout = time.time() + 60*t   
    while True:
        if time.time() > timeout:
            break
        else:
            os.system("mpg123 -f "+ vol + " " + tx)
    bell('1',vol)
    clear_q()
    return None


def remind_relax(t=30,vol='500'):
    bell('3',vol)
    text  = ["ทำ","ตัว","ผ่อน","คลาย","หาย","ใจ","ยาว","ยาว","คลาย","ความ","กังวล","ตั้ง","จิต","มั่น","รู้","ลม","หาย","ใจ"]
    text += ["เข้า","ออก","สั้น","ยาว","หยาบ","ละเอียด","เกิด","ดับ","ไม่","เที่ยง","หนอ"]
    tx   = thwords(text)
    timeout = time.time() + 60*t   
    while True:
        if time.time() > timeout:
            break
        else:
            os.system("mpg123 -f "+ vol + " " + tx)
    bell('1',vol)
    clear_q()
    return None


def loop_sati(t=30,vol='500'):
    bell('3',vol)
    os.system('mpg123 -f ' + vol + ' -loop -1 ')
    proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../thaivoices/sati-cut.mp3"])
    delay(t)
    proc.kill()
    bell('1',vol)
    clear_q()
    return None


def wise_one(c='off',vol="500"):
    proc = subprocess.Popen(["mpg123","-d","3","-f",vol,"-q","--loop","-1","../thaivoices/buddho.mp3"])
    press_for_stop(c,proc)
    return None


def breathing_alpha_meditation(c='g',t=30):

    vol = "500"
    speak(str(t) + " minutes alpha sound")

    
    relax_thai()

    bell('3',vol)

    if len(c) == 1:
        ledc(c+c)
    else:
        ledc(c)

    alpha_wave(t)

    bell('1',vol)
    clear_q()
    return None


def alpha_meditation(m=60,t=15,c='off',vol="500"):


    speak(str(m) + " minutes alpha sound")
    if t > 0:
        speak("and "+ str(t) + " minutes bell sound")

    bell('3',vol)

    if len(c) == 1:
        ledc(c+c)
    else:
        ledc(c)

    if t == 0:
        t = m
        alpha_wave(t)
        bell('1',vol)
    else:
        timeout = time.time() + 60*m
        while True:
        
            if time.time() > timeout:
                break
            else:
                alpha_wave(t)
                bell('1',vol)

    bell('1',vol)
    clear_q()
    return None


def slow_buddho(c='',t=30,vol='1000'):
    ledc(c)
    th_stand = thwords(["ยืน","หนอ"])
    for i in range(3):
        os.system('mpg123 -f ' + vol + ' ' + th_stand)
        time.sleep(1)

    del th_stand
    gc.collect()

    if t==0:
        proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../thaivoices/buddho0.mp3"])
        press_for_stop(c,proc)
    else:
        proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../thaivoices/buddho0.mp3"])
        delay(t)
        proc.kill()
    
    return None


def slow_buddho2(c='',t=30,vol='1000'):
    ledc(c)

    if t==0:
        proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../thaivoices/buddho1.mp3"])
        press_for_stop(c,proc)
    else:
        proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../thaivoices/buddho1.mp3"])
        delay(t)
        proc.kill()
    
    return None


def one_stage_en(c='',t=5):
    ledc(c)
    for i in range(3):
        speak("standing")
        time.sleep(1)
    proc = subprocess.Popen(["mpg123","-f","1000","-q","--loop","-1","../dataen/one_stage.mp3"])
    delay(t)
    proc.kill()
    return None

def one_stage_th_en(c='',t=5):

    th_right = thwords(['ขวา','ย่าง','หนอ'])
    th_left = thwords(['ซ้าย','ย่าง','หนอ'])
    th_stand = thwords(["ยืน","หนอ"])
    en_right = enwords(['right','goes','thus'])
    en_left = enwords(['left','goes','thus'])
    
    ledc(c)
    for i in range(3):
        os.system('mpg123 -f 2000 ' + th_stand)
        time.sleep(1)
        speak("standing")
        time.sleep(1)
    timeout = time.time() + 60*t
    while True:
        
        if time.time() > timeout:
            break
        else:
            os.system('mpg123 -f 2000 ' + th_right)
            time.sleep(1)
            os.system('mpg123 -f 2000 ' + th_left)
            time.sleep(1)

            os.system('mpg123 -f 2000 ' + en_right)
            time.sleep(1)
            os.system('mpg123 -f 2000 ' + en_left)
            time.sleep(1)

    del th_left
    del th_right
    del th_stand
    del en_left
    del en_right
    gc.collect()

    return None


def three_stages_th_en(c='',t=5):
    killPlayer()    
    speak(str(t) + " minutes 3 stages walking practice")
    th_stage = thwords(["ยกหนอ","ย่างหนอ","เหยียบหนอ"])
    th_stand = thwords(["ยืน","หนอ"])
    en_stage = enwords(['lifting','moving','treading'])
    ledc(c)
    for i in range(3):
        os.system('mpg123 -f 2000 ' + th_stand)
        time.sleep(1)
        speak("standing")
        time.sleep(1)
    timeout = time.time() + 60*t
    while True:
        
        if time.time() > timeout:
            break
        else:
            os.system('mpg123 -f 2000 ' + th_stage)
            time.sleep(1)
            os.system('mpg123 -f 2000 ' + en_stage)
            time.sleep(1)

            os.system('mpg123 -f 2000 ' + th_stage)
            time.sleep(1)
            os.system('mpg123 -f 2000 ' + en_stage)
            time.sleep(1)

    del th_stage
    del th_stand
    del en_stage
    gc.collect() 

    return None


def six_stages_th_en(c='',t=5):

    killPlayer()   
    speak(str(t) + " minutes 6 stages walking practice")
    th_stand = thwords(["ยืน","หนอ"])
    th_stage = thwords(["ยกส้นหนอ","ยกหนอ","ย่างหนอ","ลงหนอ","ถูกหนอ","กดหนอ"])
    en_stage = enwords(["heelup","lifting","moving","lowering","touching","pressing"])
    ledc(c)
    for i in range(3):
        os.system('mpg123 -f 2000 ' + th_stand)
        time.sleep(1)
        speak("standing")
        time.sleep(1)
    timeout = time.time() + 60*t
    
    while True:
        
        if time.time() > timeout:
            break
        else:
            os.system('mpg123 -f 2000 ' + th_stage)
            time.sleep(1)
            os.system('mpg123 -f 2000 ' + en_stage)
            time.sleep(1)

            os.system('mpg123 -f 2000 ' + th_stage)
            time.sleep(1)
            os.system('mpg123 -f 2000 ' + en_stage)
            time.sleep(1)

    del th_stage
    del th_stand
    del en_stage
    gc.collect() 

    return None

def read_sutta(d):
    speak(d["title"])
    lines = d["content"]
    # print(lines)
    for i in range(len(lines)):
        x = int(lines[i]["voice"])
        engine.setProperty('voice',es_voices[x]) 
        speak(lines[i]["text"])
    engine.setProperty('voice',es_voices[2])
    clear_q()
    return None

def meditation_goal(vol='2000'):
    text = " ../thaivoices/dukkha.mp3 ../thaivoices/goal.mp3"
    os.system("mpg123 -q -f " + vol + text)

def meditation_goal2(vol='2000'):
    text = " ../thaivoices/howtopractice.mp3"
    os.system("mpg123 -q -f " + vol + text)

def meditation_goal3(vol='2000'):
    text = " ../thaivoices/natureTruth3.mp3"
    os.system("mpg123 -q -f " + vol + text)

def meditation_goal4(vol='2000'):
    text = " ../thaivoices/circle_of_dukkha_thai.mp3"
    os.system("mpg123 -q -f " + vol + text)

def yoniso(vol='2000'):
    text = " ../thaivoices/yoniso_thai.mp3"
    os.system("mpg123 -q -f " + vol + text)


def walking_reward():
    read_sutta(sutta["sutta"][0]) 
    return None


def remind_sati():
    speak("Do not forget to mind your breathing, mind your body movement and mind your mind.")
    text = " ../thaivoices/sati.mp3"
    os.system("mpg123 -q -f 2000 "+text)


def remind_sati_bikkhu():
    entext = """
            Come you, monk, have mindfulness and situational awareness. Act with situational awareness 
            when going out and coming back; when looking ahead and aside; when bending and extending the limbs; 
            when bearing the outer robe, bowl and robes; when eating, drinking, chewing, and tasting; 
            when urinating and defecating; when walking, standing, sitting, sleeping, waking, speaking, and keeping silent.
            """
    speak(entext)
    text = " ../thaivoices/sati_bikkhu.mp3"
    os.system("mpg123 -q -f 2000 "+text)


def remind_right_sati():
    speak("Ardent, fully aware, and mindful, after removing avarice and sorrow regarding the world.")
    text = " ../thaivoices/right_sati.mp3"
    os.system("mpg123 -q -f 2000 "+text)


def remind_dead():
    text = " ../thaivoices/dead.mp3"
    os.system("mpg123 -q -f 2000 "+text)


def mixed_mode(c='',t=10,n=0):

    if n == 1:
        one_stage_en(c,t)
    elif n == 2:
        three_stages_th_en(c,t)
    elif n == 3:
        six_stages_th_en(c,t)
    else:
        one_stage_th_en(c,t)

    return None


def get_new_dhamma_files():
    new_files = []
    for file in os.listdir("../mars/dhamma"):
        if file.endswith(".mp3"):
            new_files.append(os.path.join("../mars/dhamma", file))

    # print(new_files)
    random.shuffle(new_files)
    newfiles = " + ".join(str(x) for x in new_files) 
    # print(newfiles)
    del new_files
    gc.collect()
    return newfiles


def play_my_dhamma():
    files= get_new_dhamma_files()
    cmd = "mpg123 -C -d 1.5 -f 2000 "+files
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, stdin=master)
    leds.update(Leds.rgb_on(Color.YELLOW))
    board.button.wait_for_press()
    os.write(slave, b'f')
    leds.update(Leds.rgb_on(Color.GREEN))
    board.button.wait_for_press()
    os.write(slave, b'f')
    press_for_stop('g',proc)
    killPlayer()    
    del files
    gc.collect() 
    return None


# Features
def what_time():
    today = datetime.today().strftime('%H %M')
    speak("The time is " + today)


def what_day():
    today = datetime.today().strftime('%B %A %d')
    speak("Today is " + today)
    today = dt.datetime.now() 
    # text = ["วันนี้","วัน","weekday/%w","ที่","59/%d","เดือน","month/%m","เวลา","59/%H","นาฬิกา","59/%M","นาที"]
    t = "วันนี้,วัน,weekday/%w,ที่,59/%d,เดือน,month/%m,เวลา,59/%H,นาฬิกา,59/%M,นาที"
    t = t.replace("%w",today.strftime('%w'))
    t = t.replace("%d",today.strftime('%d'))
    t = t.replace("%m",today.strftime('%m'))
    t = t.replace("%H",today.strftime('%H'))
    t = t.replace("%M",today.strftime('%M'))
    text = t.split(',')
    stext = ""
    for i in range(len(text)):
            stext += " ../thaivoices/thwords/" + text[i] + ".mp3"
    os.system("mpg123 -q -f 2100 "+stext)
    del t
    del text
    del stext
    gc.collect()


def play_daily_dependent_origination_thai():
    killPlayer()  
    speak("Dependent Origination Application in Everyday Life in Thai")
    proc = subprocess.Popen(["mpg123","-f","2000","../datath/buddhadham/paticcasamuppda.mp3"])
    press_for_stop('g',proc)


def play_buddha_thinking_thai():
    killPlayer()
    os.system("mpg123 -f 2000 -q ../thaivoices/yoniso_thai.mp3")
    speak("Thai Buddhadham Yonisomanasikan")
    proc = subprocess.Popen(["mpg123","-f","2000","../datath/buddhadham/yoniso.mp3"])
    press_for_stop('g',proc)


def play_breathing_chanting_thai():
    killPlayer()
    if "loop" in words:
        speak("Thai Anapanasati chanting")
        proc = subprocess.Popen(["mpg123","-f","2000","-C","--loop","-1","../datath/chanting/anapanasati-cut.mp3"], stdin=master)
        press_for_stop('g',proc)
    else:
        subprocess.run(["mpg123","-f","2000","../datath/chanting/anapanasati-cut.mp3"])


def play_nature_truth_chanting_thai():
    killPlayer()
    speak("Thai Dhamma Ni yam chanting")
    proc = subprocess.Popen(["mpg123","-f","2000","-C","--loop","-1","../datath/chanting/dhammaniyam.mp3"], stdin=master)
    motion_detect(proc)


def play_dependent_origination_chanting_thai():
    killPlayer()  
    speak("Thai Itup paj ja ya ta Pa tij ja sa mup path chanting")
    proc = subprocess.Popen(["mpg123","-f","2000","-C","--loop","-1","../datath/chanting/ituppajjayata.mp3"], stdin=master)
    press_for_stop('g',proc)

def play_eight_fold_path_chanting_thai(vol="2000"):
    killPlayer()   
    # speak("Thai Noble 8 fold path chanting")
    proc = subprocess.Popen(["mpg123","-f",vol,"-C","--loop","-1","../datath/chanting/8.mp3"], stdin=master)
    press_for_stop('off',proc)


def play_eight_fold_path_chanting_english():
    killPlayer()   
    speak("English Noble 8 fold path chanting")
    proc = subprocess.Popen(["mpg123","-f","4000","-C","--loop","-1","../dataen/chanting/noble8fold.mp3"], stdin=master)
    press_for_stop('g',proc)


def play_8_fold_path_clip():
    killPlayer() 
    try:
        command = "export DISPLAY=:0.0; vlc -f --loop --video-on-top ../mars/8.mp4"
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        press_for_stop('d',proc)      
    except:
        speak("sorry can not play video clip")


def play_dependent_origination_clip():
    killPlayer() 
    try:
        command = "export DISPLAY=:0.0; vlc -f --loop --video-on-top ../mars/11.mp4"
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        press_for_stop('d',proc)      
    except:
        speak("sorry can not play video clip")


def english_chating():
    killPlayer()  
    speak("English chanting")
    subprocess.run(["mpg123","-f","1500","-C","--list","chanting.txt"])


def thai_chanting():
    killPlayer()   
    speak("Thai chanting")
    proc = subprocess.Popen(["mpg123","-f","1500","-C","-Z","--list","THchanting.txt"], stdin=master)
    press_for_stop('g',proc)


def play_radio():
    killPlayer()                                    
    if have_internet():
        speak("Tibetan Buddhist internet radio")
        proc = subprocess.Popen(["mpg123","-f","2000","-q","http://199.180.72.2:9097/lamrim"])
        press_for_stop('g',proc)
    else:
        speak("sorry no internet connection")  


def meditation_time():
    killPlayer()   
    text = """
            Meditation time will make 15 minutes bell sound, you may relax your self by walking then sitting. 
            For walking, set a distance to meditate walking back and forth, your senses inwardly immersed, your mind not straying outwards. 
            Lifting, Moving, Treading, slow moving and always mind your foot movement then you can increse your awakening sense, 
            or free walking, just focus on Treading, "
            For sitting, breathing in calm, breathing out down, always mind your breathing, your citta will not go around
            """
    speak(text)
    del text
    gc.collect()
    proc = subprocess.Popen(["mpg123","-f","1500","-q","--loop","-1","../dataen/bell15min.mp3"])
    press_for_stop('g',proc)


def buddha_dhamma():
    killPlayer()    
    speak("Buddha dhamma")
    proc = subprocess.Popen(["mpg123","-f","1500","-q","-z","--list","THbuddhadham.txt"]) 
    press_for_stop('b',proc)


def play_dhamma():
    killPlayer()   
    speakThai(['ฟัง','ธรรม','ค่ะ'])
    proc = subprocess.Popen(["mpg123","-f","1500","-C","-z","--list","THdhamma4all.txt"], stdin=master)
    leds.update(Leds.rgb_on(Color.YELLOW))
    board.button.wait_for_press()
    os.write(slave, b'f')
    leds.update(Leds.rgb_on(Color.RED))
    board.button.wait_for_press()
    os.write(slave, b'f')
    press_for_stop('g',proc)


def play_sutra(vol="1000"):
    killPlayer()    
    proc1 = subprocess.Popen(["mpg123","-f",vol,"../datath/sutta/moggallana.mp3"])
    delay(15)
    proc1.kill()
    proc2 = subprocess.Popen(["mpg123","-f",vol,"-C","-z","--list","sutra.txt"], stdin=master)
    press_for_stop('d',proc2)


def walking_meditation_count(c='yy'):
    
    speak("one stage walking practice, please count your step then you can verify it in the end")

    th_right = thwords(['ขวา','ย่าง','หนอ'])
    th_left = thwords(['ซ้าย','ย่าง','หนอ'])
    th_stand = thwords(["ยืน","หนอ"])
    en_right = enwords(['right','goes','thus'])
    en_left = enwords(['left','goes','thus'])
    
    ledc(c)
    for i in range(3):
        os.system('mpg123 -f 2000 ' + th_stand)
        time.sleep(1)
        speak("standing")
        time.sleep(1)

    bell()
    count = 0
    t = random.randint(5,10)
    timeout = time.time() + 60*t
    while True:
        
        if time.time() > timeout:
            break
        else:
            t1 = random.randint(1,2)
            t2 = random.randint(1,2)
            os.system('mpg123 -f 2000 ' + th_right)
            time.sleep(t1)
            os.system('mpg123 -f 2000 ' + th_left)
            time.sleep(t2)

            os.system('mpg123 -f 2000 ' + en_right)
            time.sleep(t2)
            os.system('mpg123 -f 2000 ' + en_left)
            time.sleep(t1)

            count +=1

    bell('1')
    speak("you walk for " + str(count*4) + "steps")

    del th_left
    del th_right
    del th_stand
    del en_left
    del en_right
    gc.collect()

    return None


def heart_sutra(t=0,c='d',vol="6000"):
    ledc(c)
    if t == 0:
        proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../dataen/chanting/heart-sutra.mp3"])
        press_for_stop(c,proc)
    else:
        proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../dataen/chanting/heart-sutra.mp3"])
        delay(t)
        proc.kill()
        clear_q()
    return None


def raining_meditation(t=0,c='d',vol="6000"):
    ledc(c)
    if t == 0:
        proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../sound/rainymood.mp3"])
        press_for_stop(c,proc)
    else:
        proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../sound/rainymood.mp3"])
        delay(t)
        proc.kill()
        clear_q()
    return None


def thunder_meditation(t=0,c='d',vol="6000"):
    ledc(c)
    if t == 0:
        proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../sound/thunderstorm.mp3"])
        press_for_stop(c,proc)
    else:
        proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../sound/thunderstorm.mp3"])
        delay(t)
        proc.kill()
        clear_q()
    return None


def jungle_meditation(t=0,c='d',vol="6000"):
    ledc(c)
    if t == 0:
        proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../sound/jungle.mp3"])
        press_for_stop(c,proc)
    else:
        proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../sound/jungle.mp3"])
        delay(t)
        proc.kill()
        clear_q()
    return None


def tibetan_meditation(t=0,c='d',vol="6000"):
    ledc(c)
    if t == 0:
        proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../sound/tibetan.mp3"])
        press_for_stop(c,proc)
    else:
        proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../sound/tibetan.mp3"])
        delay(t)
        proc.kill()
        clear_q()
    return None


def om_meditation(t=0,c='d',vol="6000"):
    ledc(c)
    if t == 0:
        proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../sound/OM417Hz.mp3"])
        press_for_stop(c,proc)
    else:
        proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../sound/OM417Hz.mp3"])
        delay(t)
        proc.kill()
        clear_q()
    return None

# FOR MARTIAN MONK ONLY
def play_plants(w):
    plants = ['cells.mp4','light-sd.mp4','seed-sd.mp4','water-sd.mp4','co2.mp4','npk.mp4']
    plists = ['cell','light','seed','water','carbon','food']           
    try:
        i = plists.index(w)
        speak("Play Plants " + w)
        command = "export DISPLAY=:0.0; vlc -f --loop --video-on-top ../mars/plants/" + plants[i]
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        press_for_stop('g',proc)
    except:
        speak("sorry can not play video clip")

def play_tripataka_chapter(p):
    killPlayer()  
    speak("play Thai reading Tripitaka Chapter " + p)
    proc = subprocess.Popen(["mpg123","-d","2","-f","3000","../mars/tripitaka/Tripidok" + p + ".mp3"])
    press_for_stop('d',proc)

def pali_chanting():
    killPlayer()  
    speak("Pali grammar chanting")
    proc = subprocess.Popen(["mpg123","-f","3000","../mars/pali.mp3"])
    press_for_stop('d',proc)

def hdmi_display(s='on'):
    if s == 'off':
        os.system("/opt/vc/bin/tvservice -o")
    else:
        os.system("/opt/vc/bin/tvservice -p")
    espeak("turn display " + s, '5')
    return None

# sitting 1 hr
def testing_mode2():
    killPlayer()
    bell('3') 
    cheerful = [['BloomingFlowers.mp4','154'],['flowers-blooming.mp4','192']]
    i = random.randint(0,1)              
    try:
        command = "export DISPLAY=:0.0; vlc -f --loop --stop-time " + cheerful[i][1] + " --video-on-top ../sound/" + cheerful[i][0]
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        # delay(5)
        board.button.wait_for_press(3*int(cheerful[i][1]))
        proc.kill()
        killPlayer() 
    except:
        speak("sorry can not play video clip")
    my_sun()
    bell('1')
    om_meditation(5) 
    bell('1')   
    alpha_wave(50)
    bell('1')
    pkill_proc_name()
    clear_q()
    return None

# walking 1 hr
def testing_mode1():
    bell('3')
    sun = ['sun1.gif','sun2.gif','sun3.gif','sun4.gif']
    i = random.randint(0,3) 
    
    command = "export DISPLAY=:0.0; python3 testgif.py -f full -p ../sound/" + sun[i]
    proc1 = subprocess.Popen(command, shell=True)
    slow_buddho('off',15)
    slow_buddho2('off',15)
    slow_buddho("off",15)
    fast_buddho('oo',15)
    proc1.kill()
    pkill_proc_name("testgif")
    
    bell('1')
    clear_q()
    return None

def testing_mode3():
    bell('3')
    sun = ['sun1.gif','sun2.gif','sun3.gif','sun4.gif']
    i = random.randint(0,3) 
    
    command = "export DISPLAY=:0.0; python3 testgif.py -f full -p ../sound/" + sun[i]
    proc1 = subprocess.Popen(command, shell=True)
    slow_buddho('off',15)
    slow_buddho2('off',15)
    proc1.kill()
    pkill_proc_name("testgif")

    testing_mode2()
    
    return None

# walk 2 hrs sit 1 hr
def testing_mode4():
    bell('3')
    fruit = ['watermelon.gif','oranges.gif','redApple.gif','greenApple.gif','cantalupe.gif']

    i = random.randint(0,3) 
    command = "export DISPLAY=:0.0; python3 testgif.py -f full -p ../sound/" + fruit[i]
    proc1 = subprocess.Popen(command, shell=True)

    slow_buddho('off',30)
    bell('1')
    slow_buddho2('off',30)
    bell('1')
    slow_buddho('off',30)
    bell('1')
    fast_buddho('off',30)
    bell('1')
    alpha_wave(60)
    bell('2')

    proc1.kill()
    pkill_proc_name("testgif")
    clear_q()
    return None


def testing_mode9():
    testing_mode1()
    fast_buddho('off',180,'500')
    os.system("sudo shutdown now")
    return None


def my_sun():
    global proc_name
    sun = ['sun1.gif','sun2.gif','sun3.gif','sun4.gif']
    i = random.randint(0,3)
    command = "export DISPLAY=:0.0; python3 testgif.py -f full -p ../sound/"+sun[i]
    proc = subprocess.Popen(command, shell=True)
    proc_name = "testgif"
    return proc_name


def the_water():
    speak("water droplet at 2500 fps for visual meditation")
    killPlayer()                
    try:
        command = "export DISPLAY=:0.0; vlc -f --loop --video-on-top ../mars/water-droplets.mp4"
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        press_for_stop('d',proc)
        killPlayer() 
    except:
        speak("sorry can not play video clip")
    return None


def music_meditation(t=0,c='d',vol="6000"):
    ledc(c)
    if t == 0:
        proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../sound/youtubeRelaxmusic.mp3"])
        press_for_stop(c,proc)
    else:
        proc = subprocess.Popen(["mpg123","-f",vol,"-q","--loop","-1","../sound/youtubeRelaxmusic.mp3"])
        delay(t)
        proc.kill()
        clear_q()
    return None
    

def monk_rules(c='g'):
    ledc(c)
    proc = subprocess.Popen(["mpg123","-f","2000","-q","../mars/patimok.mp3"])
    press_for_stop(c,proc)
    return None


def morning_practice(c='off',vol="200"):
    ledc(c)
    # warm up
    slow_buddho(c,10,vol)
    alpha_wave(30)
    fast_buddho(c,10,vol)
    time.sleep(300)
    
    relax_thai(vol)

    bell('3',vol)
    # start
    ledc('off')
    alpha_wave(60)

    bell('1',vol)
    # cool down
    ledc(c)
    fast_buddho(c,30,vol)
    bell('3',vol)
    play_eight_fold_path_chanting_thai('500')
    
    return None


def morning_practice_chanting_mode(c='d',m=1,vol="200"):

    if m == 1:
        cm = '../mars/pahung.mp3'
        
    elif m == 2:
        cm = '../mars/matika.mp3'
        
    elif m == 3:
        cm = '../mars/7kampee.mp3'

    ledc(c)
    # warm up
    fast_buddho(c,50,vol)
    time.sleep(300)

    relax_thai(vol)

    bell('3',vol)
    # start
    ledc('off')
    proc = subprocess.Popen(["mpg123","-q","-f",vol,"--loop","-1",cm])
    time.sleep(3600)
    proc.kill()

    bell('1',vol)
    # cool down
    ledc(c)
    fast_buddho(c,30,vol)
    bell('3',vol)
    play_sutra('500')
    
    return None

# For Buddha holy day start at 6:00 pm
def evening_practice(d=0,vol="500"):
    # 8 + 2:30 hrs

    remind_sati_bikkhu()

    bell('3',vol)

    six_stages_th_en ('y',10)

    three_stages_th_en('b',10)

    one_stage_th_en('r',10)

    remind_sati()

    one_stage_en('g',10)
   
    slow_buddho('c',20)

    remind_right_sati()

    slow_buddho2('gg',15)
    fast_buddho('dd',15)

    fast_buddho('d',15)
    fast_buddho('off',15)

    vol = "300"
    bell('3',vol)
    ledc('off')

    relax_thai(vol)

    if d == 6:
        d = 0
        alpha_wave(360) # 6 hrs

    else:    
        alpha_wave(60)
        bell('3',vol)
        fast_buddho('off',300,vol) # 5 hrs

    bell('3',vol)

    if d == 1 or d == 2 or d == 3 or d == 4:
        if d == 4:
            d = random.randint(1,3)
        morning_practice_chanting_mode('d',d)
    else:
        morning_practice('d')
 
    return None

# International Code of Signals
ics  = 'a alfa b bravo c charlie d delta e echo f foxtrot g golf h hotel i india j juliet k kilo l lima m mike n november o oscar p papa '
ics += 'q quebec r romeo s sierra t tango u uniform v victor w whiskey x xray y yankee z zulu'
ics_list = ics.split(' ')
del ics
gc.collect()

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

    # https://github.com/Motion-Project/motion/
    os.system("sudo service motion stop")

    model = vosk.Model(args.model)

    master, slave = os.openpty()

    with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device, dtype='int16',
                            channels=1, callback=callback):
            print('#' * 80)
            print('Press Ctrl+C to stop playing')
            print('#' * 80)
            # print(args.samplerate)
            # print(args.device)

            os.system('espeak -s 130 -a 4 -v "english-us" "Nothing is worth insisting on"')
            os.system('mpg123 -q -f 400 ../thaivoices/samesame.mp3 ../thaivoices/hello.mp3')
            
            # new runtime vocabulary
            new_vocab = runtime_vocabulary()
            vrun  =  '["please zen story lord buddha buddhist buddhism what time day play help dhamma meditation english radio start light '
            vrun += 'browse chanting mantra say speak stop volume turn on off exit shutdown now thai lyric ip address sutra up down breathing '
            vrun += 'one two three four five six seven eight nine ten zero fifteen twenty thirty forty fifty sixty seventy eighty ninety '
            vrun += 'a alfa b bravo c charlie d delta e echo f foxtrot g golf h hotel i india j juliet k kilo l lima m mike n november o oscar p papa '
            vrun += 'q quebec r romeo s sierra t tango u uniform v victor w whiskey x ray y yankee z zulu letter repeat space spelling '
            vrun += 'walking mode search translate service cancel restart save anat ta sitting music raining thunder jungle tibetan heart '
            vrun += 'red green blue yellow alpha breathing pure monk rule speech morning evening practice web server sound my math next new '
            vrun += 'ohm the sun blooming flower clip quit my display testing water morse code good bye chapter pali '
            vrun += 'sixteen seventeen eighteen nineteen plants seed carbon food cell '
            vrun += new_vocab
            # vrun += ' how are you today what can i do for you ' #test
            vrun += 'yes no ok coca cola stage fold path nature truth dependent origination webcam loop daily life wise thinking technique"]'
            
            rec = vosk.KaldiRecognizer(model, args.samplerate,vrun)

            del vrun
            gc.collect()

            bot    = True
            focus  = False
            zen    = False
            math   = False
            mantra = False
            spell  = False
            save   = False
            yesno  = False
            repeat = False
            sit    = False
            verify = False
            proc_bool   = False
            # mp morning practice , ep evening practice
            mp = False
            ep = False
            mn = 0
            right_words = []
            add_letter  = ''
            spell_words = ''
            verify_words= ''   
            proc_name = ''
            sc = ""
            t  = 0
            k  = 0
            ch = ['a','b','c','d','e','f','i','j','k','l','q']
            ch_name  = ['fast buddho mantra','breathing in and out mantra in Thai','alpha sound with alpha light']
            ch_name += [' only alpha sound','only alpha light','relax and mindful mantra in Thai','Ohm sound','Meditation Music']
            ch_name += ['Tibetan music','Raining sound','Quit']
            time.sleep(1)
            i = random.randint(1,5)
            if i == 1:
                meditation_goal('500')
            elif i == 2:
                meditation_goal2('500')
            elif i == 3:
                meditation_goal3('500')
            elif i == 4:
                meditation_goal4('500')
            else:
                yoniso('555')
            # time.sleep(1)
            # espeak('hi,there! my name is anat ta, please call my name if you want to start','5')
            time.sleep(1)
            with q.mutex:
                q.queue.clear()

            while True:
                data = q.get()
                # print(q.qsize())       
                
                words = []
                with Leds() as leds:

                    if rec.AcceptWaveform(data):
                        w = rec.Result()
                        z = json.loads(w)
                        # print(z["text"])
                        # print(q.qsize()) 
                        words += z["text"].split()

                        # say "anat ta" to start
                        if z["text"] == "anat ta":
                            if not bot:
                                bot = True
                                words = []
                                speak("yes, what can i do for you?")
                                clear_q()
                        elif z["text"] == "hello":
                            espeak("Hello!",'5')
                            clear_q()
                        elif z["text"] == "please help":
                            get_help()
                            clear_q()
                            words = []
                        elif not bot:
                            words = []

                        if repeat:  

                            if not yesno and bot and len(words) > 0:
                                espeak("Do you said " + z["text"] + "?",'10') 
                                right_words = words
                                words = []
                                yesno = True
                                clear_q()
                            elif yesno:
                                if "no" in words:
                                    words = []
                                    yesno = False
                                    espeak("ok, please speak again",'5')
                                    clear_q()
                                elif "yes" in words:
                                    words = right_words
                                    yesno = False
                                else:
                                    words = []
                                    text  =  " ".join(str(x) for x in right_words) 
                                    espeak("Do you said " + text + "?",'5')
                                    espeak("please answer yes or no",'5')
                                    clear_q()
                            else:
                                words = []
                         
                        with Board() as board:
                            #coding
                            if not focus and len(words) > 1:

                                print(words)

                                if "wise" in words:
                                    if "alpha" in words:
                                        wise_one('gg')
                                    elif "one" in words:
                                        wise_one()

                                elif "morse" in words and "code" in words:
                                    if len(words) > 2:
                                        lt = words[2]
                                        if len(lt) == 1:
                                            try:
                                                n = ics_list.index(lt) + 1
                                                espeak('morse code for ' + lt + ' ' + ics_list[n],'5')
                                                morsecode(lt)
                                            except:
                                                pass
                                    else:
                                        morsecode('sati sati sati')
                                elif "plants" in words:
                                    i = words.index('plants') + 1
                                    try:
                                        if len(words[i]) > 1:
                                            play_plants(words[i])
                                        else:
                                            pass
                                    except:
                                        pass

                                elif "chapter" in words:
                                    if "sixteen" in words:
                                        p = '16'
                                    elif "seventeen" in words:
                                        p = '17'
                                    elif "eighteen" in words:
                                        p = '18'
                                    elif "nineteen" in words:
                                        p = '19'
                                    else:
                                        p = ''

                                    if p == '':
                                        pass
                                    else:
                                        play_tripataka_chapter(p)

                                elif "testing" in words:
                                    if "one" in words:
                                        testing_mode1()
                                    elif "two" in words:
                                        testing_mode2()
                                    elif "three" in words:
                                        testing_mode3()
                                    elif "four" in words:
                                        testing_mode4()
                                    elif "six" in words:
                                        testing_mode1()
                                        testing_mode2()
                                    elif "nine" in words:
                                        testing_mode9()

                                elif "repeat" in words:
                                    if "on" in words:
                                        repeat = True
                                        speak("Repeat mode on")
                                    elif "off" in words:
                                        repeat = False
                                        speak("Repeat mode off")

                                elif "anat" in words and "ta" in words:
                                    if "stop" in words:
                                        killPlayer()
                                        bot = False
                                        speak("ok, call my name when you need help, bye bye!")
                                    elif "restart" in words:
                                        speak("restart the service, please wait")
                                        os.system("sudo systemctl restart myscript.service")
                                        break
                                    elif "shutdown" in words:
                                        shutdown()
                                        break

                                elif "sound" in words:
                                    i = int(words.index('sound')) + 1
                                    
                                    try:
                                        r = word2int(words[i])
                                        if r == 'None':
                                            h = 0
                                        else:
                                            h = int(r)
                                    except:
                                        h = 0

                                    t = h*60
                                    if t == 0:
                                        speak("push button to stop")
                                    else:
                                        speak(str(t) + " minutes")

                                    if "raining" in words:
                                        speak("raining sound meditation")
                                        bell('3')
                                        raining_meditation(t)

                                    elif "thunder" in words:
                                        speak("thunder storm sound meditation")
                                        bell('3')
                                        thunder_meditation(t)

                                    elif "jungle" in words:
                                        speak("jungle sound meditation")
                                        bell('3')
                                        jungle_meditation(t)

                                    elif "tibetan" in words:
                                        speak("Tibetan sound meditation")
                                        bell('3')
                                        tibetan_meditation(t)

                                    elif "ohm" in words:
                                        speak("Ohm at 417 Herzt sound meditation")
                                        bell('3')
                                        om_meditation(t)

                                elif "alpha" in words:
                                    if "sixty" in words:
                                        t = 60
                                    elif "ninety" in words:
                                        t = 90
                                    else:
                                        t = 30
                                    
                                    if "breathing" in words:
                                        breathing_alpha_meditation('g',t);
                                    elif "pure" in words:
                                        pure_alpha() # for martian monk only 
                                    else:
                                        alpha_meditation(t,15,'g')

                                elif "meditation" in words:
                                    if "math" in words:
                                        a = random.randint(1,20)
                                        b = random.randint(1,20)
                                        speak("what is "+ str(a) + " plus "+ str(b))
                                        c = a + b
                                        sc = ''
                                        lc = list(str(c))
                                        for i in lc:
                                            sc += int2word(int(i))
                                        focus = True
                                        math = True
                                        words = []
                                    elif "music" in words:
                                        bell('3')
                                        music_meditation() 
                                    elif "time" in words:
                                        meditation_time()

                                elif "practice" in words:

                                    if "walking" in words:
                                        walking_reward()
                                        walking_meditation_count()

                                    elif "sitting" in words:

                                        if "one" in words:
                                            t = 60
                                        elif "two" in words:
                                            t = 120
                                        else:
                                            t = 30

                                        speak("sitting meditation practice for " + str(t) + " minutes")
                                        speak("which practice mode you like?")

                                        for i in range(len(ch)):
                                            speak(ch[i] + ", " + ch_name[i])
                                            time.sleep(1)

                                        sit   = True
                                        focus = True
                                    # for martian monk only     
                                    elif "morning" in words:
                                        if"one" in words:
                                            verify_words = 'Do you want to play pahoong chanting morning practice?'
                                            mn = 1
                                        elif "two" in words:
                                            verify_words = 'Do you want to play martika chanting morning practice?'
                                            mn = 2
                                        elif "three" in words:
                                            verify_words = 'Do you want to play 7 kumpee chanting morning practice?'
                                            mn = 3
                                        else:
                                            verify_words = 'Do you want to play morning practice?'
                                            mn = 0

                                        mp = True    
                                        verify = True
                                        focus  = True

                                    elif "evening" in words:
                                        if "one" in words:
                                            verify_words = 'Do you want to play pahoong chanting in the morning?'
                                            mn = 1
                                        elif "two" in words:
                                            verify_words = 'Do you want to play martika chanting in the morning?'
                                            mn = 2
                                        elif "three" in words:
                                            verify_words = 'Do you want to play 7 kumpee chanting in the morning?'
                                            mn = 3
                                        elif "four" in words:
                                            verify_words = 'Do you want to play random chanting in the morning?'
                                            mn = 4
                                        elif "six" in words:
                                            verify_words = 'Do you want to play alpha sound in the evening?'
                                            mn = 6 
                                        else:
                                            verify_words = 'Do you want to play basic mode evening practice?'
                                            mn = 0

                                        ep = True
                                        verify = True
                                        focus  = True

                                # for martian monk only 
                                elif "monk" in words and "rule" in words:
                                    monk_rules()                                

                                elif "spelling" in words and "mode" in words:
                                    speak("spelling mode, please use international code of signals such as, c charlie but can say letter c too")
                                    spell = True
                                    focus = True
                                    yesno = False
                                    save  = False
                                    spell_words = ''

                                elif "what" in words:
                                    if "time" in words:
                                        what_time()
                                    elif "day" in words:
                                        what_day()

                                elif "buddha" in words and "day" in words:
                                    buddha_day()
                                    
                                elif "zen" in words and "story" in words:
                                    nn = sequence[n]
                                    speak("Do you want to listen to this zen story?")
                                    speak(d["zen101"][nn]["title"])
                                    focus = True
                                    zen = True

                                elif "dependent" in words and "origination" in words:
                                    if "daily" in words:
                                        play_daily_dependent_origination_thai()
                                    elif "chanting" in words:
                                        play_dependent_origination_chanting_thai()
                                    elif "clip" in words:
                                        play_dependent_origination_clip()

                                elif "buddha" in words and "thinking" in words:
                                    play_buddha_thinking_thai()                                 

                                elif "fold" in words and "path" in words:
                                    if "thai" in words:
                                        play_eight_fold_path_chanting_thai()
                                    elif "english" in words:
                                        play_eight_fold_path_chanting_english()
                                    elif "clip" in words:
                                        speak("play 8 fold path with lyrics")
                                        play_8_fold_path_clip()

                                elif "chanting" in words:

                                    if "english" in words:
                                        english_chating()

                                    elif "thai" in words:
                                        thai_chanting()

                                    elif "breathing" in words:
                                        play_breathing_chanting_thai()

                                    elif "nature" in words and "truth" in words:
                                        play_nature_truth_chanting_thai() 

                                    elif "pali" in words:
                                        pali_chanting()

                                    elif "heart" in words:

                                        if "clip" in words:
                                            speak("play heart sutra with lyrics")
                                            killPlayer()                
                                            try:
                                                command = "export DISPLAY=:0.0; vlc -f --loop --video-on-top ../dataen/chanting/heart-sutra.mp4"
                                                proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                                                press_for_stop('d',proc)
                                                killPlayer() 
                                            except:
                                                speak("sorry can not play video clip")
                                        else:
                                            heart_sutra(0)
                                                                        
                                elif "play" in words:

                                    if "radio" in words:
                                        play_radio()
                                    elif "dhamma" in words:
                                        play_dhamma()
                                    elif "speech" in words or "sutra" in words:
                                        play_sutra()                                
                                    
                                elif "mantra" in words:

                                    killPlayer() 
                                    mantra = True  
                                    focus = True                                  
                                      
                                    if "five" in words:
                                        t = 5
                                        speak("Do you want to play slow buddho mantra and push button to stop?")
                                                                               
                                    elif "one" in words:  
                                        t = 1
                                        speak("Do you want to play one hour buddho mantra?")
                                    
                                    elif "two" in words: 
                                        t = 2
                                        speak("Do you want to play  mixed mode 1 hour?")                                        

                                    elif "three" in words:  
                                        t = 3
                                        speak("Do you want to play 4 hours mantra and 4 hours alpha sound?")

                                    elif "four" in words:  
                                        t = 4
                                        speak("Do you want to play 4 hours buddho mantra then shutdown?")

                                    elif "six" in words:  
                                        t = 6
                                        speak("Do you want to play mixed mode 4 hours mantra then shutdown?")

                                    elif "play" in words:
                                        t = 8
                                        speak("Do you want to play fast buddho mantra push button to stop?")

                                    elif "ten" in words:
                                        t = 10 
                                        speak("Do you want to play " + str(t) + " minutes buddho mantra?")
                                    elif "fiftheen" in words:
                                        t = 15
                                        speak("Do you want to play " + str(t) + " minutes buddho mantra?")
                                    elif "twenty" in words:
                                        t = 20
                                        speak("Do you want to play " + str(t) + " minutes buddho mantra?")
                                    elif "thirty" in words:
                                        t = 30
                                        speak("Do you want to play " + str(t) + " minutes buddho mantra?")
                                    elif "forty" in words:
                                        t = 40
                                        speak("Do you want to play " + str(t) + " minutes buddho mantra?")
                                    elif "fifty" in words:
                                        t = 50
                                        speak("Do you want to play " + str(t) + " minutes buddho mantra?")
                                    else:
                                        t = 0
                                        mantra = False
                                        focus = False                             

                                elif "stage" in words:

                                    if "one" in words:

                                        killPlayer()

                                        if "five" in words:
                                            t = 5
                                        elif "ten" in words:
                                            t = 10 
                                        elif "fiftheen" in words:
                                            t = 15
                                        elif "twenty" in words:
                                            t = 20
                                        else:
                                            t = 30

                                        speak(str(t) + " minutes 1 stage walking practice")

                                        if "english" in words:
                                            one_stage_en('g',t)
                                        else:
                                            one_stage_th_en('g',t)

                                    elif "three" in words:
                                        three_stages_th_en('g')

                                    elif "six" in words:
                                        six_stages_th_en('g')                    
                                   
                                elif "dhamma" in words:
                                    if "buddha" in words:
                                        buddha_dhamma()   
                                    elif "my" in words:
                                        play_my_dhamma()
                                          
                                #PLAY
                                elif "light" in words and "on" in words:

                                    if "red" in words:
                                        c = 'r'
                                    
                                    elif "green" in words:
                                        c = 'g'
                                    
                                    elif "blue" in words:
                                        c = 'b'
                                    
                                    elif "yellow" in words:
                                        c = 'y'

                                    else:
                                        c = ''

                                    if "alpha" in words:
                                        if len(c) == 1:
                                           c += c

                                    # may say : color sound alpha light on
                                    if "sound" in words:
                                        ledc(c)
                                        proc = subprocess.Popen(["mpg123","-q","--loop","-1","../dataen/alpha12Hz.mp3"])
                                        proc_bool = True
                                    else:
                                        ledc(c)                                        

                                    board.button.wait_for_press()
                                    if proc_bool:
                                        proc.kill()
                                        proc_bool = False

                                # https://www.raspberrypi.org/documentation/remote-access/web-server/nginx.md        
                                elif "web" in words and "server" in words:
                                    ip = get_ip()
                                    if "start" in words:
                                        if find_name('nginx'):
                                            speak("web server already start at ip " + ip)
                                        else:
                                            os.system("sudo /etc/init.d/nginx start")
                                            speak("web server start at ip " + ip)
                                    if "stop" in words:
                                        if find_name('nginx'):
                                            os.system("sudo /etc/init.d/nginx stop")
                                            speak("stop web server")
                                        else:
                                            speak("web server already stop")


                                # https://pimylifeup.com/raspberry-pi-webcam-server/ 
                                elif "turn" in words and "webcam" in words:
                                    if "on" in words:
                                        ip = get_ip()
                                        speak("Turn on web camera at ip address")
                                        speak(ip + " port number 8081") 
                                        os.system("sudo service motion start") 
                                    elif "off" in words:
                                        speak("Turn off web camera")
                                        os.system("sudo service motion stop")
                                        

                                #TEST
                                elif "buddha" in words:
                                    if "story" in words or "what" in words:
                                        speak("play buddha story")
                                        killPlayer()                
                                        try:
                                            command = "export DISPLAY=:0.0; vlc -f --stop-time 453 --play-and-exit buddha-story.mp4"
                                            proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                                            press_for_stop('d',proc)
                                            killPlayer() 
                                        except:
                                            speak("sorry can not play video clip")

                                elif "my" in words and "sun" in words:
                                    espeak("open sun gif animation",'4')
                                    sun = ['sun1.gif','sun2.gif']
                                    i = random.randint(0,1)
                                    command = "export DISPLAY=:0.0; python3 testgif.py -f full -p ../sound/"+sun[i]
                                    proc = subprocess.Popen(command, shell=True)
                                    proc_name = "testgif"
                                    proc_bool = True
                                    # fast_buddho('d',0)

                                elif "the" in words:
                                    if "sun" in words:
                                        speak("the sun time lapse for fire meditation")
                                        killPlayer()                
                                        try:
                                            command = "export DISPLAY=:0.0; vlc -f --loop --video-on-top ../sound/sun.mp4"
                                            proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                                            press_for_stop('d',proc)
                                            killPlayer() 
                                        except:
                                            speak("sorry can not play video clip")

                                    elif "water" in words:
                                        the_water()

                                elif "blooming" in words and "flower" in words:
                                    speak("the blooming flowers time lapse for cheerful meditation")
                                    killPlayer()  
                                    cheerful = [['BloomingFlowers.mp4','154'],['flowers-blooming.mp4','192']]
                                    i = random.randint(0,1)              
                                    try:
                                        command = "export DISPLAY=:0.0; vlc -f --loop --stop-time " + cheerful[i][1] + " --video-on-top ../sound/" + cheerful[i][0]
                                        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                                        press_for_stop('d',proc)
                                        killPlayer() 
                                    except:
                                        speak("sorry can not play video clip")

                                elif "browse" in words:
                                    if "buddhism" in words:
                                        speak("open Thai buddhism in wikipedia")
                                        command = "export DISPLAY=:0.0; chromium-browser --incognito --start-fullscreen --start-maximized https://th.wikipedia.org/wiki/ศาสนาพุทธ"
                                        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                                        press_for_stop('g',proc)
                                        os.system("sudo pkill -f chromium")

                                    elif "buddhist" in words and "story" in words:
                                        speak("open youtube for buddhist stories")
                                        command = "export DISPLAY=:0.0; chromium-browser --incognito --start-fullscreen --start-maximized https://www.youtube.com/watch?v=tI-hgIhFDT0&list=PLYBNr5a72-497Q3UVkpDB24W4NTCD5f2K"
                                        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                                        press_for_stop('g',proc)
                                        os.system("sudo pkill -f chromium")

                                    elif "meditation" in words and "technique" in words:
                                        speak("open youtube for meditation technique")
                                        command = "export DISPLAY=:0.0; chromium-browser --incognito --start-fullscreen --start-maximized https://www.youtube.com/playlist?list=PLUh8U5np7D-7FMh6ONGwnaltFppPBwTVI"
                                        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                                        press_for_stop('g',proc)
                                        os.system("sudo pkill -f chromium")
                                    elif "webcam" in words:
                                        speak("open webcam on web browser")
                                        ip = get_ip()
                                        command = "export DISPLAY=:0.0; chromium-browser --incognito --start-fullscreen --start-maximized " + ip + ":8081"
                                        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                                        press_for_stop('g',proc)
                                        os.system("sudo pkill -f chromium")
   
                                elif "please" in words:
                                    if "help" in words:
                                        get_help()

                                    elif "stop" in words:
                                        killPlayer()
                                        if len(proc_name) > 0:
                                            os.system("pkill -f " + proc_name)
                                            speak("kill " + proc_name)
                                            proc_name = ''
                                        if proc_bool:
                                            proc.kill()
                                            proc_bool = False
                                            speak("kill the process")
                                        speak("done")
                                        clear_q()
                                    elif "restart" in words:
                                        speak("restart the service, please wait")
                                        os.system("sudo systemctl restart myscript.service")
                                        break

                                    elif "shutdown" in words:
                                        shutdown()
                                        break

                                elif "good" in words and "bye" in words:
                                    shutdown()
                                    break
                                
                                elif "volume" in words:
                                    if "up" in words:
                                        call(["amixer","-D","pulse","sset","Master","95%"])
                                        speak("set volume to 95%")
                                    elif "down" in words:
                                        call(["amixer","-D","pulse","sset","Master","50%"])
                                        speak("set volume to 50%")

                                elif "ip" in words and "address" in words:
                                    ip = get_ip()
                                    speak(ip)

                                elif "say" in words:
                                    listToStr = ' '.join(map(str, words))
                                    listToStr = listToStr.replace("say",'')
                                    speak("You said, " + listToStr)
                                    clear_q()

                                elif len(words) > 0:
                                    listToStr = ' '.join(map(str, words))
                                    espeak("words i heard , " + listToStr, '5')
                                    clear_q()
                                                               
                            else:

                                if len(words)>0:

                                    if verify:
                                        if "no" in words:
                                            speak('ok')
                                            verify = False
                                            focus = False
                                        elif "yes" in words:
                                            if mp:
                                                if mn == 0:
                                                    morning_practice()
                                                else:
                                                    morning_practice_chanting_mode('d',mn)
                                                verify = False
                                                mp = False
                                                focus = False
                                            elif ep:
                                                evening_practice(d)
                                                verify = False
                                                ep = False
                                                focus = False

                                        else:
                                            espeak(verify_words,'5')
                                            espeak("please answer yes or no",'5')
                                            clear_q()

                                    elif zen:
                                        if "no" in words:
                                            n = n + 1
                                            if n == m:
                                                random.shuffle(sequence)
                                                n = 0
                                            nn = sequence[n]    
                                            speak("Do you want to listen to this zen story?")                                     
                                            speak(d["zen101"][nn]["title"])  
                                        elif "yes" in words:
                                            lines = d["zen101"][nn]["story"]
                                            # print(lines)
                                            for i in range(len(lines)):
                                                x = int(lines[i]["voice"])
                                                engine.setProperty('voice',es_voices[x]) 
                                                speak(lines[i]["text"])
                                            zen = False
                                            focus = False
                                            engine.setProperty('voice',es_voices[2]) 
                                            n = n +1 
                                        else:
                                            speak("please speak yes or no")
                                            clear_q()

                                    elif math:
                                        
                                        ans = ''
                                        for x in words:
                                            ans += x

                                        if sc == ans:
                                            speak("well done")
                                            a = random.randint(1,20)
                                            b = random.randint(1,20)
                                            if a>b:
                                                speak("what is "+ str(a) + " minus "+ str(b))
                                                c = a - b
                                            else:
                                                speak("what is "+ str(a) + " plus "+ str(b))
                                                c = a + b
                                            sc = ''
                                            lc = list(str(c))
                                            for i in lc:
                                                sc += int2word(int(i))
                                            clear_q()

                                        elif "stop" in words:
                                            math = False
                                            focus = False
                                            speak("quit math meditation")
                                            clear_q()
                                        elif "next" in words:
                                            speak("the answer is " + sc)
                                            a = random.randint(1,20)
                                            b = random.randint(1,20)
                                            if a>b:
                                                speak("what is "+ str(a) + " minus "+ str(b))
                                                c = a - b
                                            else:
                                                speak("what is "+ str(a) + " plus "+ str(b))
                                                c = a + b
                                            sc = ''
                                            lc = list(str(c))
                                            for i in lc:
                                                sc += int2word(int(i))
                                            clear_q()                                     

                                        else:
                                            speak("i heard "+ ans + " , it's incorrect")
                                            clear_q()

                                    elif mantra:

                                        if "yes" in words:

                                            if t == 1:
                                                bell('3','500')
                                                fast_buddho('y',15)
                                                fast_buddho('yy',15)
                                                bell('3','500')
                                                fast_buddho('g',15)
                                                fast_buddho('gg',15)
                                                mantra = False
                                                focus = False

                                            elif t == 2:
                                                c = ["r","g","b","y","p","c"]
                                                n = [0,1,2,3]

                                                random.shuffle(c)
                                                random.shuffle(n)

                                                mixed_mode(c[0],10,n[0])
                                                mixed_mode(c[1],10,n[1])
                                                mixed_mode(c[2],10,n[2])
                                                mixed_mode(c[3],10,n[3])                                       
                                                
                                                remind_sati()
                                                
                                                slow_buddho(c[4],10)
                                                fast_buddho(c[5],10)
                                                mantra = False
                                                focus = False

                                            elif t == 3:
                                                remind_sati_bikkhu()
                                            
                                                one_stage_th_en('y',10)

                                                one_stage_en('g',10)

                                                three_stages_th_en('b',10)
                                                
                                                remind_sati()

                                                slow_buddho2('c',15)
                                                fast_buddho('gg',15)

                                                remind_right_sati()

                                                fast_buddho('off',180)
                                                
                                                ledc('off')
                                                alpha_wave(240)
                                                mantra = False
                                                focus = False

                                            elif t == 4:
                                                slow_buddho('off',15)
                                                slow_buddho2('off',15)
                                                                                                
                                                remind_sati()

                                                slow_buddho2('bb',15)
                                                fast_buddho('gg',15)

                                                remind_right_sati()

                                                fast_buddho('off',180)
                                                
                                                os.system("sudo shutdown now")
                                                break

                                            elif t == 5:
                                                slow_buddho('off',0)
                                                mantra = False
                                                focus = False

                                            elif t == 6:
                                                remind_sati_bikkhu()

                                                three_stages_th_en('c',10)

                                                six_stages_th_en('y')

                                                one_stage_th_en('g',15)

                                                one_stage_en('b',15)

                                                fast_buddho('p',15)
                                                
                                                remind_right_sati()

                                                slow_buddho('yy',15)

                                                fast_buddho('off',15)

                                                remind_sati()

                                                slow_buddho('gg',15)

                                                fast_buddho('off',15)

                                                fast_buddho('off',120)
                                                
                                                os.system("sudo shutdown now")
                                                break

                                            elif t == 8:
                                                speak("fast buddho mantra push button to stop")
                                                bell('3','500')
                                                fast_buddho('d',0)
                                                mantra = False
                                                focus = False

                                            else :
                                                speak(str(t) + " minutes buddho mantra")
                                                bell('3','500')
                                                fast_buddho('g',t)
                                                mantra = False
                                                focus = False

                                        elif "no" in words:
                                            speak('ok, please repeat your command again')
                                            mantra = False
                                            focus = False

                                        else:
                                            speak("please speak yes or no")
                                            clear_q()

                                    elif spell:

                                        if len(words) > 1 and not yesno:

                                            try:
                                                if len(words[1]) > 1:
                                                    b = ics_list.index(words[1])-1
                                                    add_letter = ics_list[b]
                                                    speak("Do you want to add letter " + add_letter + " " + words[1] + "?")
                                                    yesno = True
                                                else:
                                                    if len(words[1]) == 1:   
                                                        add_letter = words[1]
                                                        b = ics_list.index(words[1])+1
                                                        speak("Do you want to add letter " + add_letter + " " + ics_list[b] + "?")
                                                        yesno = True
                                                    else:
                                                        pass
                                            except:
                                                if words[0] == "letter" and len(words[1]) == 1:
                                                    add_letter = words[1]
                                                    b = ics_list.index(words[1])+1
                                                    speak("Do you want to add letter " + add_letter + " " + ics_list[b] + "?")
                                                    yesno = True
                                                else:
                                                    if words[1] == "space":
                                                        add_letter = "space"
                                                        speak("Do you want to add letter " + add_letter + "?")
                                                        yesno = True
                                                    else:
                                                        pass

                                        elif "yes" in words:
                                            if save:
                                                #save words for runtime vocabulary
                                                save_vocabulary(spell_words)
                                                save = False
                                            elif add_letter == "space":
                                                spell_words += ' '
                                            else:
                                                spell_words += add_letter

                                            speak("done, what's next?")
                                            yesno = False

                                        elif "repeat" in words:
                                            spw = list(spell_words)
                                            for l in spw:
                                                speak(l)

                                        elif "speak" in words:
                                            speak(spell_words)

                                        elif "no" in words: 
                                            if save:
                                                speak("ok, do not save it")
                                            else:
                                                speak("please repeat the letter you want again")
                                            yesno = False

                                        elif "save" in words:
                                            speak("Do you really want to save " + spell_words + " to runtime vocabulary?")
                                            yesno = True
                                            save = True
                                            
                                        elif "search" in words:
                                            speak("I will google for " + spell_words + "please see the search result on the monitor and push button to quit")
                                            command = 'export DISPLAY=:0.0; chromium-browser --incognito --start-fullscreen --start-maximized https://www.google.com/search?q="' + spell_words + '"'
                                            proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                                            press_for_stop('g',proc)
                                            os.system("sudo pkill -f chromium")
                                            focus = False
                                            spell = False

                                        elif "translate" in words:
                                            speak("please see the translation on the monitor and push button to Quit")
                                            command = 'export DISPLAY=:0.0; chromium-browser --incognito --start-fullscreen --start-maximized https://www.google.com/search?q="translate ' + spell_words + '"'
                                            proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                                            press_for_stop('g',proc)
                                            os.system("sudo pkill -f chromium")
                                            focus = False
                                            spell = False

                                        elif "exit" == words[0]:
                                            speak("Quit spelling mode")
                                            focus = False
                                            spell = False

                                        else:
                                            listToStr = ' '.join(map(str, words))
                                            espeak("i heard , " + listToStr, '5')
                                            if yesno:
                                                espeak("please answer yes or no",'5')
                                            else:
                                                espeak("next letter please", '5')
                                            clear_q()   
                                    
                                    elif sit:

                                        if yesno:
                                            if "yes" in words:
                                                speak(str(t) + " minutes " + ch_name[k])
                                                if ch[k] == 'a':
                                                    bell('3','500')
                                                    fast_buddho('off',t)
                                                    bell('1','500')
                                                    focus = False
                                                    sit = False
                                                elif ch[k] == 'b':
                                                    bell('3','500')
                                                    remind_breathing(t)
                                                    bell('1','500')
                                                    focus = False
                                                    sit = False
                                                elif ch[k] == 'c':
                                                    breathing_alpha_meditation('gg',t)
                                                    focus = False
                                                    sit = False
                                                elif ch[k] == 'd':
                                                    breathing_alpha_meditation('off',t)
                                                    focus = False
                                                    sit = False
                                                elif ch[k] == 'e':
                                                    bell('3','500')
                                                    ledc('gg')
                                                    delay(t)
                                                    bell('1','500')
                                                    focus = False
                                                    sit = False
                                                elif ch[k] == 'f':
                                                    remind_relax(t)
                                                    focus = False
                                                    sit = False
                                                elif ch[k] == 'i':
                                                    bell('3','500')
                                                    om_meditation(t)
                                                    bell('1','500')
                                                    focus = False
                                                    sit = False
                                                elif ch[k] == 'j':
                                                    bell('3','500')
                                                    music_meditation(t)
                                                    bell('1','500')
                                                    focus = False
                                                    sit = False
                                                elif ch[k] == 'k':
                                                    bell('3','500')
                                                    tibetan_meditation(t)
                                                    bell('1','500')
                                                    focus = False
                                                    sit = False
                                                elif ch[k] == 'l':
                                                    bell('3','500')
                                                    raining_meditation(t)
                                                    bell('1','500')
                                                    focus = False
                                                    sit = False
                                            elif "no" in words:
                                                yesno = False
                                                speak("please select new choice ")
                                                speak(ch)
                                                clear_q()
                                            else:
                                                listToStr = ' '.join(map(str, words))
                                                espeak("i heard , " + listToStr, '5')
                                                espeak("please answer yes or no",'5')
                                                clear_q()                                                
                                            
                                        elif len(words[0]) == 1:

                                            if words[0] == 'q':
                                                speak("Quit sitting practice")
                                                focus = False
                                                sit = False
                                            else:
                                                try:
                                                    k = ch.index(words[0])
                                                    speak("Do you want to play " + ch_name[k] + "?")
                                                    yesno = True
                                                    
                                                except:
                                                    listToStr = ' '.join(map(str, words))
                                                    espeak("i heard , " + listToStr, '5')
                                                    speak("please select")
                                                    speak(ch)
                                                    yesno = False
                                                    clear_q()
                                                

                    else:
                        if bot:
                            leds.update(Leds.rgb_on(Color.RED))
                        else:
                            leds.update(Leds.rgb_on(Color.BLACK))
                        # x = rec.PartialResult()
                        # print(x)

except KeyboardInterrupt:
    print('\nDone')
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))


# For Martian Monk Bhavana practice
# twitter @MartianZenMonk