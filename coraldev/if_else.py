#!/usr/bin/env python3

import argparse
import os
import queue
import sounddevice as sd
import vosk
import sys
import json
import random

import subprocess
from subprocess import call
from datetime import datetime


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
            
# print(holyday)

"""VOICE"""

# voices = ["en-us","en-gb-scotland","mb-us1","mb-us2","mb-us3"] 

#espeak
voices = ["english-us","english_rp+f3","english+m1","english+m3","english+f1","english_rp","en-scottish"]

#espeak-ng
# voices = ["en-us","en-gb-scotland","en-gb","en-029","en-gb-x-rp","en-gb-x-gbclan"] 


def speak(t,v='',*args):
        if v == '':
            v = voices[2]
        # text = 'speak-ng -s 150 -v ' + v + ' "' + str(t) + '"'
        text = 'espeak -s 130 -v ' + v + ' "' + str(t) + '"'
        # print(text)
        os.system(text)
        return None

zen = {
    "zenstories":[
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
bot_name = "acumen" # shall use rare vocabulary and add to list such as acumen, coronel
bot = False
focus = False
focus_event = []

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
            datetime.today().strftime('%Y%m%d')

            speak('Hello my name is '+bot_name+' please call my name before speak to me')
            
            proc = 0

            rec = vosk.KaldiRecognizer(model, args.samplerate, '["acumen begin buddha buddhist chanting coronel day dhamma do down eighty face holy how meditation mindfulness news no now on play please quiet sermons seventy shutdown silent sitting sixty show sleep start stop story sutra tell time to turn up volume wake walking what yes zen","[unk]"]')
            # rec = vosk.KaldiRecognizer(model, args.samplerate, '["shutdown acumen coronel now sutra mindfulness dhamma buddha holy day zen buddhist story chanting sermons meditation time sleep wake up down turn on begin start stop play how to do what tell yes no walking sitting please quiet silent news when volume sixty seventy eighty show face","[unk]"]')
            # rec1 = vosk.KaldiRecognizer(model, args.samplerate)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    w = rec.Result()
                    z = json.loads(w)
                    # print(z["text"])  #print rec text
                    # print('Acumen is ',bot)
                    words = z["text"].split() 
                    if bot_name == z["text"] or ("wake" in words and "up" in words and bot_name in words):
                        bot = True
                        speak('Yes sir')
                    if bot or focus:
                        print(z["text"])
                        print("Listening...")
                        if "chanting" in words:
                            print("start playing") 
                            # proc = subprocess.Popen(["vlc","--random","--loop","--playlist-autostart","chanting.xspf"])
                            proc = subprocess.Popen(["mpg123","-Z","-l","0","-q","--list","chanting.txt"])  
                            bot = False  
                        elif focus:
                            if "yes" in words:
                                proc = subprocess.Popen(focus_event)
                                focus = False
                                focus_event = []
                            elif "no" in words:
                                focus = False
                                focus_event = []
                        elif "tell" in words and "buddha" in words:
                            lines = buddhism["buddha"][0]["content"]
                            # print(lines)
                            for i in range(len(lines)):
                                x = int(lines[i]["voice"])
                                # print(voices[x]) 
                                speak(lines[i]["text"],voices[x])
                            focus_event = ["vlc","-f","--video-on-top","--play-and-exit","buddha-story.mp4"]
                            focus = True
                            bot = False                 
                        elif "buddhist" in words and "story" in words:
                            print("play animated buddhist stories video") 
                            proc = subprocess.Popen(["vlc","--random","--loop","--playlist-autostart","-f","--video-on-top","buddhiststories.xspf"])
                            bot = False
                        elif "show" in words and "face" in words:
                            print("show robot face") 
                            proc = subprocess.Popen(["vlc","--play-and-exit","-f","--video-on-top","--no-video-title-show","face3.mp4"])
                            bot = False
                        elif "play" in words and ("sermons" in words or "dhamma" in words):
                            print("play daily sermons") 
                            proc = subprocess.Popen(["vlc","--random","--loop","--playlist-autostart","sermons.xspf"])
                            bot = False
                        elif "meditation" in words and ("start" in words or "begin" in words or "time" in words):
                            print("start meditation bell ring every 15 minutes") 
                            proc = subprocess.Popen(["vlc","--loop","bell15min.mp3"])
                            bot = False
                        elif "mindfulness" in words and ("how" in words or "to" in words or "do" in words):
                            print("start meditation bell ring every 15 minutes") 
                            proc = subprocess.Popen(["vlc","howto-mindfulness.mp3"])
                            bot = False
                        elif "stop" in words:
                            print("stop playing")
                            # proc.kill()
                            os.system("killall vlc")
                            os.system("killall mpg123")
                            bot = False
                        elif "quiet" in words or "silent" in words or "sleep" in words:
                            print("stop listening")
                            bot = False
                        elif "volume" in words and "up" in words:
                            call(["amixer","-D","pulse","sset","Master","90%"])
                            bot = False
                            speak("set volume to 90%") 
                        elif "volume" in words and "down" in words:
                            call(["amixer","-D","pulse","sset","Master","50%"])
                            bot = False
                            speak("set volume to 50%")
                        elif "volume" in words and "sixty" in words:
                            call(["amixer","-D","pulse","sset","Master","60%"])
                            bot = False
                            speak("set volume to 60%")
                        elif "volume" in words and "seventy" in words:
                            call(["amixer","-D","pulse","sset","Master","70%"])
                            bot = False
                            speak("set volume to 70%")        
                        elif "volume" in words and "eighty" in words:
                            call(["amixer","-D","pulse","sset","Master","80%"])
                            bot = False
                            speak("set volume to 80%")            
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
                            speak("Next Buddha Holy day is " + z)
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
                        elif "zen" in words and "story" in words:
                            i = random.randint(0,4)
                            lines = zen["zenstories"][i]["story"]
                            # print(lines)
                            for i in range(len(lines)):
                                x = int(lines[i]["voice"])
                                speak(lines[i]["text"],voices[x])
                                bot = False
                        elif "play" in words and "sutra" in words:
                            i = random.randint(0,1)
                            lines = sutta["sutta"][i]["content"]
                            # print(lines)
                            for i in range(len(lines)):
                                x = int(lines[i]["voice"])
                                speak(lines[i]["text"],voices[x])
                                bot = False
                        elif "shutdown" in words and "now" in words:
                            # print("Shutdown the system")
                            os.system("sudo killall mpg123")
                            speak("The system is Shutting down")
                            os.system("sudo shutdown now")
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
