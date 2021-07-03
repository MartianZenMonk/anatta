THANK YOU VERY MUCH TO MR. Peter Malkin FOR GIVING ME THE VOICEKIT AND CORAL DEV BOARD


https://aiyprojects.withgoogle.com/voice/



You may have to install the following packages


- sudo pip3 install pyttsx3
- sudo apt  install espeak  (and espeak-ng if you like )
- sudo apt  install mpg123


You may use crontab -e for

- @reboot python3 shutdown_button.py
- @reboot sleep 60 && python3 sayhi.py
- or play with button @reboot sleep 90 && cd anatta/voicekit && python3 anatta_button.py


