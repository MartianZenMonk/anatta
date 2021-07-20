import os
import sys
import time
import pyttsx3

from aiy.board import Board, Led

engine = pyttsx3.init()  # object creation
engine.setProperty('voice', 'english-us')
engine.setProperty('rate', 130)
engine.setProperty('volume', 0.1)

def speak(text):
        print(text)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        return None


# voices = ["en-gb","en-us","en-gb-scotland","en-gb-x-gbclan","en-gb-x-gbcwmd","en-029"]

# def speakng(t,v='',*args):
#         if v == '':
#                 v = "en-us"
#         text = 'speak-ng -a 10 -s 130 -v ' + v + ' "' + t + '"'
#         print(text)
#         os.system(text)
#         return None


def main():
	with Board() as board:
		while True:
			board.led.state = Led.OFF
			text = "Hello Press button within 3 seconds For English Language"
			speak(text)
			t1 = time.time()
			board.led.state = Led.ON
			board.button.wait_for_press()
			t2 = time.time()
			try:
				if t2-t1 < 4:
					board.led.state = Led.OFF
					os.system("python3 anatta_button.py")
			except:
				print("wait too long")
			board.led.state = Led.OFF
			text = "Hello Press button within 3 seconds For Thai Language"
			speak(text)
			t1 = time.time()
			board.led.state = Led.ON
			board.button.wait_for_press()
			t2 = time.time()
			try:
				if t2-t1 < 4:
					board.led.state = Led.OFF
					os.system("python3 anatta_Thai_button.py")
			except:
				print("wait too long again")
			board.led.state = Led.OFF
			text = "Hello Press button within 3 seconds For Shutdown"
			speak(text)
			t1 = time.time()
			board.led.state = Led.ON
			board.button.wait_for_press()
			t2 = time.time()
			try:
				if t2-t1 < 4:
					board.led.state = Led.OFF
					os.system("sudo shutdown now")
			except:
				print("wait too long again")


if __name__ == '__main__':
        main()