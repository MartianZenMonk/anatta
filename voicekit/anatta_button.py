import os
import sys
import time
import math
import pyttsx3
import subprocess

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


from aiy.board import Board, Led
from aiy.leds import (Leds, Pattern, PrivacyLed, RgbLeds, Color)

from datetime import datetime

import pyttsx3
engine = pyttsx3.init() # object creation
engine.setProperty('voice','english-us') 
engine.setProperty('rate', 130)
engine.setProperty('volume',0.1)

import csv
with open('myhora-buddha-2564.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

day = datetime.today().strftime('%Y%m%d')
holyday = []

for i in range(len(data)):
    if i>0:
        if(int(data[i][1])>int(day)):
            holyday.append(data[i][1])
            
# print(holyday)

def speak(text):
        print (text)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        return None

# if install espeak-ng
# sudo apt-get install synaptic (or install via this)
# sudo apt-get install mbrola mbrola-us (1-3)

# voices = ["english-en","english-us","mb-us1","us-mbrola-1","us-mbrola-2","us-mbrola-3"]

# def speakng(text,voice,*args):
#         x = 'espeak-ng -v "'+ voice + '" ' + '"' + text + '"'
#         os.system(x)
#         return None

def main():
        print('Welcome to Anatta Project, press button to play with Dhamma')
        button_press = 0
        ts1 = time.time()
        with Leds() as leds:

                print('RGB: Solid GREEN for 1 second')
                leds.update(Leds.rgb_on(Color.GREEN))
                time.sleep(1)

                print('RGB: Solid YELLOW for 1 second')
                leds.update(Leds.rgb_on(Color.YELLOW))
                time.sleep(1)

                print('RGB: Solid BLUE for 1 second')
                leds.update(Leds.rgb_on(Color.BLUE))
                time.sleep(1)

                print('RGB: Solid PURPLE for 1 second')
                leds.update(Leds.rgb_on(Color.PURPLE))
                time.sleep(1)

                print('RGB: Solid CYAN for 1 second')
                leds.update(Leds.rgb_on(Color.CYAN))
                time.sleep(1)

                print('RGB: Solid WHITE for 1 second')
                leds.update(Leds.rgb_on(Color.WHITE))
                time.sleep(1)

                print('RGB: Solid BLUE for 1 second')
                leds.update(Leds.rgb_on(Color.BLUE))
                time.sleep(1)

                print('Set blink pattern: period=500ms (2Hz)')
                leds.pattern = Pattern.blink(500)

                print('RGB: Blink GREEN for 5 seconds')
                leds.update(Leds.rgb_pattern(Color.GREEN))
                time.sleep(5)

                leds.update(Leds.rgb_on(Color.GREEN))

                with Board() as board:
                        while True:
                                board.button.wait_for_press()
                                # board.led.state = Led.ON
                                button_press += 1
                                board.button.wait_for_release()
                                # board.led.state = Led.OFF
                                ts2 = time.time()
                                if button_press == 1:
                                        if have_internet():
                                                leds.update(Leds.rgb_on(Color.WHITE))
                                                import datetime
                                                today = datetime.datetime.now() 
                                                text = "Today is "+today.strftime('%B %A %d')+" Time "+today.strftime('%H %M')
                                                speak(text)
                                                y = list(str(holyday))
                                                yy = y[2]+y[3]+y[4]+y[5]
                                                mm = y[6]+y[7]
                                                dd = y[8]+y[9]
                                                x = datetime.datetime(int(yy),int(mm),int(dd))
                                                z = x.strftime("%B %A %d")
                                                text = "Next Buddha Holy Day is "+z
                                                speak(text)   
                                                text="Listen to Tibetan Buddhist internet radio"
                                                speak(text)
                                                proc = subprocess.Popen(["mpg123","-f","2000","-q","http://199.180.72.2:9097/lamrim"])
                                        else:
                                                speak("No internet connection, do not forget to mind your breathing, mind your body movement and mind your mind.")   
                                elif button_press == 2:
                                        proc.kill()
                                        leds.update(Leds.rgb_on(Color.YELLOW))
                                        text = "English chanting"
                                        speak(text)
                                        proc = subprocess.Popen(["mpg123","-f","2000","-q","-Z","-l","0","--list","chanting.txt"]) 
                                elif button_press == 3:
                                        proc.kill()
                                        leds.update(Leds.rgb_on(Color.PURPLE))
                                        text = "Play Dhamma"
                                        speak(text)
                                        proc = subprocess.Popen(["mpg123","-f","2000","-q","-Z","-l","0","--list","dhamma.txt"])
                                elif button_press == 4:
                                        proc.kill()
                                        leds.update(Leds.rgb_on(Color.GREEN))
                                        text = "The lecture of Buddhadasa Bhikkhu"
                                        speak(text)
                                        proc = subprocess.Popen(["mpg123","-f","2000","-q","-Z","-l","0","--list","buddhadasa.txt"])
                                elif button_press == 5:
                                        proc.kill()
                                        leds.update(Leds.rgb_on(Color.GREEN))
                                        text = "The sermons of Bhikkhu P. A. Payutto"
                                        speak(text)
                                        proc = subprocess.Popen(["mpg123","-f","2000","-q","-Z","-l","0","--list","payutto.txt"])
                                elif button_press == 6:
                                        proc.kill()
                                        leds.update(Leds.rgb_on(Color.RED))
                                        text = "Our Real Home lecture by Ajahn Chah"
                                        speak(text)
                                        proc = subprocess.Popen(["mpg123","-f","2000","-q","../dataen/dhamma/Our_Real_Home.mp3"])
                                elif button_press == 7:
                                        proc.kill()
                                        leds.update(Leds.rgb_on(Color.YELLOW))
                                        text = "How to Meditation"
                                        speak(text)
                                        proc = subprocess.Popen(["mpg123","-f","2000","-q","--list","howtobhavana.txt"])
                                elif button_press == 8:
                                        proc.kill()
                                        text = "Meditation time will make 15 minutes bell sound, you may relax your self by walking then sitting. "
                                        text += "For walking, set a distance to meditate walking back and forth, your senses inwardly immersed, your mind not straying outwards. "
                                        text += "Lifting, Moving, Treading, slow moving and always mind your foot movement then you can increse your awakening sense, "
                                        text += "or free walking, just focus on Treading, "
                                        text += "For sitting, breathing in calm, breathing out down, always mind your breathing, your citta will not go around"
                                        speak(text)
                                        leds.update(Leds.rgb_on(Color.BLUE))
                                        # board.led.state = Led.ON
                                        proc = subprocess.Popen(["mpg123","-f","2000","-q","-l","0","../dataen/bell15min.mp3"])
                                else:
                                        proc.kill()
                                        os.system("sudo killall mpg123")
                                        text = "Hello Press button within 3 seconds For Exit"
                                        speak(text)
                                        t1 = time.time()
                                        board.led.state = Led.ON
                                        board.button.wait_for_press()
                                        t2 = time.time()
                                        if t2-t1 < 4:
                                                os.system("sudo killall mpg123")
                                                speak("goodbye, have a nice day.")
                                                break
                                        else:
                                                board.led.state = Led.OFF
                                                button_press = 0
                                                ts1 = time.time()
if __name__ == '__main__':
        main()

# mpg123 -f 2000 the maximum value of the amplitude is 100% which coressponds to 32768, i use this when i want to run with crontab