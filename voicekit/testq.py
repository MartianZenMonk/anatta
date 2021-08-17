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
    if q.qsize() > 10:
        with q.mutex:
            q.queue.clear()
    else:
        q.put(bytes(indata)) 


def clear_q():
    time.sleep(1)
    with q.mutex:
        q.queue.clear()


def ledc(c='', f='alpha'):
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

    elif c == 'off':
        board.led.state = Led.OFF

    else:
        leds.update(Leds.rgb_on(Color.WHITE))

    return None


def press_for_stop(c='',proc=0):
    ledc(c)
    board.button.wait_for_press()
    proc.kill()
    with q.mutex:
        q.queue.clear()
    return None


def get_help():
    text =  '''
            You have to start with words anat ta,
            and then you can say,
            repeat mode on off,
            daily dependent origination,
            buddha thinking,
            nature truth chanting,
            breathing chanting,
            dependent origination chanting,
            8 fold path Thai, 8 fold path English,
            English chanting, Thai chanting,
            meditaion time, play radio, 
            play mantra 1 2 3 4 5 6 or 10 15 20 30 40 50 minutes,
            play 1 3 6 stage,
            buddha dhamma, play dhamma, play sutra, my dhamma
            what time, what day, buddha day, zen story,
            red green blue yellow or sound and or alpha light on,
            pure or breathing alpha meditation,
            math meditation,
            walking practice,
            moring practice,
            wise one and or alpha,
            please shutdown or anat ta stop,
            '''
    speak(text)
    time.sleep(3)
    with q.mutex:
        q.queue.clear()
    return None


def shutdown():
    os.system("mpg123 -f 1000 ../thaivoices/dead.mp3")
    speak("The system is shutting down, wait until the green light in the box turn off")
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


def killPlayer():
    if find_name('mpg123'):
        os.system("killall mpg123")
    if find_name('vlc'):
        os.system("killall vlc")
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


def fast_buddho(c='off', t=30, vol='1000'):

    ledc(c)

    if t==0:
        proc = subprocess.Popen(["mpg123","-d","3","-f",vol,"-q","--loop","-1","../thaivoices/buddho.mp3"])
        press_for_stop(c,proc)
    else:
        proc = subprocess.Popen(["mpg123","-d","3","-f",vol,"-q","--loop","-1","../thaivoices/buddho.mp3"])
        time.sleep(60*t)
        proc.kill() 
   
    return None



def bell(l='3',vol='200'):
    subprocess.run(["mpg123","-q","-f",vol,"--loop",l,"../dataen/bell.mp3"])
    return None


def relax_thai(vol="500"):

    text  = ["ทำ","ตัว","ผ่อน","คลาย","หาย","ใจ","ยาว","ยาว","คลาย","ความ","กังวล","ตั้ง","จิต","มั่น","รู้","ลม","หาย","ใจ",]
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
    proc = subprocess.Popen(["mpg123","-q","--loop","-1","../mars/pureAlpha.mp3"])
    press_for_stop(c,proc)
    return None


def alpha_wave(t):
    proc = subprocess.Popen(["mpg123","-q","--loop","-1","../mars/pureAlpha.mp3"])
    time.sleep(60*t)
    proc.kill()
    return None


#BHAVANA
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

    bell('3',vol)
    
    return None


def alpha_meditation(m=60,t=15,c='off',vol="500"):


    speak(str(m) + " minutes alpha sound")

    bell('3',vol)

    if len(c) == 1:
        ledc(c+c)
    else:
        ledc(c)

    if t == 0:
        t = m
        alpha_wave(t)
        bell('3',vol)
    else:
        timeout = time.time() + 60*m
        while True:
        
            if time.time() > timeout:
                break
            else:
                alpha_wave(t)
                bell('3',vol)


    return None


def slow_buddho(c='',t=30):
    ledc(c)
    th_stand = thwords(["ยืน","หนอ"])
    for i in range(3):
        os.system('mpg123 -f 2000 ' + th_stand)
        time.sleep(1)

    del th_stand
    gc.collect()

    if t==0:
        proc = subprocess.Popen(["mpg123","-f","1000","-q","--loop","-1","../thaivoices/buddho0.mp3"])
        press_for_stop(c,proc)
    else:
        proc = subprocess.Popen(["mpg123","-f","1000","-q","--loop","-1","../thaivoices/buddho0.mp3"])
        time.sleep(60*t)
        proc.kill()
    
    return None


def one_stage_en(c='',t=5):
    ledc(c)
    for i in range(3):
        speak("standing")
        time.sleep(1)
    proc = subprocess.Popen(["mpg123","-f","1000","-q","--loop","-1","../dataen/one_stage.mp3"])
    time.sleep(60*t)
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
    return None

def meditation_goal():
    text = " ../thaivoices/goal.mp3"
    os.system("mpg123 -q -f 2000 "+text)


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
    leds.update(Leds.rgb_on(Color.RED))
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
    text = "Meditation time will make 15 minutes bell sound, you may relax your self by walking then sitting. "
    text += "For walking, set a distance to meditate walking back and forth, your senses inwardly immersed, your mind not straying outwards. "
    text += "Lifting, Moving, Treading, slow moving and always mind your foot movement then you can increse your awakening sense, "
    text += "or free walking, just focus on Treading, "
    text += "For sitting, breathing in calm, breathing out down, always mind your breathing, your citta will not go around"
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
    os.system("mpg123 -f " + vol + " ../datath/sutta/moggallana.mp3")
    proc = subprocess.Popen(["mpg123","-f",vol,"-C","-z","--list","sutra.txt"], stdin=master)
    press_for_stop('r',proc)


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


# FOR MARTIAN MONK ONLY
def monk_rules(c='g'):
    ledc(c)
    proc = subprocess.Popen(["mpg123","-f","2000","-q","../mars/patimok.mp3"])
    press_for_stop(c,proc)
    return None


def morning_practice(c='off',vol="200"):

    ledc(c)
    # warm up
    fast_buddho(c,10,vol)
    alpha_wave(30)
    fast_buddho(c,10,vol)
    time.sleep(300)
    
    relax_thai(vol)

    # bell('3',vol)
    # start
    ledc('off')
    alpha_wave(60)

    bell('3',vol)
    # cool down
    ledc(c)
    fast_buddho(c,30,vol)

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
    fast_buddho(c,10,vol)
    alpha_wave(30)
    fast_buddho(c,10,vol)
    time.sleep(300)

    relax_thai(vol)

    bell('3',vol)
    # start
    ledc('off')
    proc = subprocess.Popen(["mpg123","-q","-f",vol,"--loop","-1",cm])
    time.sleep(3600)
    proc.kill()

    bell('3',vol)
    # cool down
    ledc(c)
    fast_buddho(c,30,vol)

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

    fast_buddho('gg',15)
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
            d = random.randint(0,2)
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
            # speak("Welcome to Anat ta Project, your Buddhist true friend ever")
            # get_help()
            os.system('espeak -s 130 -a 4 -v "english-us" "Nothing is worth insisting on"')
            os.system('mpg123 -q -f 400 ../thaivoices/hello.mp3')
            
            # new runtime vocabulary
            new_vocab = runtime_vocabulary()
            v =  '["please zen story lord buddha buddhist buddhism what time day play help dhamma meditation english radio start light '
            v += 'browse chanting mantra say speak stop volume turn on off exit shutdown now thai lyric ip address sutra up down breathing '
            v += 'one two three four five six seven eight nine ten zero fifteen twenty thirty forty fifty sixty seventy eighty ninety '
            v += 'a alfa b bravo c charlie d delta e echo f foxtrot g golf h hotel i india j juliet k kilo l lima m mike n november o oscar p papa '
            v += 'q quebec r romeo s sierra t tango u uniform v victor w whiskey x ray y yankee z zulu letter repeat space spelling '
            v += 'walking mode search translate service cancel restart save anat ta '
            v += 'red green blue yellow alpha breathing pure monk rule speech morning evening practice web server sound my math next new '
            v += new_vocab
            v += 'yes no ok coca cola stage fold path nature truth dependent origination webcam loop daily life wise thinking technique"]'

            rec = vosk.KaldiRecognizer(model, args.samplerate,v)

            del v
            gc.collect()

            bot = False
            focus = False
            zen = False
            proc_bool = False
            math = False
            mantra = False
            spell = False
            save = False
            yesno = False
            repeat = False
            right_words = []
            add_letter = ''
            spell_words = ''
            sc = ""
            t = 0
            meditation_goal()
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
                                speak("yes sir, what can i do for you?")
                                clear_q()
                        elif z["text"] == "please help":
                            get_help()
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
                            if not focus and len(words) > 0:

                                print(words)

                                if "wise" in words and "one" in words:
                                    if "alpha" in words:
                                        wise_one('gg')
                                    else:
                                        wise_one()

                                elif "repeat" in words and "mode" in words:
                                    if "on" in words:
                                        repeat = True
                                        speak("Repeat mode on")
                                    elif "off" in words:
                                        repeat = False
                                        speak("Repeat mode off")

                                elif "anat" in words and "ta" in words and "stop" in words:
                                    bot = False
                                    speak("ok, call my name when you need help, bye bye!")

                                elif "my" in words and "dhamma" in words:

                                    play_my_dhamma()                                                                    

                                elif "alpha" in words and "meditation" in words:
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

                                elif "math" in words and "meditation" in words:
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

                                elif "walking" in words and "practice" in words:
                                    walking_reward()
                                    walking_meditation_count()

                                # for martian monk only 
                                elif "monk" in words and "rule" in words:
                                    monk_rules() 
                                # for martian monk only 
                                elif "morning" in words and "practice" in words:
                                    if"one" in words:
                                        morning_practice_chanting_mode('d',1)
                                    elif "two" in words:
                                        morning_practice_chanting_mode('d',2)
                                    elif "three" in words:
                                        morning_practice_chanting_mode('d',3)
                                    else:
                                        morning_practice()

                                elif "evening" in words and "practice" in words:
                                    if "one" in words:
                                        d = 1
                                    elif "two" in words:
                                        d = 2
                                    elif "three" in words:
                                        d = 3
                                    elif "four" in words:
                                        d = 4
                                    elif "six" in words:
                                        d = 6 
                                    else:
                                        d = 0

                                    evening_practice(d)

                                elif "spelling" in words and "mode" in words:
                                    speak("spelling mode, please use international code of signals such as, c charlie but can say letter c too")
                                    spell = True
                                    focus = True
                                    yesno = False
                                    save  = False
                                    spell_words = ''

                                elif "what" in words and "time" in words:
                                    today = datetime.today().strftime('%H %M')
                                    speak("The time is " + today)
                                    
                                elif "what" in words and "day" in words:
                                    today = datetime.today().strftime('%B %A %d')
                                    speak("Today is " + today)
                                elif "buddha" in words and "day" in words:
                                    buddha_day()
                                    
                                elif "zen" in words and "story" in words:
                                    nn = sequence[n]
                                    speak("Do you want to listen to this zen story?")
                                    speak(d["zen101"][nn]["title"])
                                    focus = True
                                    zen = True

                                elif "daily" in words and "dependent" in words and "origination" in words:
                                    play_daily_dependent_origination_thai()

                                elif "buddha" in words and "thinking" in words:
                                    play_buddha_thinking_thai()

                                elif "breathing" in words and "chanting" in words:
                                    play_breathing_chanting_thai()

                                elif "nature" in words and "truth" in words and "chanting" in words:
                                    play_nature_truth_chanting_thai()

                                elif "dependent" in words and "origination" in words and "chanting" in words:
                                    play_dependent_origination_chanting_thai()

                                elif "eight" in words and "path" in words and "thai" in words:
                                    play_eight_fold_path_chanting_thai()

                                elif "eight" in words and "path" in words and "english" in words:
                                    play_eight_fold_path_chanting_english()

                                elif "chanting" in words and "english" in words:
                                    english_chating()

                                elif "chanting" in words and "thai" in words:
                                    thai_chanting()
                                                                        
                                elif "radio" in words and "play" in words:
                                    play_radio()                                
                                    
                                elif "play" in words and "mantra" in words:

                                    killPlayer() 
                                    mantra = True  
                                    focus = True                                  
                                      
                                    if "five" in words:
                                        t = 5
                                        speak("Do you want to play slow buddho mantra, push button for stop?")
                                                                               
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
                                        speak("Do you want to play 4 hours mixed mode then shutdown?")

                                    elif "eight" in words:
                                        t = 8
                                        speak("fast buddho mantra push button to stop")

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

                                elif "play" in words and "stage" in words:

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

                                elif "meditation" in words and "time" in words:
                                    meditation_time()
                                    
                                elif "buddha" in words and "dhamma" in words:
                                    buddha_dhamma()
                                            
                                elif "dhamma" in words and "play" in words:
                                    play_dhamma()

                                elif "play" in words and "speech" in words or "sutra" in words:
                                    play_sutra()
                                          
                                elif "shutdown" in words and "please" in words:
                                    shutdown()
                                    break
                                
                                elif "please" in words and "restart" in words:
                                    speak("restart the service, please wait")
                                    os.system("sudo systemctl restart myscript.service")
                                    break

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
                                        
                                elif "browse" in words and "webcam" in words:
                                    speak("open webcam on web browser")
                                    ip = get_ip()
                                    command = "export DISPLAY=:0.0; chromium-browser --incognito --start-fullscreen --start-maximized " + ip + ":8081"
                                    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                                    press_for_stop('g',proc)
                                    os.system("sudo pkill -f chromium")

                                #TEST
                                elif "buddha" in words and ("story" in words or "what" in words):
                                    speak("play buddha story")
                                    killPlayer()                
                                    try:
                                        os.system("export DISPLAY=:0.0 && vlc -f --play-and-exit buddha-story.mp4")
                                    except:
                                        speak("sorry can not play video clip")

                                elif "browse" in words and "buddhism" in words:
                                    speak("open Thai buddhism in wikipedia")
                                    command = "export DISPLAY=:0.0; chromium-browser --incognito --start-fullscreen --start-maximized https://th.wikipedia.org/wiki/ศาสนาพุทธ"
                                    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                                    press_for_stop('g',proc)
                                    os.system("sudo pkill -f chromium")

                                elif "browse" in words and "buddhist" in words and "story" in words:
                                    speak("open youtube for buddhist stories")
                                    command = "export DISPLAY=:0.0; chromium-browser --incognito --start-fullscreen --start-maximized https://www.youtube.com/watch?v=tI-hgIhFDT0&list=PLYBNr5a72-497Q3UVkpDB24W4NTCD5f2K"
                                    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                                    press_for_stop('g',proc)
                                    os.system("sudo pkill -f chromium")

                                elif "browse" in words and "meditation" in words and "technique" in words:
                                    speak("open youtube for meditation technique")
                                    command = "export DISPLAY=:0.0; chromium-browser --incognito --start-fullscreen --start-maximized https://www.youtube.com/playlist?list=PLUh8U5np7D-7FMh6ONGwnaltFppPBwTVI"
                                    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                                    press_for_stop('g',proc)
                                    os.system("sudo pkill -f chromium")
   
                                elif "help" in words and "please" in words:
                                    get_help()
                                elif "volume" in words and "up" in words:
                                    call(["amixer","-D","pulse","sset","Master","95%"])
                                    speak("set volume to 95%")
                                elif "volume" in words and "down" in words:
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

                                    if zen:
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

                                                fast_buddho('c',15)
                                                fast_buddho('gg',15)

                                                remind_right_sati()

                                                fast_buddho('off',180)
                                                
                                                ledc('off')
                                                alpha_wave(240)
                                                mantra = False
                                                focus = False

                                            elif t == 4:
                                                fast_buddho('y')

                                                remind_sati()

                                                fast_buddho('gg')

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
                                                fast_buddho('r',0)
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
                                            speak("Quit speeling mode")
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

                    else:
                        leds.update(Leds.rgb_on(Color.RED))
                        # x = rec.PartialResult()
                        # print(x)

except KeyboardInterrupt:
    print('\nDone')
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))


# For Martian Monk Bhavana practice
# twitter @MartianZenMonk