import os
import sys
import time

from aiy.board import Board, Led

with Board() as board:
	board.led.state = Led.ON
	# board.button.wait_for_press()
	os.system("amixer -D pulse sset Master 50%")
	time.sleep(5)
	board.led.state = Led.OFF
	# board.button.wait_for_release()
	os.system("amixer -c 0 sset Headphone 50%")
	time.sleep(5)
	os.system('mpg123 -q -f 2000 ../thaivoices/hello.mp3')
	
# How to
# $ crontab -e
# select nano editor (if not)
# type
# @reboot sleep 60 && python3 sayhi.py
#$ crontab -l Check if crontab is properly configured
