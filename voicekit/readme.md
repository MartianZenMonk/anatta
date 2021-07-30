
THANK YOU VERY MUCH TO MR. Peter Malkin FOR GIVING ME THE VOICEKIT AND CORAL DEV BOARD


https://aiyprojects.withgoogle.com/voice/


use

git clone https://github.com/MartianZenMonk/anatta.git

- then you can use git pull to update the content after reboot if you like :)


You may have to install the following packages
- sudo pip3 install pyttsx3
- sudo apt  install espeak  (and espeak-ng if you like )
- sudo apt  install mpg123


if you use aiyprojects-2021-04-02.img.xz then you can do this
- sudo pip3 install vosk
- apt-get install libgfortran3


You may use crontab -e for
- @reboot cd anatta/voicekit && sleep 60 && python3 update.py
- @reboot cd anatta/voicekit && sleep 60 && python3 sayhi.py

- play with button
- @reboot cd anatta/voicekit && sleep 90 && python3 anatta_en-th_btn.py 


- play with voices
- @reboot cd anatta/voicekit && sleep 90 && python3 testq.py 


or


https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/

- for this one you can use
- sudo systemctl status myscript.service
- sudo systemctl start myscript.service
- sudo systemctl restart myscript.service
- sudo systemctl stop myscript.service




You may use others text to speech engine 



https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/customizations/tts-engine




voice2json for Pi zero but very slow

$ git clone https://github.com/synesthesiam/voice2json
$ cd voice2json
$ ./configure
$ make
$ make install


get profile
- mkdir -p ~/.config/voice2json 
- curl -SL https://github.com/synesthesiam/en-us_pocketsphinx-cmu/archive/v1.0.tar.gz | tar -C ~/.config/voice2json --skip-old-files --strip-components=1 -xzvf -
-

testing
- ./voice2json/voice2json.sh --profile ~/.config/voice2json transcribe-stream 
- 
- https://learn.adafruit.com/edge-speech-recognition-with-voice2json



if you want to share your idea please join FB Group : https://m.facebook.com/groups/890791731653111/



