import os
import sys
import time
import math
import pyttsx3
import subprocess
import pyttsx3
import csv

from aiy.board import Board, Led
from aiy.leds import (Leds, Pattern, PrivacyLed, RgbLeds, Color)

from datetime import datetime


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

# podcast
# import feedparser
# import webbrowser

# # feed = feedparser.parse("https://dharmachakra.libsyn.com/rss")  
# feed = feedparser.parse("https://dharmabytes.libsyn.com/rss")

# feed_entries = feed.entries
# article_title = feed_entries[0].title
# article_link = feed_entries[0].link


engine = pyttsx3.init()  # object creation
engine.setProperty('voice', 'english-us')
engine.setProperty('rate', 130)
engine.setProperty('volume', 0.1)


with open('myhora-buddha-2564.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

day = datetime.today().strftime('%Y%m%d')
holyday = []

for i in range(len(data)):
    if i > 0:
        if(int(data[i][1]) > int(day)):
            holyday.append(data[i][1])
        # print(holyday)


def speak(text):
        print(text)
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
                                if button_press == 0:
                                        proc = subprocess.Popen(["python3", "sati.py"])
                                board.button.wait_for_press()
                                # board.led.state = Led.ON
                                button_press += 1
                                board.button.wait_for_release()
                                # board.led.state = Led.OFF
                                ts2 = time.time()                                       
                                if button_press == 1: 
                                        proc.kill()
                                        if have_internet():
                                                text = ""
                                        else:
                                                text = "../thaivoices/nointernet.mp3 "
                                        leds.update(Leds.rgb_on(Color.WHITE))
                                        import datetime
                                        today = datetime.datetime.now() 
                                        text += "../thaivoices/words/today.mp3 ../thaivoices/words/day.mp3 ../thaivoices/weekday/"+today.strftime('%w')+".mp3"
                                        text += " ../thaivoices/words/at.mp3 ../thaivoices/59/"+today.strftime('%d')+".mp3"+" ../thaivoices/month/0.mp3 ../thaivoices/month/"+today.strftime('%m')+".mp3"
                                        text += " ../thaivoices/words/time.mp3 ../thaivoices/59/"+today.strftime('%H')+".mp3"+" ../thaivoices/words/hour.mp3"
                                        text += " ../thaivoices/59/"+today.strftime('%M')+".mp3"+" ../thaivoices/words/minute.mp3"
                                        os.system("mpg123 -q -f 2000 "+text)

                                        y = list(str(holyday))
                                        yy = y[2]+y[3]+y[4]+y[5]
                                        mm = y[6]+y[7]
                                        dd = y[8]+y[9]
                                        x = datetime.datetime(int(yy), int(mm), int(dd))
                                        # z = x.strftime("%B %A %d")
                                        text = ""
                                        text += " ../thaivoices/words/buddhaday.mp3 ../thaivoices/words/face.mp3 ../thaivoices/words/is.mp3 ../thaivoices/words/day.mp3"
                                        text += " ../thaivoices/weekday/"+x.strftime('%w')+".mp3 ../thaivoices/words/at.mp3 ../thaivoices/59/"+x.strftime('%d')+".mp3"
                                        text += " ../thaivoices/month/0.mp3 ../thaivoices/month/"+x.strftime('%m')+".mp3"  
                                        os.system("mpg123 -q -f 2000 "+text) 
                                        proc = subprocess.Popen(["python3", "sati.py"])    
                                elif button_press == 2:
                                        proc.kill()
                                        if have_internet():
                                                text = "Listen to Tibetan Buddhist internet radio"
                                                speak(text)
                                                leds.update(Leds.rgb_on(Color.WHITE))
                                                proc = subprocess.Popen(["mpg123","-f","2000","-q","http://199.180.72.2:9097/lamrim"])
                                                # proc = subprocess.Popen(["mpg123","-f","2000","-q",article_link])
                                        else:
                                                leds.update(Leds.rgb_on(Color.YELLOW))
                                                text = " ../thaivoices/words/buddhadham.mp3"
                                                os.system("mpg123 -q -f 2000 "+text) 
                                                proc = subprocess.Popen(["mpg123","-f","2000","-q","-Z","-l","0","--list","THbuddhadham.txt"]) 
                                elif button_press == 3:
                                        proc.kill()
                                        leds.update(Leds.rgb_on(Color.YELLOW))
                                        text = " ../thaivoices/words/chanting.mp3"
                                        os.system("mpg123 -q -f 2000 "+text) 
                                        proc = subprocess.Popen(["mpg123","-f","2000","-q","-Z","-l","0","--list","THchanting.txt"]) 
                                elif button_press == 4:
                                        proc.kill()
                                        leds.update(Leds.rgb_on(Color.YELLOW))
                                        text = " ../thaivoices/words/sutra.mp3"
                                        os.system("mpg123 -q -f 2000 "+text) 
                                        proc = subprocess.Popen(["mpg123","-f","2000","-q","-Z","-l","0","--list","sutra.txt"]) 
                                elif button_press == 5:
                                        proc.kill()
                                        leds.update(Leds.rgb_on(Color.PURPLE))
                                        text = " ../thaivoices/words/dhamma.mp3"
                                        os.system("mpg123 -q -f 2000 "+text) 
                                        proc = subprocess.Popen(["mpg123","-f","2000","-q","-Z","-l","0","--list","THdhamma.txt"])
                                elif button_press == 6:
                                        proc.kill()
                                        leds.update(Leds.rgb_on(Color.GREEN))
                                        text = "../thaivoices/words/dhamma.mp3 ../thaivoices/words/buddhadasa.mp3"
                                        os.system("mpg123 -q -f 2000 "+text) 
                                        proc = subprocess.Popen(["mpg123","-f","2000","-q","-Z","-l","0","--list","THbuddhadasa.txt"])
                                elif button_press == 7:
                                        proc.kill()
                                        leds.update(Leds.rgb_on(Color.GREEN))
                                        text = "../thaivoices/words/dhamma.mp3 ../thaivoices/words/payutto.mp3"
                                        os.system("mpg123 -q -f 2000 "+text) 
                                        proc = subprocess.Popen(["mpg123","-f","2000","-q","-Z","-l","0","--list","THpayutto.txt"])
                                elif button_press == 8:
                                        proc.kill()
                                        text = "../thaivoices/meditation.mp3"
                                        os.system("mpg123 -q -f 2000 "+text)
                                        leds.update(Leds.rgb_on(Color.BLUE))
                                        # board.led.state = Led.ON
                                        proc = subprocess.Popen(["mpg123","-f","2000","-q","-l","0","../dataen/bell15min.mp3"])
                                else:
                                        if button_press >= 9 :
                                                proc.kill()
                                                text = " ../thaivoices/sati.mp3"
                                                os.system("mpg123 -q -f 2000 " + text) 
                                                os.system("sudo pkill -f mpg123")
                                                board.led.state = Led.OFF
                                                button_press = 0
                                                ts1 = time.time()
if __name__ == '__main__':
        main()

# mpg123 -f 2000 the maximum value of the amplitude is 100% which coressponds to 32768, i use this when i want to run with crontab