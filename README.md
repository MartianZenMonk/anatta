# anatta
Project Anatta, Buddhism Corpus for AI assistant developer.
-----
Free question about Buddhism --> intent model ( got keywords ) --> collect passages from Anatta Project Buddhism Corpus ( passages of each keyword from buddhism books database + inverted index ? or + elasticsearch ?) --> multi passages for answer extraction model --> Answers

-----
ในเบื้องต้น น่าจะเป็นการทำระบบฐานข้อมูลของหนังสือธรรมะต่างเพื่อให้ สามารถ จ่าย  passages ที่มี keywords จากคำถามได้ แล้ว เอา คำถาม และ passages ไป หาคำตอบ จาก เอไอ แบบ multi passages for answer extraction model

https://www.youtube.com/watch?v=Y_X7y3WP9WU

BERT : https://www.youtube.com/watch?v=XaQ0CBlQ4cY

-----
https://medium.com/machinereading/elasticsearch-%E0%B8%A0%E0%B8%B2%E0%B8%84%E0%B8%A5%E0%B8%B8%E0%B8%A2%E0%B8%AA%E0%B8%99%E0%B8%B2%E0%B8%A1-%E0%B8%95%E0%B8%AD%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%88-1-19077ab210b3

https://discuss.elastic.co/t/best-approach-to-index-a-book-content/227186

จากบทความข้างบน
ก็น่าจะเอาข้อมูลหนังสือ ใส่ใน  elasticserach
พอค้นด้วย คำที่ต้องการ มันก็จะแสดง หนังสือ ที่ มี คำนั้นมากสุดมาก่อน
แล้ว เราค่อย ไป เอา passages ในหนังสือ นั้น ออกมา ให้

ถ้าจะให้ดีเหมือนว่าต้องทำ Buddhism Searchengine ที่ให้ผลลัพธ์เป็น passages จากหนังสือเล่มต่างๆที่อาจจะมีตำตอบของคำถามอยู่

แต่ถ้ากลัวด้าต้าเบสใหญ่เกิน เปลืองทั้งพื้นที่เก็บและเวลาประมวลผล อาจพิจารณา ทำ แบบ supervised underline sentences passage technique อิอิ คือให้ผู้เชี่ยวชาญอ่านแล้วขีดเส้นใต้ประโยคที่สำคัญในแต่ละบทแล้วนำมาต่อเป็น passage ใหม่ ก่อนเอาเข้า elasticsearch

จึงเดาว่า database ของหนังสือแต่ละเล่ม น่าจะมี 

table ( topic, from_page, from_line, to_page, to_line, underline sentences passage)

table ( page,line, texts )

---
ทดลองทำดาต้าเบส หนังสือ A Brief Introduction to the Buddha-Dhamma ไว้
เก็บข้อมูล ข้อความ เป็นหน้า บรรทัด ไว้

น่า ร่วมมือกับ สำนักงานแม่กองธรรมสนามหลวง รวบรวม ถามตอบ ข้อสอบ ธรรมศึกษา ทำเป็น database ด้วย แต่จะเอาไปใช้ยังไงต้องขอคิดก่อน ฮาๆ แต่คิดว่าน่าจะเอาเข้า elasticsearch ทำใช้เองได้เลย 


