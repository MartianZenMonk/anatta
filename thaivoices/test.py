import os
import sys
import subprocess
import time
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

# text = ["หาย","ใจ","เข้า","พุท","หาย","ใจ","ออก","โธ"]
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

# text = ["หนึ่ง","เหยียบ"]

# for i in range(len(text)):

#   print(text[i])

#   speech = gTTS(text = text[i],lang='th',slow = False)
#   speech.save(str("thwords/"+text[i]) + ".mp3")


  # speech = gTTS(text = text[i],lang='en',slow = False)
  # speech.save(str("../dataen/"+text[i]) + ".mp3")

# t = "อนิจจาวะตะสังขารา, สังขารทั้งหลายไม่เที่ยงหนอ, อุปปาทะวะยะธัมมิ โน , มีอันเกิดขึ้นและเสื่อมไปเป็นธรรมดา, อุปปัชชิตะวานิรุชฌันติ, บังเกิดขึ้นแล้วย่อมดับไป, เตสังวูปะสะโมสุโข, การเข้าไประงับสังขารเหล่านั้นเสียได้เป็นความสุข"

# t = 'ฝึกเพื่อให้มีความรู้สึกตัวไว ทันต่อการรับรู้ทาง ตา หู จมูก ลิ้น กาย ใจ'
# t = "หายใจเข้า พุท หายใจออก โธ"

# t1 = '''
# ดูกะระภิกษุทั้งหลาย ก็ความดับแห่งทุกข์เป็นไฉน เพราะอาศัย
# จักษุและรูป จึงเกิดจักขุวิญญาณ ความประชุมแห่งธรรม ๓ ประการเป็นผัสสะ
# เพราะผัสสะเป็นปัจจัย จึงเกิดเวทนา เพราะเวทนาเป็นปัจจัย จึงเกิดตัณหา
# เพราะตัณหานั้นเทียวดับด้วยสำรอกโดยไม่เหลือ อุปาทานจึงดับ เพราะอุปาทานดับ
# ภพจึงดับ เพราะภพดับ ชาติจึงดับ เพราะชาติดับ ชราและมรณะ โสกะปริเทวะทุกขะโทมะนัส
# และอุปายาสจึงดับ ความดับแห่งกองทุกข์ทั้งมวลนี้ ย่อมมีด้วยประการอย่างนี้ ภิกษุทั้งหลาย นี้แลเป็นความดับแห่งทุกข์
# '''

# t = '''
# กะตะโม จะ ภิกฺขะเว ทุก ขัส สะ อัต ถัง คะ โม 
# จัก ขุญ จะ ปฏิจ จะ รู เป จะ อุป ปะ ชัช ติ 
# จัก ขุ วิญญาณัง ติณณัง สังคะติ ผัสโส
# ผัสสะ ปัจ จะ ยา เว ทะ นา เว ทะ นา ปัจ จะ ยา ตัณหา ตัส สา เย วะ ตัณหายะ
# อะเสสะวิราคะนิโรธา อุปาทานะนิโรโธ อุปาทานะนิโรธา ภะวะนิโรโธ
# ภะวะนิโรธา ชา ติ นิโรโธ ชา ติ นิโรธา ชรามะระณัง โส กะ ปริเทวะ ทุก ขะ
# โทมะนัสสุปายาสา นิรุชฌันติ เอวะเมตัสสะ เกวะลัสสะ ทุก ขักฺ ขัน ธัสฺ สะ
# นิโรโธ โหติ อะยัง โข ภิกฺขะเว ทุก ขัส สะ อัตถังคโม
# '''

# t = '''
# อะตีตัง นาน๎วาคะเมยยะ นัปปะฏิกังเข อะนาคะตัง
# -บุคคลไม่ควรตามคิดถึงสิ่งที่ล่วงไปแล้วด้วยอาลัย ,
# และไม่พึงพะวงถึงสิ่งที่ยังไม่มาถึง

# ยะทะตีตัมปะหีนันตัง อัปปัตตัญจะ อะนาคะตัง
# -สิ่งเป็นอดีตก็ละไปแล้ว , สิ่งเป็นอนาคตก็ยังไม่มา

# ปัจจุปปันนัญจะ โย ธัมมัง ตัตถะ ตัตถะ วิปัสสะติ ,
# อะสังหิรัง อะสังกุปปัง ตัง วิทธา มะนุพ๎รูหะเย
# -ผู้ใดเห็นธรรมอันเกิดขึ้นเฉพาะหน้าที่นั้นๆ อย่างแจ่มแจ้ง ,
# ไม่ง่อนแง่นคลอนแคลน , เขาควรพอกพูนอาการเช่นนั้นไว้

# อัชเชวะ กิจจะมาตัปปัง โก ชัญญา มะระณัง สุเว
# -ความเพียรเป็นกิจที่ต้องทำวันนี้ , ใครจะรู้ความตายแม้พรุ่งนี้
# '''

# t = 'เพียรฝึกให้ สุขง่าย ทุกข์ยาก มีความอยากเป็นฉันทะ'

# t = 'ยังทำตามความเคยชินอยู่ไหมหนอ'

# t = 'อัปเปวะนา มิมัสสะ เกวะลัสสะ ทุกขักขันธัสสะ อันตะกิริยา ปัญญาเยถาติ ทำไฉนการทำที่สุดแห่งกองทุกข์ทั้งสิ้นนี้ จะพึงปรากฏชัดแก่เราได้'

# t = 'ความทุกข์ เกิดที่จิต เพราะเห็นผิด เมื่อผัสสะ. ความทุกข์ จะไม่โผล่ ถ้าไม่โง่ เมื่อผัสสะ. ความทุกข์ เกิดไม่ได้ ถ้าเข้าใจ เรื่องผัสสะ'
# t = "เธอพึงอธิษฐานจงกรม กำหนดหมายเดินกลับไปกลับมา สำรวมอินทรีย์ มีใจไม่คิดไปในภายนอก"

# t = ' 6 6 7 7 8 8 9 9 สิบ สิบ '
# t = 'บุคคลไม่ควรตามคิดถึงสิ่งที่ล่วงไปแล้วด้วยอาลัย และไม่พึงพะวงถึงสิ่งที่ยังไม่มาถึง สิ่งเป็นอดีตก็ละไปแล้ว, สิ่งเป็นอนาคตก็ยังไม่มา'

t = 'จิตเบิกบานหายใจเข้า จิตโล่งเบาหายใจออก'
speech = gTTS(text = t,lang='th',slow = False)
speech.save(str("cheerful_breathing.mp3"))




# เพราะอาศัยจักษุและรูป จึงเกิดจักขุวิญญาณ ความประชุมแห่งธรรม ๓ ประการเป็นผัสสะ
# เพราะผัสสะเป็นปัจจัย จึงเกิดเวทนา เพราะเวทนาเป็นปัจจัย จึงเกิดตัณหา
# เพราะตัณหาเป็นปัจจัย จึงเกิดอุปาทาน เพราะอุปาทานเป็นปัจจัย จึงเกิดภพ
# เพราะภพเป็นปัจจัย จึงเกิดชาติ เพราะชาติเป็นปัจจัย จึงเกิด ชราและมรณะ โสกปริเทวทุกขโทมนัสและอุปายาส

# text = '''
# กลยุทธ์ที่ 1 ปิดฟ้าข้ามทะเล ตัวอย่างการนำเอากลยุทธ์ปิดฟ้าข้ามทะเลไปใช้ได้แก่ลิบองที่ลอบบุกเข้าโจมตีเกงจิ๋วโดยที่กวนอูไม่รู้ตัวแม้แต่น้อย
# กลยุทธ์ที่ 2 ล้อมเวยช่วยจ้าว ตัวอย่างการนำเอากลยุทธ์ล้อมเวยจิ้วจ้าวไปใช้ได้แก่จูกัดเหลียงที่หลอกให้โจโฉนำทัพไปทำศึกสงครามกับซุนกวน และนำทัพบุกเข้ายึดฮันต๋งจากโจโฉมาเป็นของตนได้สำเร็จ
# กลยุทธ์ที่ 3 ยืมดาบฆ่าคน ตัวอย่างการนำเอากลยุทธ์ยืมดาบฆ่าคนไปใช้ได้แก่จิวยี่ที่หลอกให้โจโฉฆ่าซัวมอและเตียวอุ๋น แม่ทัพเรือของตนเองในคราวศึกเซ็กเพ็ก ระหว่างเล่าปี่และซุนกวนจนโจโฉถูกเผาเรือพ่ายแพ้ย่อยยับ
# กลยุทธ์ที่ 4 รอซ้ำยามเปลี้ย ตัวอย่างการนำเอากลยุทธ์รอซ้ำยามเปลี้ยไปใช้ได้แก่ลกซุนที่แนะนำซุนกวนให้พระเจ้าเล่าเสี้ยนนำกำลังทหารไปตีลกเอี๋ยง
# กลยุทธ์ที่ 5 ตีชิงตามไฟ ตัวอย่างการนำเอากลยุทธ์ตีชิงตามไฟไปใช้ได้แก่ตั๋งโต๊ะที่ฉกฉวยโอกาสยึดเอาเมืองหลวงและราชสำนักของพระเจ้าหองจูเหียบมาเป็นของตน และแต่งตั้งตนเองเป็นมหาอุปราชและเป็นบิดาบุญธรรมของพระเจ้าหองจูเปียน
# กลยุทธ์ที่ 6 ส่งเสียงบูรพาฝ่าตีประจิม ตัวอย่างการนำเอากลยุทธ์ส่งเสียงบูรพาฝ่าตีประจิมไปใช้ได้แก่จูกัดเหลียงที่หลอกล่อเฮ็กเจียวให้เกิดความสับสนและหลงทิศในการนำกำลังทหารเฝ้าระวังการบุกเข้าโจมตีด่านตันฉองของจูกัดเหลียงและทหารจ๊กก๊ก
# กลยุทธ์ที่ 7 มีในไม่มี ตัวอย่างการทำเอากลยุทธ์มีในไม่มีไปใช้ได้แก่โจโฉที่วางแผนหลอกลิโป้ให้หลงเชื่อว่าตนเองตายและลอบซุ่มบุกตีโจมตีกระหนาบจนลิโป้พ่ายแพ้ยับเยิน
# กลยุทธ์ที่ 8 ลอบตีเฉินชาง ตัวอย่างการนำเอากลยุทธ์ลอบตีเฉินชางไปใช้ได้แก่ตันฮกที่ให้กวนอูคุมทหารลอบเข้าบุกยึดห้วนเสีย ทำให้โจหยินที่พ่ายแพ้ต้องหนีกลับฮูโต๋
# กลยุทธ์ที่ 9 ดูไฟชายฝั่ง ตัวอย่างการนำเอากลยุทธ์ดูไฟชายฝั่งไปใช้ได้แก่กุยแกที่ให้คำแนะนำแก่โจโฉเพื่อนำกำลังทหารไปตีกิจิ๋วในขณะที่อ้วนซงขึ้นครองกิจิ๋วแทนอ้วนเสี้ยว
# กลยุทธ์ที่ 10 ซ่อนดาบในรอยยิ้ม ตัวอย่างการนำเอากลยุทธ์ซ่อนดาบในรอยยิ้มไปใช้ได้แก่ชีฮูหยินภรรยาของซุนเซียง น้องสะใภ้ของซุนกวนที่วางแผนลอบฆ่าอิหลำที่คิดข่มเหงตนเองเป็นภรรยาด้วยรอยยิ้มประดุจยินดีจะมีสามีใหม่
# กลยุทธ์ที่ 11 หลี่ตายแทนถาว ตัวอย่างการนำเอากลยุทธ์หลี่ตายแทนถาวไปใช้ได้แก่โจโฉที่ยอมเสียหัวของอองเฮานายทหารชั้นผู้น้อย เพื่อแลกกับขวัญและกำลังของทหารทั้งกองทัพ
# กลยุทธ์ที่ 12 จูงแพะติดมือ ตัวอย่างการนำเอากลยุทธ์จูงแพะติดมือไปใช้ได้แก่จูกัดเหลียงที่หลอกเอาลูกเกาฑัณฑ์จำนวนมากจากโจโฉ ตามคำสั่งของจิวยี่ที่สั่งให้จูกัดเหลียงทำลูกเกาฑัณฑ์จำนวนสิบหมื่นให้เสร็จภายในระยะเวลาสามวัน เพื่อหาทางกำจัดจูกัดเหลียงด้วยความอิจฉาริษาที่มีความฉลาดหลักแหลม รู้เท่าทันแผนการของตนเองตลอดเวลา


# '''

# for i in range(len(text)):
#   speech = gTTS(text = text[i],lang='th',slow = False)
#   speech.save(str("36/"+text[i]) + ".mp3")