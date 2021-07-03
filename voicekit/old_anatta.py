import os
import sys
import time
import pyttsx3

from aiy.board import Board, Led

engine = pyttsx3.init() # object creation
engine.setProperty('voice','english-us') 
engine.setProperty('rate', 150)
engine.setProperty('volume',0.5)

def main():
        print('Welcome to Anatta Project, press button to play with dhamma')
        button_press = 0
        ts1 = time.time()
        with Board() as board:
                while True:
                        board.button.wait_for_press()
                        board.led.state = Led.ON
                        button_press += 1
                        board.button.wait_for_release()
                        board.led.state = Led.OFF
                        ts2 = time.time()
                        if button_press == 2 and ts2-ts1 < 20:
                                button_press = 0
                                ts1 = time.time()
                                engine.say("English chanting")
                                engine.runAndWait()
                                engine.stop()
                                os.system("mpg123 --list chanting.txt") # loop forever just add -l 0
                        elif button_press == 3 and ts2-ts1 < 40:
                                button_press = 0
                                ts1 = time.time()
                                engine.say("Play Dhamma")
                                engine.runAndWait()
                                engine.stop()
                                os.system("mpg123 --list dhamma.txt") # loop forever just add -l 0
                        else:
                                print(str(button_press))
                                print(str(ts2-ts1))
                                button_press = 0
                                ts1 = time.time()
if __name__ == '__main__':
        main()