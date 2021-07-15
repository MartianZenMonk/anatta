import os
import sys
from gtts import gTTS 

# file = open("moggallana.txt", "r").read().replace("\n", " ")
# speech = gTTS(text = str(file),lang='en',slow = False)
# speech.save("moggallana.mp3")

# for i in range(59,60):
# 	speech = gTTS(text = str(i),lang='th',slow = False)
# 	speech.save(str(i)+".mp3")

weekday = ["อาทิตย์","จันทร์","อังคาร","พุทธ","พฤหัสบดี","ศุกร์","เสาร์"]

month = ["เดือน","มกราคม","กุมภาพันธ์","มีนาคม","เมษายน","พฤกษภาคม","มิถุนายน","กรกฎาคม","สิงหาคม","กันยายน","ตุลาคม","พฤศจิกายน","ธันวาคม"]

others = ["วันนี้","วัน","ที่","เวลา","นาฬิกา","นาที","วันพระ","ถัดไป","คือ","สวดมนต์","ฟังธรรม","ท่านพุทธทาส","ท่าน ป. อ. ปยุตโต","พุทธธรรม","พระสูตร"]

# for i in range(0,15):
# 	speech = gTTS(text = str(others[i]),lang='th',slow = False)
# 	speech.save(str(i)+".mp3")

# text = "ชั่วโมงปฏิบัติธรรม เสียงระฆังจะดังทุกๆสิบห้านาที ผู้ปฏิบัติอาจจะเริ่ม ด้วยการเดินจงกรมก่อน แล้วค่อยนั่ง เพื่อการ ผ่อนคลาย การเดินจงกรมอาจจะเดิน สามจังหวะ ยก ย่าง เหยียบ หรือ ขวา ย่าง หนอ ซ้าย ย่างหนอ "
# text += "หรือหนึ่งจังหวะ รู้เหยียบ หรือ ขวา พุท ซ้าย โธ"

# text = "สัพเพ ธัมมา นาลัง อภินิเวสายะ สิ่งทั้งหลายทั้งปวง ไม่ควรยึดมั่นถือมั่น ธรรมะสวัสดีค่ะ"

#text = "ไม่มีการเชื่อมต่ออินเตอร์เนต วันเวลาอาจจะไม่ถูกต้องค่ะ"

# text = "รู้ ลม หาย ใจ รู้ กาย เคลื่อน ไหว รู้ ใจ นึก คิด"

# text = "มี ความ เพียร เครื่อง เผา กิเลส มี ความ รู้ สึก ตัว มี สติ ถอน ความ พอ ใจ และ ความ ไม่ พอ ใจ ใน ใจ ออก เสีย ได้"

# text = ["ยิน","ดี","ต้อน","รับ","สู่","โครง","การ","อนัตตา","ขอ","ให้","ท่าน","มี","ความ","สุข","กับ","การ","ปฏิบัติ","ธรรม","ค่ะ"]

# for i in range(len(text)):
# 	speech = gTTS(text = text[i],lang='th',slow = False)
# 	speech.save(str(text[i]) + ".mp3")
# ftext = ""
# for i in range(len(text)):
# 	ftext += " thwords/" + text[i] + ".mp3"

# os.system('mpg123 -h 1 -d 2  ' + ftext)


# import requests
# from pprint import pprint
# from urllib.request import urlopen
# from json import load


# def ipInfo(addr=''):
    
#     if addr == '':
#         url = 'https://ipinfo.io/json'
#     else:
#         url = 'https://ipinfo.io/' + addr + '/json'
#     res = urlopen(url)
#     #response from url(if res==None then check connection)
#     data = load(res)

#     #will load the json response into data
#     # for attr in data.keys():
#     #     #will print the data line by line
#     #     print(attr,' '*13+'\t->\t',data[attr])

#     loc = data['loc'].split(',')
#     query='lat='+loc[0]+'&lon='+loc[1]
#     res=requests.get('https://fcc-weather-api.glitch.me/api/current?'+query)

#     return res.json();


# w = ipInfo()

# text = 'Country '+w['sys']['country']+' city '+w['name']+' Temperature is '+str(w['main']['temp'])+' Humidity is '+str(w['main']['humidity'])+' weather '+w['weather'][0]['description']
# text += ' Sunrise '+str(w['sys']['sunrise'])+' Sunset '+str(w['sys']['sunset'])
# print(text)
import csv
from datetime import datetime

with open('myhora-buddha-2564.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

day = datetime.today().strftime('%Y%m%d')
holyday = []
thholyday = []

for i in range(len(data)):
    if i > 0:
        if(int(data[i][1]) > int(day)):
            holyday.append(data[i][1])
            thholyday.append(data[i][0])
t = thholyday[0].replace("(", " ")
x = t.split()

# text = ["วันพระ","ขึ้น","แรม","8","15","1","14","ค่ำ","เดือนอ้าย","เดือนยี่","เดือนสาม","เดือนสี่","เดือนห้า","เดือนหก","เดือนเจ็ด","เดือนแปด","เดือนแปดหลัง","เดือนเก้า","เดือนสิบ","เดือนสิบเอ็ด","เดือนสิบสอง"]

ftext = ""
for i in range(len(x)-1):
  ftext += " thwords/" + x[i] + ".mp3"

print(ftext)
# os.system('mpg123 ' + ftext)