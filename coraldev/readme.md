
THANK YOU VERY MUCH TO MR. Peter Malkin FOR GIVING ME THE VOICEKIT AND CORAL DEV BOARD


https://coral.ai/docs/dev-board/get-started/


use

git clone https://github.com/MartianZenMonk/anatta.git

- then you can use git pull to update the content after reboot if you like :)


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


http://voice2json.org/install.html



if you want to share your idea please join FB Group : https://m.facebook.com/groups/890791731653111/



