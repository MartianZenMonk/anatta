
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




VOSK For Coral Dev Board

- pip3 install https://github.com/alphacep/vosk-api/releases/download/0.3.15/vosk-0.3.15-cp37-cp37m-linux_aarch64.whl
- https://alphacephei.com/vosk/install


# voice2json For Coral Dev Board / Pi 4

Install Voice2JSON
- sudo apt-get install libasound2 libasound2-data libasound2-plugins
- verify armhf architecture by typing , dpkg-architecture | grep DEB_BUILD_ARCH=
- wget https://github.com/synesthesiam/voice2json/releases/download/v2.0/voice2json_2.0_armhf.deb
- sudo apt install ./voice2json_2.0_armhf.deb
- sudo apt-get install espeak-ng
- mkdir -p ~/.config/voice2json (for profile)
- curl -SL https://github.com/synesthesiam/en-us_pocketsphinx-cmu/archive/v1.0.tar.gz | tar -C ~/.config/voice2json --skip-old-files --strip-components=1 -xzvf -
- To configure custom commands, you will need to edit the sentences.ini file located inside the ~/.config/voice2json folder.
- test profile, voice2json --profile ~/.config/voice2json transcribe-stream
- good luck!


https://learn.adafruit.com/edge-speech-recognition-with-voice2json

for Pi zero but very slow

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


if you want to share your idea please join FB Group : https://m.facebook.com/groups/890791731653111/



