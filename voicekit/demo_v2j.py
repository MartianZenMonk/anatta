import os
import subprocess
import random
import json
import re
from datetime import datetime

import requests
from pprint import pprint
from urllib.request import urlopen
from json import load


def ipInfo(addr=''):
    
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    #response from url(if res==None then check connection)
    data = load(res)

    #will load the json response into data
    # for attr in data.keys():
    #     #will print the data line by line
    #     print(attr,' '*13+'\t->\t',data[attr])

    loc = data['loc'].split(',')
    query='lat='+loc[0]+'&lon='+loc[1]
    res=requests.get('https://fcc-weather-api.glitch.me/api/current?'+query)

    return res.json();

listen_command = "/usr/bin/voice2json transcribe-stream | /usr/bin/voice2json recognize-intent"
speak_command = "/usr/bin/voice2json speak-sentence '{}'"
pattern = re.compile(r'(?<!^)(?=[A-Z])')


def get_time():
	now = datetime.now()
	speak("The time is {}".format(now.strftime("%-I:%M %p")))


def get_temperature():
	w = ipInfo()
	text = 'Country '+w['sys']['country']+'. City '+w['name']+'. Temperature is '+str(w['main']['temp'])+'. Humidity is '+str(w['main']['humidity'])+'. The weather '+w['weather'][0]['description']
	speak(text)


def speak(sentence):
	for output_line in shell_command(speak_command.format(sentence)):
		print(output_line, end='')


def shell_command(cmd):
	popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
	for stdout_line in iter(popen.stdout.readline, ""):
		yield stdout_line
	popen.stdout.close()
	return_code = popen.wait()
	if return_code:
		raise subprocess.CalledProcessError(return_code, cmd)


def process_output(line):
	data = json.loads(line)
	if not data['timeout'] and data['intent']['name']:
		func_name = pattern.sub('_', data['intent']['name']).lower()
		if func_name in globals():
			globals()[func_name](**data['slots'])


for output_line in shell_command(listen_command):
	process_output(output_line)