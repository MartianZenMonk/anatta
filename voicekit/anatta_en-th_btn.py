import os
import sys
import time
import pyttsx3

from aiy.board import Board, Led

engine = pyttsx3.init()  # object creation
engine.setProperty('voice', 'english-us')
engine.setProperty('rate', 130)
engine.setProperty('volume', 0.2)

def speak(text):
        print(text)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        return None


def main():
	with Board() as board:
		while True:
			text = "Hello Press button within 3 sec For English"
			speak(text)
			t1 = time.time()
			board.led.state = Led.ON
			board.button.wait_for_press()
			t2 = time.time()
			if t2-t1 < 4:
				os.system("python3 anatta_button.py")
			else:
				pass
			text = "Hello Press button within 3 sec For Thai"
			speak(text)
			t1 = time.time()
			board.led.state = Led.ON
			board.button.wait_for_press()
			t2 = time.time()
			if t2-t1 < 4:
				os.system("python3 anatta_Thai_button.py")


if __name__ == '__main__':
        main()