#!/usr/bin/env python3

import argparse
import os
import queue
import sounddevice as sd
import vosk
import sys
import json
import random
import time
import datetime as dt
import subprocess
from subprocess import call
from datetime import datetime

import psutil
import pty
import gc

import requests
from pprint import pprint
from urllib.request import urlopen
from json import load


def ipInfo(addr=''):
    
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    #response from url(if res==None then check connection)
    data = load(res)

    #will load the json response into data
    # for attr in data.keys():
    #     #will print the data line by line
    #     print(attr,' '*13+'\t->\t',data[attr])

    loc = data['loc'].split(',')
    query='lat='+loc[0]+'&lon='+loc[1]
    res=requests.get('https://fcc-weather-api.glitch.me/api/current?'+query)

    return res.json();


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


# read zenstories file
with open('../dataen/zenstories.json', 'r') as myfile:
    zdata=myfile.read()

# parse file
d = json.loads(zdata)
del zdata
gc.collect()


global pop 
global proc
bot_name = "acumen" # shall use rare vocabulary and add to list such as acumen, coronel
pop = False
bot = False
focus = False
focus_event = []

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


import csv
with open('myhora-buddha-2564.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

today = datetime.today().strftime('%Y%m%d')
holyday = []
print(len(data))
for i in range(len(data)):
    if i>0:
        if(int(data[i][1])>int(today)):
            holyday.append(data[i][1])
            
del data
gc.collect()

"""VOICE"""

# voices = ["en-us","en-gb-scotland","mb-us1","mb-us2","mb-us3"] 

#espeak
voices = ["english-us","english_rp+f3","english+m1","english+m3","english+f1","english_rp","en-scottish"]

#espeak-ng
# voices = ["en-us","en-gb-scotland","en-gb","en-029","en-gb-x-rp","en-gb-x-gbclan"] 


def speak(t,v='',*args):
        if v == '':
            v = voices[2]
        # text = 'espeak-ng -s 150 -v ' + v + ' "' + str(t) + '"'
        text = 'espeak -s 130 -v ' + v + ' "' + str(t) + '"'
        # print(text)
        os.system(text)
        return None


def clear_proc(proc,pop):
    if(pop):
        proc.kill()
        os.system("sudo killall mpg123")
    pop = False
    return pop


def get_temperature():
    w = ipInfo()
    text = 'Country '+w['sys']['country']+'. City '+w['name']+'. Temperature is '+str(w['main']['temp'])+'. Humidity is '+str(w['main']['humidity'])+'. The weather '+w['weather'][0]['description']
    speak(text) 
    return None


def play_chanting():
    speak("English chanting")
    proc = subprocess.Popen(["mpg123","-Z","-q","--list","chanting.txt"], stdin=master)      
    return proc


def buddha_story():
    lines = buddhism["buddha"][0]["content"]
    # print(lines)
    for i in range(len(lines)):
        x = int(lines[i]["voice"])
        # print(voices[x]) 
        speak(lines[i]["text"],voices[x])
    focus_event = ["vlc","-f","--video-on-top","--play-and-exit","buddha-story.mp4"]
    focus = True
    return None


def play_sermons():
    speak("play daily sermons") 
    proc = subprocess.Popen(["mpg123","-Z","-q","--list","sermons.txt"], stdin=master)  
    return proc


def play_radio():
    speak("Listen to Tibetan Buddhist internet radio") 
    proc = subprocess.Popen(["mpg123","-q","http://199.180.72.2:9097/lamrim"], stdin=master)
    return proc


def medition_time():
    speak("The meditation bell will ring every 15 minutes.") 
    proc = subprocess.Popen(["mpg123","-q","-loop","-1","bell15min.mp3"])
    return proc


def how_mindfulness():
    proc = subprocess.Popen(["mpg123","howto-mindfulness.mp3"])
    return proc


def buddha_day():
    y = list(str(holyday))
    yy = y[2]+y[3]+y[4]+y[5]
    mm = y[6]+y[7]
    dd = y[8]+y[9]
    # print(yy,mm,dd)
    
    x = dt.datetime(int(yy),int(mm),int(dd))
    z = x.strftime("%B %A %d")
    # print(holyday[0])
    speak("Next Buddha Holy day is " + z)
    return None


def zen_story():
    i = random.randint(0,len(d["zen101"])-1)
    lines = d["zen101"][i]["story"]
    speak(lines)
    for i in range(len(lines)):
        x = int(lines[i]["voice"])
        speak(lines[i]["text"],voices[x])
    return None


def play_sutra():
    i = random.randint(0,1)
    lines = sutta["sutta"][i]["content"]
    # print(lines)
    for i in range(len(lines)):
        x = int(lines[i]["voice"])
        speak(lines[i]  ["text"],voices[x])  
    return None


def buddhist_story():
    speak("play animated buddhist stories video") 
    proc = subprocess.Popen(["vlc","--random","--loop","--playlist-autostart","-f","--video-on-top","buddhiststories.xspf"], stdin=master)   
    return proc


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
    q.put(bytes(indata))

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

    with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device, dtype='int16',
                            channels=1, callback=callback):
            print('#' * 80)
            print('Hello my name is ',bot_name,' please call my name before speak to me ;)')
            print('Press Ctrl+C to stop the recording')
            print('#' * 80)
            # datetime.today().strftime('%Y%m%d')

            speak('Hello my name is '+bot_name+' please call my name before speak to me')

            words = []
            with q.mutex:
                q.queue.clear()

            master, slave = os.openpty()

            rec = vosk.KaldiRecognizer(model, args.samplerate, '["acumen begin buddha buddhist chanting coronel day hey dhamma do down eighty face how meditation mindfulness news no now on play please quiet radio reboot speak sermons seventy shutdown silent sitting sixty show sleep start stop story sutra tell temperature time to turn up volume wake walking what yes zen"]')
            # rec = vosk.KaldiRecognizer(model, args.samplerate, '["shutdown acumen coronel now sutra mindfulness dhamma buddha holy day zen buddhist story chanting sermons meditation time sleep wake up down turn on begin start stop play how to do what tell yes no walking sitting please quiet silent news when volume sixty seventy eighty show speak face","[unk]"]')
            # rec = vosk.KaldiRecognizer(model, args.samplerate)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    w = rec.Result()
                    z = json.loads(w)
                    # print(z["text"])  #print rec text
                    # print('Acumen is ',bot)
                    words = z["text"].split() 
                    # if bot_name == z["text"] or ("wake" in words and "up" in words and bot_name in words):
                    if bot_name in words and "hey" in words:
                        if pop:
                            os.write(slave, b's')
                        bot = True
                        speak('Yes sir')
                    if bot or focus:
                        print(z["text"])
                        print("Listening...")
                        if "chanting" in words:
                            proc = play_chanting()
                            pop = True
                            bot = False
                        elif focus:
                            if "yes" in words:
                                proc = subprocess.Popen(focus_event)
                                focus = False
                                focus_event = []
                            elif "no" in words:
                                focus = False
                                focus_event = []
                            bot = False
                        elif "tell" in words and "buddha" in words:
                            buddha_story()
                            bot = False
                        elif "buddhist" in words and "story" in words:
                            proc = buddhist_story()
                            pop = True
                            bot = False   
                        elif "radio" in words and "buddhist" in words:
                            proc = play_radio()
                            pop = True
                            bot = False            
                        elif "show" in words and "face" in words:
                            print("show robot face") 
                            proc = subprocess.Popen(["vlc","--play-and-exit","-f","--video-on-top","--no-video-title-show","face3.mp4"])
                            bot = False
                        elif "play" in words and ("sermons" in words or "dhamma" in words):
                            proc = play_sermons()
                            pop = True
                            bot = False                            
                        elif "meditation" in words and ("start" in words or "begin" in words or "time" in words):
                            proc = medition_time()
                            pop = True
                            bot = False                            
                        elif "mindfulness" in words and ("how" in words or "to" in words or "do" in words):
                            proc = how_mindfulness()
                            pop = True
                            bot = False                            
                        elif "stop" in words:
                            clear_proc(proc,pop)                            
                            speak("stop playing")
                            bot = False                            
                        elif "quiet" in words or "silent" in words or "sleep" in words:
                            speak("ok")
                            print("stop listening")
                            bot = False
                            if pop:
                                os.write(slave, b's') 
                        elif "volume" in words and "up" in words:
                            call(["amixer","-D","pulse","sset","Master","90%"])
                            bot = False
                            speak("set volume to 90%")
                            if pop:
                                os.write(slave, b's') 
                        elif "volume" in words and "down" in words:
                            call(["amixer","-D","pulse","sset","Master","50%"])
                            bot = False
                            speak("set volume to 50%")
                            if pop:
                                os.write(slave, b's') 
                        elif "volume" in words and "sixty" in words:
                            call(["amixer","-D","pulse","sset","Master","60%"])
                            bot = False
                            speak("set volume to 60%")
                            if pop:
                                os.write(slave, b's') 
                        elif "volume" in words and "seventy" in words:
                            call(["amixer","-D","pulse","sset","Master","70%"])
                            bot = False
                            speak("set volume to 70%")
                            if pop:
                                os.write(slave, b's')         
                        elif "volume" in words and "eighty" in words:
                            call(["amixer","-D","pulse","sset","Master","80%"])
                            bot = False
                            speak("set volume to 80%")
                            if pop:
                                os.write(slave, b's')             
                        elif "buddha" in words and "day" in words:
                            buddha_day()
                            bot = False                      
                        elif "what" in words and "time" in words:
                            today = datetime.today().strftime('%H %M')
                            print(today)
                            speak("The time is " + today)
                            bot = False
                        elif "what" in words and "day" in words:
                            today = datetime.today().strftime('%B %A %d')
                            print(today)
                            speak("Today is " + today)
                            bot = False
                        elif "what" in words and "temperature" in words:
                            get_temperature()
                            bot = False
                        elif "zen" in words and "story" in words:
                            zen_story()
                            bot = False
                        elif "play" in words and "sutra" in words:
                            play_sutra()
                            bot = False
                        elif "reboot" in words and "now" in words:
                            # print("Shutdown the system")
                            speak("reboot the system, please wait")
                            os.system("sudo reboot now")
                            break
                        elif "shutdown" in words and "now" in words:
                            # print("Shutdown the system")
                            speak("The system is Shutting down, have a nice day")
                            os.system("sudo shutdown now")
                            break
                        elif "speak" in words:
                                listToStr = ' '.join(map(str, words))
                                listToStr = listToStr.replace("speak",'')
                                speak("You said, " + listToStr)
                                bot = False
                    else:
                        x = rec.PartialResult()
                        # print(x)
                    if dump_fn is not None:
                        dump_fn.write(data)
                    # if rec1.AcceptWaveform(data):
                    #     w1 = rec1.Result()
                    #     z1 = json.loads(w1)
                    #     print(z1["text"])

except KeyboardInterrupt:
    print('\nDone')
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))
