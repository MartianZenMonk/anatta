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



# flite Voices available: kal awb_time kal16 awb rms slt  
def speakf(v,t,*args):
        os.system('flite -voice ' + v + ' -t "' + str(t) + '"')
        return None

voices = ["kal", "slt", "rms", "awb", "awb_time", "kal16"]


d = {
    "zen101":[
        {"title":"A cup of tea",
        "story":[
            {"voice":"1","text":"Nan-in, a Japanese master during the Meiji era (1868-1912) received a university professor who came to inquire about Zen."},
            {"voice":"1","text":"Nan-in saved tea. He poured his visitor's cup full, and then kept on pouring."},
            {"voice":"1","text":"The professor watched the overflow until he no longer could restrain himself."},
            {"voice":"2","text":"It is overfull. No more will go in"},
            {"voice":"3","text":"Like this cup,You are full of your own opinions and speculations. How can I show you Zen unless you first empty your cup?"},
            ]
        },
        {"title":"Is That So?",
        "story":[
            {"voice":"1","text":"The Zen master Hakuin was praised by his neighbors as one living a pure life."},
            {"voice":"1","text":"A beautiful Japanese girl whose parents owned a food store lived near him. Suddenly, without any warning her parents discovered she was with child."},
            {"voice":"1","text":"This made her parents angry. She would not confess who the man was, but after much harassment at last named Hakuin."},
            {"voice":"1","text":"In great anger the parents went to the master. 'Is that so?' was all he would say."},
            {"voice":"1","text":"After the child was born it was brought to Hakuin. By this time he had lost his reputation, which did not trouble him, but good care of the child. He obtained milk from his neighbors and everything else the little one needed."},
            {"voice":"1","text":"A year later the girl-mother could stand it no longer. She told her parents the truth - that the real father of the child was a in the fish market."},
            {"voice":"1","text":"The mother and father of the girl at once went to Hakuin to ask his forgiveness, to apologize at length, and to get the child back again."},
            {"voice":"1","text":"Hakuin was willing. In yielding the child, all he said was"},
            {"voice":"2","text":"Is that so?"}
            ]
        },
        {"title":"The Moon cannot be Stolen",
        "story":[
            {"voice":"1","text":"Ryokan, a Zen master, lived the simplest kind of life in a little hut at the foot of a mountain. One evening a thief visited the hut only to discover there was nothing in it to stea1."},
            {"voice":"1","text":"Ryokan returned and caught him."},
            {"voice":"2","text":"You may have come a long way to visit me and you should not return empty-handed. Please take my clothes as a gift."},
            {"voice":"1","text":"The thief was bewildered. He took the clothes and slunk away.Ryokan sat naked, watching the moon."},
            {"voice":"2","text":"Poor fellow, I wish I could give him this beautiful moon."},
            {"voice":"1","text":"No one can steal your beautiful heart"}
            ]
        },
        {"title":"Muddy Road",
        "story":[
            {"voice":"1","text":"Tanzan and Ekido were once traveling together down a muddy road. A heavy rain was still falling."},
            {"voice":"1","text":"Coming around a bend, they met a lovely girl in a silk kimono and sash, unable to cross the intersection."},
            {"voice":"2","text":"Come on, girl"},
            {"voice":"1","text":"said Tanzan at once. Lifting her in his arms, he carried her over the mud."},
            {"voice":"1","text":"Ekido did not speak again until that night when they reached a lodging temple. Then he no longer could restrain himself."},
            {"voice":"3","text":"We monks don't go near females, especially not young and lovely ones. It is dangerous. Why did you do that?"},
            {"voice":"2","text":"I left the girl there, Are you still carrying her?"}
            ]
        },
        {"title":"Learning to be Silent",
        "story":[
            {"voice":"1","text":"The pupils of the Tendai School used to study meditation before Zen entered Japan. Four of them who were intimate friends promised one another to observe seven days of silence."},
            {"voice":"1","text":"On the first day all were silent Their meditation had begun auspiciously, but when night came and the oil-lamps were growing dim one of the pupils could not help exclaiming to a servant"},
            {"voice":"2","text":"Fix those lamps"},
            {"voice":"1","text":"The second pupil was surprised to hear the first one talk."},
            {"voice":"3","text":"We are not supposed to say a word"},
            {"voice":"4","text":"You two are stupid. Why did you talk?"},
            {"voice":"1","text":"asked the third"},
            {"voice":"5","text":"I am the only one who has not talked"},
            {"voice":"1","text":"muttered the fourth pupil."}
            ]
        }
        ]
    }

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
    if q.qsize() > 30:
        with q.mutex:
            q.queue.clear()
    else:
        q.put(bytes(indata))    


def press_for_stop():
    leds.update(Leds.rgb_on(Color.WHITE)) 
    board.button.wait_for_press()
    proc.kill()
    return None


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
            print(args.samplerate)
            print(args.device)

            speak("Welcome to Anat ta Project, your Buddhist true friend ever")

            y = list(str(holyday))
            yy = y[2]+y[3]+y[4]+y[5]
            mm = y[6]+y[7]
            dd = y[8]+y[9]
            x = dt.datetime(int(yy), int(mm), int(dd))
            # z = x.strftime("%B %A %d")
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

            rec = vosk.KaldiRecognizer(model, args.samplerate,'["acumen me zen story lord buddha what time day play dhamma meditation radio start chanting speak stop turn on off exit shutdown sutra help"]')
            
            with q.mutex:
                q.queue.clear()

            while True:
                data = q.get()
                print(q.qsize())       
                
                words = []
                with Leds() as leds:

                    if rec.AcceptWaveform(data):
                        w = rec.Result()
                        z = json.loads(w)
                        print(z["text"])
                        words += z["text"].split()
                        
                        with Board() as board:

                            if len(words) > 0:
                                leds.update(Leds.rgb_on(Color.YELLOW)) 
                            
                            if "what" in words and "time" in words:
                                if find_name('mpg123'):
                                    proc.kill()
                                today = datetime.today().strftime('%H %M')
                                print(today)
                                engine.say("The time is " + today)
                                engine.runAndWait()
                                engine.stop()
                            elif "what" in words and "day" in words:
                                if find_name('mpg123'):
                                    proc.kill()
                                today = datetime.today().strftime('%B %A %d')
                                print(today)
                                engine.say("Today is " + today)
                                engine.runAndWait()
                                engine.stop()
                            elif "zen" in words and "story" in words:
                                if find_name('mpg123'):
                                    proc.kill()
                                n = random.randint(0,4)
                                speak(d["zen101"][n]["title"])
                                lines = d["zen101"][n]["story"]
                                # print(lines)
                                for i in range(len(lines)):
                                    x = int(lines[i]["voice"])
                                    # speakf(voices[x], lines[i]["text"])
                                    # print(voices[x])
                                    engine.setProperty('voice',es_voices[x]) 
                                    engine.say(lines[i]["text"])
                                    engine.runAndWait()
                                    engine.stop()
                            elif "chanting" in words:
                                if find_name('mpg123'):
                                    os.system("killall mpg123")
                                speak("Thai chanting")
                                proc = subprocess.Popen(["mpg123","-f","1000","-C","-Z","--list","THchanting.txt"], stdin=master)
                                press_for_stop()

                            elif "radio" in words:
                                if find_name('mpg123'):
                                    os.system("killall mpg123")
                                if have_internet():
                                    speak("Tibetan Buddhist internet radio")
                                    proc = subprocess.Popen(["mpg123","-f","2100","-q","http://199.180.72.2:9097/lamrim"])
                                    press_for_stop()
                                else:
                                    speak("sorry no internet connection")

                            elif "lord" in words and "buddha" in words:
                                if find_name('mpg123'):
                                    os.system("killall mpg123")
                                speak("buddho mantra")
                                proc = subprocess.Popen(["mpg123","-d","3","-f","1000","-q","--loop","-1","../thaivoices/buddho.mp3"])
                                press_for_stop()

                            elif "meditation" in words:
                                if find_name('mpg123'):
                                    os.system("killall mpg123")
                                speak("15 minutes meditation Bell")
                                proc = subprocess.Popen(["mpg123","-f","2100","-q","--loop","-1","../dataen/bell15min.mp3"])
                                press_for_stop()

                            elif "buddha" in words and "dhamma" in words:
                                if find_name('mpg123'):
                                    os.system("killall mpg123")
                                speak("Buddha dhamma")
                                proc = subprocess.Popen(["mpg123","-f","2100","-q","-Z","--list","THbuddhadham.txt"]) 
                                press_for_stop()
                                
                            elif "dhamma" in words and "play" in words:
                                if find_name('mpg123'):
                                    os.system("killall mpg123")
                                proc = subprocess.Popen(["mpg123","-f","1000","-C","-Z","--list","THdhamma4all.txt"], stdin=master)
                                press_for_stop()

                            elif "sutra" in words and "play" in words:
                                if find_name('mpg123'):
                                    os.system("killall mpg123")
                                os.system("mpg123 -f 1000 ../datath/sutta/moggallana.mp3")
                                proc = subprocess.Popen(["mpg123","-f","1000","-C","-Z","--list","sutra.txt"], stdin=master)
                                press_for_stop()

                            elif "stop" in words or "acumen" in words:
                                if find_name('mpg123'):
                                    proc.kill()
                                    
                            elif "exit" in words:
                                if find_name('mpg123'):
                                    proc.kill()
                                speak("Exit voices control mode")
                                break
                            elif "shutdown" in words:
                                if find_name('mpg123'):
                                    proc.kill()
                                speak("The system is shutting down, wait until the green light in the box turn off")
                                # speakf("rms","The system is shutting down, wait until the green light in the box turn off")
                                board.led.state = Led.OFF
                                os.system("sudo shutdown now")
                                break
                            elif "speak" in words:
                                listToStr = ' '.join(map(str, words))
                                listToStr = listToStr.replace("speak",'')
                                speak("You said, " + listToStr)
                            elif "help" in words and "me" in words:
                                text = "words you can say are chanting, meditaion, radio, lord buddha, buddha dhamma, play dhamma"
                                text += ", play sutra, what time, what day, zen story, shutdown"
                                speak(text)
                                time.sleep(3)
                                with q.mutex:
                                    q.queue.clear()


                    else:
                        leds.update(Leds.rgb_on(Color.RED))
                        x = rec.PartialResult()
                        # print(x)
                    if dump_fn is not None:
                        dump_fn.write(data)

except KeyboardInterrupt:
    print('\nDone')
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))
