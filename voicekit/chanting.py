import os
import sys
import pyttsx3

from aiy.board import Board, Led

def main():
        button_press = 0
        with Board() as board:
                while True:
                        board.button.wait_for_press()
                        print('ON')
                        board.led.state = Led.ON
                        button_press += 1
                        board.button.wait_for_release()
                        print('OFF')
                        board.led.state = Led.OFF
                        if button_press >= 2 :
                                engine = pyttsx3.init() # object creation
                                engine.setProperty('voice','english-us') 
                                engine.setProperty('rate', 150)
                                engine.setProperty('volume',0.5)
                                engine.say("English Chanting")
                                engine.runAndWait()
                                engine.stop()
                                button_press = 0
                                os.system("mpg123 --list chanting.txt") # loop forever just add -l 0
if __name__ == '__main__':
        main()