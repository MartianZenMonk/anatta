import os
import sys

os.system("amixer -D pulse sset Master 50%")
os.system("amixer -c 0 sset Headphone 50%")


# How to
# $ crontab -e
# select nano editor (if not)
# type
# @reboot python3 setVolume.py
#$ crontab -l Check if crontab is properly configured
