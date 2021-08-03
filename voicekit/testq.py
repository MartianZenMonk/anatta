#!/usr/bin/env python3

import argparse
import os
import queue
import sounddevice as sd
import vosk
import sys
import json
import math
import numpy as np
import random
import subprocess
import pty
import gc
import time
import csv
from subprocess import call
import socket
import cv2

import datetime as dt
from datetime import datetime
from aiy.board import Board, Led
from aiy.leds import (Leds, Pattern, PrivacyLed, RgbLeds, Color)

import psutil

# sd._terminate()
# time.sleep(5)
# sd._initialize()
# sd.default.latency = 'low'

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


es_voices = ["englisg+f1","english+f2","english+m1","english+m3","english+m2","english_rp+m2"]


def espeak(t,v='',s='130',a='10',*args):
        if v == '':
            v = es_voices[2]
        text = 'espeak -s ' + s + ' -a ' + a + ' -v ' + v + ' "' + str(t) + '"'
        print(t)
        os.system(text)
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
    if q.qsize() > 25:
        with q.mutex:
            q.queue.clear()
    else:
        q.put(bytes(indata))    


def press_for_stop(c=''):
    if c == 'r':
        leds.update(Leds.rgb_on(Color.RED))
    elif c == 'g':
        leds.update(Leds.rgb_on(Color.GREEN))
    elif c == 'b':
        leds.update(Leds.rgb_on(Color.BLUE))
    else:
        leds.update(Leds.rgb_on(Color.WHITE))

    board.button.wait_for_press()
    proc.kill()
    with q.mutex:
        q.queue.clear()
    return None


def get_help():
    text = "words you can say are Thai chanting, meditaion time, play radio, play mantra 0 to 6, play 1 3 6 stage, buddha dhamma, play dhamma"
    text += ", play sutra, what time, what day, buddha day, zen story, please shutdown"
    speak(text)
    time.sleep(3)
    with q.mutex:
        q.queue.clear()
    return None


def shutdown():
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
def motion_detect():
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
            if w*h > 250000:
                bk = True

        # Appending status of motion
        motion_list.append(motion)

        if bk:
            break

        #cv2.imshow("Gray Frame", gray)
        #cv2.imshow("Difference Frame", diff_frame)
        #cv2.imshow("Threshold Frame", thresh_frame)
        #cv2.imshow("Color Frame", frame)
    proc.kill()
        
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

# read zenstories file
with open('zenstories.json', 'r') as myfile:
    zdata=myfile.read()

# parse file
d = json.loads(zdata)
del zdata
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
    '-f', '--filename', type=str, metavar='FILENAME',
    help='audio file to store recording to')
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

    if args.filename:
        dump_fn = open(args.filename, "wb")
    else:
        dump_fn = None

    # args.device = 0

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
            os.system('espeak -s 130 -a 5 -v "english-us" "Nothing is worth insisting on"')
            os.system('mpg123 -q -f 1000 ../thaivoices/hello.mp3')

            v =  '["please zen story lord buddha buddhist buddhism what time day play help dhamma meditation english radio start light '
            v += 'browse chanting mantra say speak stop volume turn on off exit shutdown now thai lyric ip address sutra up down breathing '
            v += 'one two three four five six seven eight nine ten zero fifteen twenty thirty forty fifty sixty red green blue yellow '
            v += 'yes no ok coca cola stage fold path nature truth dependent origination webcam loop daily life thinking"]'

            rec = vosk.KaldiRecognizer(model, args.samplerate,v)

            del v
            gc.collect()

            focus = False
            zen = False
            
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
                        if len(words) > 0:
                            leds.update(Leds.rgb_on(Color.YELLOW))
                            print(words) 
                        
                        with Board() as board:

                            if not focus:

                                if "what" in words and "time" in words:
                                    today = datetime.today().strftime('%H %M')
                                    speak("The time is " + today)
                                    
                                elif "what" in words and "day" in words:
                                    today = datetime.today().strftime('%B %A %d')
                                    speak("Today is " + today)
                                elif "buddha" in words and "day" in words:
                                    buddha_day()
                                    
                                elif "zen" in words and "story" in words:
                                    n = random.randint(0,len(d["zen101"])-1)
                                    speak(d["zen101"][n]["title"])
                                    focus = True
                                    zen = True

                                elif "daily" in words and "life" in words and "dependent" in words and "origination" in words:
                                    killPlayer()  
                                    speak("Dependent Origination Application in Everyday Life")
                                    proc = subprocess.Popen(["mpg123","-f","2000","../datath/buddhadham/paticcasamuppda.mp3"])
                                    press_for_stop()

                                elif "buddha" in words and "thinking" in words and "play" in words:
                                    killPlayer()  
                                    speak("Dependent Origination Application in Everyday Life")
                                    proc = subprocess.Popen(["mpg123","-f","2000","../datath/buddhadham/yoniso.mp3"])
                                    press_for_stop()

                                elif "breathing" in words and "chanting" in words:
                                    killPlayer()
                                    if "loop" in words:
                                        speak("Thai Anapanasati chanting")
                                        proc = subprocess.Popen(["mpg123","-f","2000","-C","--loop","-1","../datath/chanting/anapanasati-cut.mp3"], stdin=master)
                                        press_for_stop()
                                    else:
                                        subprocess.run(["mpg123","-f","2000","../datath/chanting/anapanasati-cut.mp3"])

                                elif "nature" in words and "truth" in words and "chanting" in words:
                                    killPlayer()
                                    speak("Thai Dhamma Ni yam chanting")
                                    proc = subprocess.Popen(["mpg123","-f","2000","-C","--loop","-1","../datath/chanting/dhammaniyam.mp3"], stdin=master)
                                    motion_detect()

                                elif "dependent" in words and "origination" in words and "chanting" in words:
                                    killPlayer()  
                                    speak("Thai Itup paj ja ya ta Pa tij ja sa mup path chanting")
                                    proc = subprocess.Popen(["mpg123","-f","2000","-C","--loop","-1","../datath/chanting/ituppajjayata.mp3"], stdin=master)
                                    press_for_stop()

                                elif "eight" in words and "fold" in words and "path" in words and "thai" in words:
                                    killPlayer()   
                                    speak("Thai Noble 8 fold path chanting")
                                    proc = subprocess.Popen(["mpg123","-f","2000","-C","--loop","-1","../datath/chanting/8.mp3"], stdin=master)
                                    press_for_stop()

                                elif "eight" in words and "fold" in words and "path" in words and "english" in words:
                                    killPlayer()   
                                    speak("English Noble 8 fold path chanting")
                                    proc = subprocess.Popen(["mpg123","-f","4000","-C","--loop","-1","../dataen/chanting/noble8fold.mp3"], stdin=master)
                                    press_for_stop()

                                elif "chanting" in words and "english" in words:
                                    killPlayer()  
                                    speak("English chanting")
                                    subprocess.run(["mpg123","-f","1500","-C","--list","chanting.txt"])

                                elif "chanting" in words and "thai" in words:
                                    killPlayer()   
                                    speak("Thai chanting")
                                    proc = subprocess.Popen(["mpg123","-f","1500","-C","-Z","--list","THchanting.txt"], stdin=master)
                                    press_for_stop()
                                                                        
                                elif "radio" in words and "play" in words:
                                    killPlayer()
                                        
                                    if have_internet():
                                        speak("Tibetan Buddhist internet radio")
                                        proc = subprocess.Popen(["mpg123","-f","2000","-q","http://199.180.72.2:9097/lamrim"])
                                        press_for_stop()
                                    else:
                                        speak("sorry no internet connection")

                                elif "play" in words and "mantra" in words and "zero" in words:
                                    killPlayer()
                                    speak("buddho mantra")
                                    leds.update(Leds.rgb_on(Color.BLUE)) 
                                    proc = subprocess.Popen(["mpg123","-f","1000","-q","--loop","-1","../thaivoices/buddho0.mp3"])
                                    press_for_stop('g')
                                    
                                elif "play" in words and "mantra" in words and "one" in words:
                                    killPlayer()    
                                    speak("buddho mantra")
                                    leds.update(Leds.rgb_on(Color.BLUE)) 
                                    proc = subprocess.Popen(["mpg123","-d","3","-f","1000","-q","--loop","-1","../thaivoices/buddho.mp3"])
                                    press_for_stop('r')
                                    
                                elif "play" in words and "mantra" in words and "two" in words:
                                    killPlayer()   
                                    if "ten" in words:
                                        t = 10 
                                    elif "fiftheen" in words:
                                        t = 15
                                    elif "twenty" in words:
                                        t = 20
                                    else:
                                        t = 30
                                    speak(str(t) + " minutes buddho mantra")
                                    leds.update(Leds.rgb_on(Color.BLUE)) 
                                    proc = subprocess.Popen(["mpg123","-d","3","-f","1000","-q","--loop","-1","../thaivoices/buddho.mp3"])
                                    time.sleep(t*60)
                                    proc.kill()
                                    
                                elif "play" in words and "mantra" in words and "three" in words:
                                    killPlayer()   
                                    speak("one hour buddho mantra")
                                    leds.update(Leds.rgb_on(Color.RED)) 
                                    proc = subprocess.Popen(["mpg123","-d","3","-f","1000","-q","--loop","-1","../thaivoices/buddho.mp3"])
                                    time.sleep(1800)
                                    proc.kill()
                                    leds.update(Leds.rgb_on(Color.GREEN)) 
                                    proc = subprocess.Popen(["mpg123","-d","3","-f","1000","-q","--loop","-1","../thaivoices/buddho.mp3"])
                                    time.sleep(1800)
                                    proc.kill()
                                    
                                elif "play" in words and "mantra" in words and "four" in words:
                                    killPlayer()   
                                    speak("one hour buddho mantra then shutdown")
                                    leds.update(Leds.rgb_on(Color.GREEN)) 
                                    proc = subprocess.Popen(["mpg123","-d","3","-f","1000","-q","--loop","-1","../thaivoices/buddho.mp3"])
                                    time.sleep(1800)
                                    proc.kill()
                                    speak("Do not forget to mind your breathing, mind your body movement and mind your mind.")
                                    text = " ../thaivoices/sati.mp3"
                                    os.system("mpg123 -q -f 2000 "+text)
                                    leds.update(Leds.rgb_on(Color.RED)) 
                                    proc = subprocess.Popen(["mpg123","-d","3","-f","1000","-q","--loop","-1","../thaivoices/buddho.mp3"])
                                    time.sleep(1800)
                                    proc.kill()
                                    shutdown()
                                    break  
                                
                                elif "play" in words and "mantra" in words and "six" in words:
                                    killPlayer()    
                                    speak("4 hours buddho mantra then shutdown")
                                    leds.update(Leds.rgb_on(Color.YELLOW)) 
                                    proc = subprocess.Popen(["mpg123","-d","3","-f","1500","-q","--loop","-1","../thaivoices/buddho.mp3"])
                                    time.sleep(1800)
                                    proc.kill()
                                    speak("Do not forget to mind your breathing, mind your body movement and mind your mind.")
                                    text = " ../thaivoices/sati.mp3"
                                    os.system("mpg123 -q -f 2000 "+text)
                                    leds.update(Leds.rgb_on(Color.GREEN)) 
                                    proc = subprocess.Popen(["mpg123","-d","3","-f","1500","-q","--loop","-1","../thaivoices/buddho.mp3"])
                                    time.sleep(1800)
                                    proc.kill()
                                    speak("Ardent, fully aware, and mindful, after removing avarice and sorrow regarding the world.")
                                    text = " ../thaivoices/right_sati.mp3"
                                    os.system("mpg123 -q -f 2000 "+text)
                                    leds.update(Leds.rgb_on(Color.RED)) 
                                    proc = subprocess.Popen(["mpg123","-d","3","-f","1000","-q","--loop","-1","../thaivoices/buddho.mp3"])
                                    time.sleep(10800)
                                    proc.kill()
                                    board.led.state = Led.OFF
                                    os.system("sudo shutdown now")
                                    # shutdown()
                                    break  

                                elif "play" in words and "one" in words and "stage" in words:
                                    killPlayer()
                                    th_right = thwords(['ขวา','ย่าง','หนอ'])
                                    th_left = thwords(['ซ้าย','ย่าง','หนอ'])
                                    en_right = enwords(['right','goes','thus'])
                                    en_left = enwords(['left','goes','thus'])

                                    if "ten" in words:
                                        t = 10 
                                    elif "fiftheen" in words:
                                        t = 15
                                    elif "twenty" in words:
                                        t = 20
                                    else:
                                        t = 30

                                    speak(str(t) + " minutes 1 stage walking practice")

                                    if "english" in words:
                                        leds.update(Leds.rgb_on(Color.GREEN))  
                                        proc = subprocess.Popen(["mpg123","-f","1000","-q","--loop","-1","../dataen/one_stage.mp3"])
                                        time.sleep(60*t)
                                        proc.kill()
                                    else:
                                        leds.update(Leds.rgb_on(Color.BLUE))
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
                                    del en_left
                                    del en_right
                                    gc.collect()

                                elif "play" in words and "three" in words and "stage" in words:
                                    killPlayer()    
                                    speak("15 minutes 3 stages walking practice")
                                    th_stage = thwords(["ยกหนอ","ย่างหนอ","เหยียบหนอ"])
                                    en_stage = enwords(['lifting','moving','treading'])
                                    leds.update(Leds.rgb_on(Color.BLUE))
                                    timeout = time.time() + 60*15   # 15 minutes from now
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
                                    del en_stage
                                    gc.collect() 

                                elif "play" in words and "six" in words and "stage" in words:
                                    killPlayer()   
                                    speak("5 minutes 6 stages walking practice")
                                    th_stage = thwords(["ยกส้นหนอ","ยกหนอ","ย่างหนอ","ลงหนอ","ถูกหนอ","กดหนอ"])
                                    en_stage = enwords(["heelup","lifting","moving","lowering","touching","pressing"])
                                    leds.update(Leds.rgb_on(Color.BLUE))
                                    timeout = time.time() + 60*5   # 5 minutes from now
                                    
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
                                    del en_stage
                                    gc.collect()                     

                                elif "meditation" in words and "time" in words:
                                    killPlayer()   
                                    text = "Meditation time will make 15 minutes bell sound, you may relax your self by walking then sitting. "
                                    text += "For walking, set a distance to meditate walking back and forth, your senses inwardly immersed, your mind not straying outwards. "
                                    text += "Lifting, Moving, Treading, slow moving and always mind your foot movement then you can increse your awakening sense, "
                                    text += "or free walking, just focus on Treading, "
                                    text += "For sitting, breathing in calm, breathing out down, always mind your breathing, your citta will not go around"
                                    speak(text)
                                    proc = subprocess.Popen(["mpg123","-f","1500","-q","--loop","-1","../dataen/bell15min.mp3"])
                                    press_for_stop('g')
                                    del text
                                    gc.collect()
                                    
                                elif "buddha" in words and "dhamma" in words:
                                    killPlayer()    
                                    speak("Buddha dhamma")
                                    proc = subprocess.Popen(["mpg123","-f","1500","-q","-Z","--list","THbuddhadham.txt"]) 
                                    press_for_stop('b')
                                            
                                elif "dhamma" in words and "play" in words:
                                    killPlayer()   
                                    speakThai(['ฟัง','ธรรม','ค่ะ'])
                                    proc = subprocess.Popen(["mpg123","-f","1500","-C","-z","--list","THdhamma4all.txt"], stdin=master)
                                    leds.update(Leds.rgb_on(Color.YELLOW))
                                    board.button.wait_for_press()
                                    os.write(slave, b'f')
                                    leds.update(Leds.rgb_on(Color.RED))
                                    board.button.wait_for_press()
                                    os.write(slave, b'f')
                                    press_for_stop()

                                elif "sutra" in words and "play" in words:
                                    killPlayer()    
                                    os.system("mpg123 -f 1000 ../datath/sutta/moggallana.mp3")
                                    proc = subprocess.Popen(["mpg123","-f","1000","-C","-Z","--list","sutra.txt"], stdin=master)
                                    press_for_stop('r') 
                                          
                                elif "shutdown" in words and "please" in words:
                                    shutdown()
                                    break
                                
                                #PLAY
                                elif "light" in words and "on" in words:
                                    if "red" in words:
                                        leds.update(Leds.rgb_on(Color.RED))
                                    elif "green" in words:
                                        leds.update(Leds.rgb_on(Color.GREEN))
                                    elif "blue" in words:
                                        leds.update(Leds.rgb_on(Color.BLUE))
                                    elif "yellow" in words:
                                        leds.update(Leds.rgb_on(Color.YELLOW))
                                    else:
                                        leds.update(Leds.rgb_on(Color.WHITE))
                                    board.button.wait_for_press() 
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
                                    command = "export DISPLAY=:0.0; chromium-browser --start-fullscreen --start-maximized " + ip + ":8081"
                                    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                                    press_for_stop()
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
                                    command = "export DISPLAY=:0.0; chromium-browser --start-fullscreen --start-maximized https://th.wikipedia.org/wiki/ศาสนาพุทธ"
                                    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                                    press_for_stop()
                                    os.system("sudo pkill -f chromium")

                                elif "browse" in words and "buddhist" in words and "story" in words:
                                    speak("open youtube for buddhist stories")
                                    command = "export DISPLAY=:0.0; chromium-browser --start-fullscreen --start-maximized https://www.youtube.com/watch?v=tI-hgIhFDT0&list=PLYBNr5a72-497Q3UVkpDB24W4NTCD5f2K"
                                    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                                    press_for_stop()
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
                                    time.sleep(3)
                                    with q.mutex:
                                        q.queue.clear()

                                elif len(words) > 0:
                                    listToStr = ' '.join(map(str, words))
                                    speak("words i heard , " + listToStr)
                                    time.sleep(3)
                                    with q.mutex:
                                        q.queue.clear()
                                
                            else:

                                if zen:
                                    if "no" in words:
                                        n = random.randint(0,len(d["zen101"])-1)
                                        speak(d["zen101"][n]["title"])
                                    elif "yes" in words:
                                        lines = d["zen101"][n]["story"]
                                        # print(lines)
                                        for i in range(len(lines)):
                                            x = int(lines[i]["voice"])
                                            # speakf(voices[x], lines[i]["text"])
                                            # print(voices[x])
                                            engine.setProperty('voice',es_voices[x]) 
                                            speak(lines[i]["text"])
                                        zen = False
                                        focus = False

                                                           
                                

                    else:
                        leds.update(Leds.rgb_on(Color.RED))
                        # x = rec.PartialResult()
                        # print(x)
                    if dump_fn is not None:
                        dump_fn.write(data)

except KeyboardInterrupt:
    print('\nDone')
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))


# For Martian Monk Bhavana practice
# twitter @MartianZenMonk