from gtts import gTTS 
import os

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

# text = "ชั่วโมงปฏิบัติธรรม อาจจะเริ่มด้วยการเดินจงกรม ก่อนแล้วค่อยนั่ง เพื่อการ ผ่อนคลาย การเดินจงกรม อาจจะเดิน สามจังหวะ ยก ย่าง เหยียบ หรือ ขวา ย่าง หนอ ซ้าย ย่างหนอ "
# text += "หรือหนึ่งจังหวะ รู้เหยียบ หรือ ขวา พุท ซ้าย โธ"

text = "สัพเพ ธัมมา นาลัง อภินิเวสายะ สิ่งทั้งหลายทั้งปวง ไม่ควรยึดมั่นถือมั่น ธรรมะสวัสดีค่ะ"
speech = gTTS(text = text,lang='th',slow = False)
speech.save("hello.mp3")