import os
import sys
import csv
from gtts import gTTS 

# file = open("moggallana.txt", "r").read().replace("\n", " ")
# speech = gTTS(text = str(file),lang='en',slow = False)
# speech.save("moggallana.mp3")

# for i in range(59,60):
# 	speech = gTTS(text = str(i),lang='th',slow = False)
# 	speech.save(str(i)+".mp3")

# weekday = ["อาทิตย์","จันทร์","อังคาร","พุทธ","พฤหัสบดี","ศุกร์","เสาร์"]

# month = ["เดือน","มกราคม","กุมภาพันธ์","มีนาคม","เมษายน","พฤกษภาคม","มิถุนายน","กรกฎาคม","สิงหาคม","กันยายน","ตุลาคม","พฤศจิกายน","ธันวาคม"]

# others = ["วันนี้","วัน","ที่","เวลา","นาฬิกา","นาที","วันพระ","ถัดไป","คือ","สวดมนต์","ฟังธรรม","ท่านพุทธทาส","ท่าน ป. อ. ปยุตโต","พุทธธรรม","พระสูตร"]

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


# text  = ["ทำ","ตัว","ผ่อน","คลาย","หาย","ใจ","ยาว","ยาว","คลาย","ความ","กังวล","ตั้ง","จิต","มั่น","รู้","ลม","หาย","ใจ",]
# text += ["เข้า","ออก","สั้น","ยาว","หยาบ","ละเอียด","เกิด","ดับ","ไม่","เที่ยง","หนอ","แล"]
# text += ["ไม่","มี","ทุกข์","ไม่","มี","สุข","มี","แต่","ความ","ที่","สติ","เป็น","ธรรมชาติ","บริสุทธิ์","เพราะ","อุเบกขา","แล้ว","แล","อยู่"]

# ftext = ""
# for i in range(len(text)):
# 	ftext += " thwords/" + text[i] + ".mp3"

# os.system('mpg123 ' + ftext)


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
# import csv
# from datetime import datetime

# with open('myhora-buddha-2564.csv', newline='') as f:
#     reader = csv.reader(f)
#     data = list(reader)

# day = datetime.today().strftime('%Y%m%d')
# holyday = []
# thholyday = []

# for i in range(len(data)):
#     if i > 0:
#         if(int(data[i][1]) > int(day)):
#             holyday.append(data[i][1])
#             thholyday.append(data[i][0])
# t = thholyday[0].replace("(", " ")
# x = t.split()

# text = ["วันพระ","ขึ้น","แรม","8","15","1","14","ค่ำ","เดือนอ้าย","เดือนยี่","เดือนสาม","เดือนสี่","เดือนห้า","เดือนหก","เดือนเจ็ด","เดือนแปด","เดือนแปดหลัง","เดือนเก้า","เดือนสิบ","เดือนสิบเอ็ด","เดือนสิบสอง"]


# ftext = ""
# for i in range(len(x)-1):
#   ftext += " thwords/" + x[i] + ".mp3"

# text = ["วันวิสาขบูชา","วันอัฏฐมีบูชา","วันอาสาฬหบูชา","วันมาฆบูชา","วันเข้าพรรษา","วันออกพรรษา"]
# text = ["วันนี้","วัน","ที่","เดือน","เวลา","นาฬิกา","นาที"]
# text = ["หน้า","คือ"]
# for i in range(len(text)):
#   speech = gTTS(text = text[i],lang='th',slow = False)
#   speech.save(str("thwords/"+text[i]) + ".mp3")

# import datetime
# today = datetime.datetime.now() 
# # text = ["วันนี้","วัน","weekday/%w","ที่","59/%d","เดือน","month/%m","เวลา","59/%H","นาฬิกา","59/%M","นาที"]
# t = "วันนี้,วัน,weekday/%w,ที่,59/%d,เดือน,month/%m,เวลา,59/%H,นาฬิกา,59/%M,นาที"
# t = t.replace("%w",today.strftime('%w'))
# t = t.replace("%d",today.strftime('%d'))
# t = t.replace("%m",today.strftime('%m'))
# t = t.replace("%H",today.strftime('%H'))
# t = t.replace("%M",today.strftime('%M'))
# text = t.split(',')
# print(text)
# ftext = ""
# for i in range(len(text)):
#     ftext += " thwords/" + text[i] + ".mp3"
# os.system('mpg123 ' + ftext)

# t1 = ["ยิน","ดี","ต้อน","รับ","สู่","โครง","การ","อนัตตา","ขอ","ให้","ท่าน","มี","ความ","สุข","กับ","การ","ปฏิบัติ","ธรรม","ค่ะ"]
# t2 = ["วันวิสาขบูชา","วันอัฏฐมีบูชา","วันอาสาฬหบูชา","วันมาฆบูชา","วันเข้าพรรษา","วันออกพรรษา"]
# t3 = ["วันนี้","วัน","ที่","เดือน","เวลา","นาฬิกา","นาที","หน้า","คือ"]
# t4 = ["วันพระ","ขึ้น","แรม","ค่ำ","เดือนอ้าย","เดือนยี่","เดือนสาม","เดือนสี่","เดือนห้า","เดือนหก","เดือนเจ็ด","เดือนแปด","เดือนแปดหลัง","เดือนเก้า","เดือนสิบ","เดือนสิบเอ็ด","เดือนสิบสอง"]

# text = t1 + t2 + t3 + t4
# with open('thwords.csv', 'w') as f:
      
#     # using csv.writer method from CSV package
#     write = csv.writer(f)
      
#     write.writerow(text)

# จงกรม 6 ระยะ ยกส้นหนอ-ยกหนอ-ย่างหนอ-ลงหนอ-ถูกหนอ-กดหนอ

# กำหนดว่า หายใจหนอ เข้าออกหนอ นี่ขั้นหนึ่ง สั้นยาวหนอ ขั้นหนึ่ง หยาบละเอียดหนอ ขั้นหนึ่ง เป็นนามเป็นรูปหนอ ขั้นหนึ่ง เป็นการเกิดการดับหนอ ขั้นหนึ่ง เป็นอนิจจังหนอ ขั้นหนึ่ง เป็นอนัตตา ขั้นหนึ่ง อ้าว! จางแล้วโว้ยๆ นี่ขั้นหนึ่ง ดับแล้วโว้ย ขั้นหนึ่ง โยนหมดแล้วโว้ย อีกขั้นหนึ่ง ขั้นนี้ไม่ต้องก็ได้ เพราะว่าถ้าดับแล้ว มันก็วางของมันเอง กี่ขั้นล่ะ 1 2 3 4 5 6 7 8 9 10 11 ขั้นน่ะ รวบรัดเสียบ้าง เหลือ 5-6 ขั้นก็ได้ 

# there are six stages of walking exercise
# การเดินจงกรม  มี  ๖ ระยะ

# 1. Stages: Right goes thus, Left goes thus
# ๑.  ระยะที่  ๑:   ขวา  ย่าง  หนอ ,  ซ้าย   ย่าง  หนอ

# 2. Stages: Lifting, Treading
# ๒.  ระยะที่  ๒  : ยกหนอ ,  เหยียบหนอ

# 3. Stages: Lifting, Moving, Treading
# ๓.  ระยะที่ ๓:  ยกหนอ, ย่างหนอ, เหยียบหนอ

# 4. Stages: Heel up, Lifting, Moving, and Treading
# ๔.  ระยะที่ ๔:  ยกส้นหนอ,  ยกหนอ, ย่างหนอ, เหยียบหนอ

# 5. Stages: Heel up, Lifting, Moving, Lowering, Touching
# ๕.  ระยะที่ ๕:  ยกส้นหนอ, ยกหนอ, ย่างหนอ, ลงหนอ,  ถูกหนอ

# 6. Stages: Heel up, Lifting, Moving, Lowering, Touching, and Pressing


# text = ["ยกส้นหนอ","ยกหนอ","ย่างหนอ","ลงหนอ","ถูกหนอ","กดหนอ"]
# text = ["heel up","lifting","moving","lowering","touching","pressing"]
# t = "ไม่ มี ทุกข์ ไม่ มี สุข มี แต่ ความ ที่ สติ เป็น ธรรมชาติ บริสุทธิ์ เพราะ อุเบกขา แล้ว แล อยู่"
# t = "ไม่ มี ทุกข์ สุข แต่ ความ ที่ สติ เป็น ธรรมชาติ บริสุทธิ์ เพราะ อุเบกขา แล้ว แล อยู่"
# text = t.split(" ")
# text = ["ไม่มีทุกข์ ไม่มีสุข มีแต่ความที่สติเป็นธรรมชาติบริสุทธิ์เพราะอุเบกขา แล้วแลอยู่"]

# text = ["คิดเป็นระเบียบ คิดถูกวิธี คิดเป็นเหตุเป็นผล คิดให้เกิดการกระทำที่เป็นกุศล"]

# text = ["หาย","ใจ","เข้า","ออก","รู้","สั้น","ยาว","หยาบ","ละเอียด","หนัก","เบา","เกิด","ดับ","ไม่","เที่ยง","หนอ"]

# text = ["ทำ","ตัว","ผ่อน","คลาย","ความ","กังวล","ตั้ง","จิต","มั่น","ที่","ลม"]


# text = ["ทุกข์","แต่","สติ","เป็น","ธรรมชาติ","บริสุทธิ์","เพราะ","อุเบกขา","แล้ว","แล","อยู่"]

# for i in range(len(text)):

#   print(text[i])

#   speech = gTTS(text = text[i],lang='th',slow = False)
#   speech.save(str("thwords/"+text[i]) + ".mp3")


  # speech = gTTS(text = text[i],lang='en',slow = False)
  # speech.save(str("../dataen/"+text[i]) + ".mp3")

# t = "อนิจจาวะตะสังขารา, สังขารทั้งหลายไม่เที่ยงหนอ, อุปปาทะวะยะธัมมิ โน , มีอันเกิดขึ้นและเสื่อมไปเป็นธรรมดา, อุปปัชชิตะวานิรุชฌันติ, บังเกิดขึ้นแล้วย่อมดับไป, เตสังวูปะสะโมสุโข, การเข้าไประงับสังขารเหล่านั้นเสียได้เป็นความสุข"

# t = 'ฝึกเพื่อให้มีความรู้สึกตัวไว ทันต่อการรับรู้ทาง ตา หู จมูก ลิ้น กาย ใจ'
# speech = gTTS(text = t,lang='th',slow = False)
# speech.save(str("goal.mp3"))

def runtime_vocabulary():
    with open('vocabulary.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    print(data)
    new_vocab = " ".join(str(x[0]) for x in data) 
    
    return new_vocab


def save_vocabulary(w):
    wlist = []
    wlist.append(w)
    writer = csv.writer(open("vocabulary.csv", "a"))
    writer.writerow(wlist)


save_vocabulary("orange")

v = runtime_vocabulary()
print(v)