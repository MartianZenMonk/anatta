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

    model = vosk.Model(args.model)
   
    with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device, dtype='int16',
                            channels=1, callback=callback):
            print('#' * 80)
            print('Hello my name is ',bot_name,' please call my name before speak to me ;)')
            print('Press Ctrl+C to stop')
            print('#' * 80)

            runv  = '["acumen anat ta hey begin buddha buddhist chanting close day dhamma do down eighty face holy how mantra '
            runv += 'meditation mindfulness news no now on open play please quiet sermons seventy shutdown silent sitting sixty '
            runv += 'mouse left right scroll click exit center sky star page browse technique wise speak player '
            runv += 'one two three four five six seven eight nine ten zero fifteen twenty thirty forty fifty sixty '
            runv += 'a b c d e f g h i j k l m n o p q r s t u v w x y z '
            runv += 'show sleep start stop story sutra tell time to turn up volume wake walking what when who yes zen fire fox"]'
            
            rec = vosk.KaldiRecognizer(model, args.samplerate, runv)

            stop_player()
            engine.say('Hello my name is '+ bot_name +' please call my name before speak to me')
            engine.runAndWait()
            engine.stop()
            n = 0
            global proc
            proc_ck = False
            with q.mutex:
                q.queue.clear()

            while True:
                data = q.get()
                # print(q.qsize())    
                if rec.AcceptWaveform(data):
                    w = rec.Result()
                    z = json.loads(w)
                    words = z["text"].split()

                    if not bot:
                        if len(words)==0:
                            print("[-_-]")
                        else:
                            print("[^_^]o ")
                            print(words)  
                     
                    if bot_name == z["text"] or ("hey" in words and bot_name in words):
                        bot = True
                        speak("yes sir")
                    if bot or focus:
                        print(z["text"])
                        print("Listening...")
                        if "wise" in words and "one" in words:
                            if "play" in words:
                                proc = subprocess.Popen(["mpg123","-d","3","-q","--loop","-1","../thaivoices/buddho.mp3"])
                                proc_ck = True
                                bot = False
                            elif "stop" in words:
                                if proc_ck:
                                    proc.kill()
                                    proc_ck = False
                                bot = False

                        elif "chanting" in words:
                            speak("Thai chanting")
                            proc = subprocess.Popen(["mpg123","-z","--list","THchanting.txt"])        
                            # print("Thai Chanting") 
                            # proc = subprocess.Popen(["vlc","--random","--loop","--playlist-autostart","THchanting.xspf"]) 
                            bot = False
                            motion_detect(proc)
                            clear_q()

                        elif focus:
                            if "yes" in words:
                                proc = subprocess.Popen(focus_event)
                                focus = False
                                focus_event = []
                            elif "no" in words:
                                focus = False
                                focus_event = []

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
                            focus_event = ["vlc","-f","--video-on-top","--play-and-exit","buddha-story.mp4"]
                            focus = True
                            bot = False                 
                        # elif "buddhist" in words and "story" in words:
                        #     print("play animated buddhist stories video") 
                        #     proc = subprocess.Popen(["vlc","--random","--loop","--playlist-autostart","-f","--video-on-top","buddhiststories.xspf"])
                        #     bot = False
                        # elif "show" in words and "face" in words:
                        #     print("show robot face") 
                        #     proc = subprocess.Popen(["vlc","--play-and-exit","-f","--video-on-top","--no-video-title-show","face3.mp4"])
                        #     bot = False
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
                        elif "stop" in words and "player" in words:
                            stop_player()
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
