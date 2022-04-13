<h1>Project Anatta</h1>
<h2>Goal</h2>
<h4>Open Buddhism Corpus for AI assistant (AI scholar & true friend) developer</h4>
<p>
 Because in the past we believe that the Lord Buddha can know the people mind before he speak his dhamma and it can fix the people problem (dukkha) a lot.
</p>
<p>
Anatta is an assistant AI that will give the advice to people who have dukkha, it will talk to peple (via typing or speaking) and learn about his/her dukkha and then tell him/her the dhamma that she/he should watch or listen to , and the Bhavana practice that he/she should do.
</p>
<p>
Human input ->intent->process->output->feedback
</p>
<p>
 if you need more information please contact TBC
 </p>

<h2>โครงการ อนัตตา</h2>
<h4>จุดประสงค์ จัดทำเผยแพร่ ข้อมูล เกี่ยวกับพุทธศาสนา เพื่อให้ผู้ที่สนใจนำไปพัฒนาระบบเอไอผู้ช่วย ที่เป็น พหูสูต หรือ กัลยาณมิตร</h4>
<p>
 ความเป็นมา<br/>
ในพุทธกาล เชื่อกันว่าพระพุทธเจ้าจะใช้ญาณ ตรวจผู้มาฟังธรรมก่อนเพื่อจะได้เลือกแสดงธรรมที่เหมาะสม

โครงการ อนัตตา เป็นโครงที่จะใช้กระบวนการ crowdsourcing เพื่อ ทำ dataset คลิปธรรมะ (ทำdataset พระไตรปิฏกด้วย) ไว้ให้ผู้สนใจนำไปพัฒนา เป็นเอไอที่จะช่วย แนะนำคลิปธรรมะ นิทานชาดก และ วิธีการปฏิบัติธรรมตามจริต ให้กับ ญาติโยมที่มีความทุกข์ จากการรับฟังและสอบถามเกี่ยวกับความทุกข์ของโยมแต่ละคน
<br/><br/>
Human input ->intent->process->output->feedback
<br/><br/>
แนวทางการดำเนินงานโดยคร่าวๆ สำหรับสื่อ vdo audio คือ<br/>
1 ให้ผู้ที่สนใจ แนะนำคลิปธรรมะที่ตนเองได้ฟังแล้วช่วยลดทุกข์ได้<br/>
2* เผยแพร่คลิปให้อาสาสมัครที่สนใจฟังแล้ว สรุปว่า เหมาะกับคนที่มีทุกข์เรื่องอะไร มีปัญหาอะไร นิสัยแบบไหน หรือ สรุปเนื้อหาเป็น passages และโดยอาจมีแนะนำ ว่า ฟังที่นาทีเท่าไหร่ แล้วกระโดดไปนาทีไหน ทั้งนี้เพราะบางคลิปอาจจะมีน้ำมาก ถ้าทำระบบเล่นได้ตามเวลา ก็ไม่ต้องตัดต่อคลิป แต่แน่นอนว่าเก็บคลิปค้นฉบับไว้ด้วย FAQ พุทธศาสนา <br/>
3 ให้ทีมงาน รวบรวมเป็น dataset เผยแพร่ <br/>
4* จัดทำและเผยแพร่ dataset พระไตรปิฏก และหนังสือธรรมะที่สำคัญอื่นๆเพื่อให้สามารถนำไปเทรน เอไอได้ง่าย
แนวทางสำหรับ พระไตรปิฏก หรือหนังสือ เช่น พุทธธรรม หรือ ชุดธรรมโฆษณ์ ก็อาจพิจารณาทำ database เพื่อให้ นักพัฒนาเขียนสร้าง dataset ตามที่ต้องการได้ 
<br/>
Free question about Buddhism --> intent model ( got keywords ) --> collect passages from Anatta Project Buddhism Corpus ( passages of each keyword from buddhism books database + inverted index ?  elasticsearch ?) --> multi passages for answer extraction model --> Answers
<br/>
ในเบื้องต้น น่าจะเป็นการทำระบบฐานข้อมูลของหนังสือธรรมะต่างเพื่อให้ สามารถ จ่าย passages ที่มี keywords จากคำถามได้ แล้ว เอา คำถาม และ passages ไป หาคำตอบ จาก เอไอ แบบ multi passages for answer extraction model
---
โปรคเจคอนัตตา จึงอาจให้บริการแค่ จัด passages ที่อาจจะมีคำตอบ จาก keywords ที่ได้จากคำถาม ให้เอาไป หาคำตอบจาก โมเดล เอไอ ที่เทรนมาแล้วเอง
---
ถ้าเป็นแบบนี้ ระบบการแจก passages นี่จะออกแบบยังไงให้ดีที่สุดหนอ
<br/>
* ต้องปรึกษากับ นักวิทยาการข้อมูล และ วิศกร เอไอ ก่อน<br/>
ปล มีสอบถามไว้ที่เฟซบุค ได้คำตอบน่าศึกษาต่อ <br/>
https://m.facebook.com/groups/thaidsml/permalink/732015200839051/
<br/><br/>
สิ่งที่ต้องการ <br/>
1 ทีมงาน <br/>
2 งบประมาณ สนับสนุน <br/>
<br/>
สนใจสอบถามข้อมูลเพิ่มเติมเพื่อประกอบการพิจาณาในการตัดสินใจเพื่อให้การสนับสนุนได้ที่ <br/>
TBC
<br/><br/>
<h4>ถ้าเราสร้างเอไอที่ทำหน้าที่เป็นกัลยาณมิตรได้ดี น่าจะช่วยสร้างประโยชน์แก่พุทธศาสนาได้มาก การนำ dataset ไปใช้ เช่น การเอาไปพัฒนาใช้ร่วมกับโครงการ https://mycroft.ai/ </h4>
</p>
<pre>
กัลยาณมิตร คือ มิตรแท้ เพื่อนแท้ เพื่อนตาย เพื่อนที่คอยช่วยเหลือเพื่อนอย่างจริงใจโดยไม่หวังสิ่งใดตอบแทน เป็นมิตรที่หวังดี มีสิ่งดี ๆ ให้กันด้วยความจริงใจ

คุณสมบัติของกัลยาณมิตร (กัลยาณมิตรธรรม 7)

    ปิโย น่ารัก ในฐานเป็นที่สบายใจและสนิทสนม ชวนให้อยากเข้าไปปรึกษา ไต่ถาม
    ครุ น่าเคารพ ในฐานประพฤติสมควรแก่ฐานะ ให้เกิดความรู้สึกอบอุ่นใจ เป็นที่พึ่งใจ และปลอดภัย
    ภาวนีโย น่าเจริญใจ หรือน่ายกย่อง ในฐานทรงคุณ คือ ความรู้และภูมิปัญญาแท้จริง ทั้งเป็นผู้ฝึกอบรมและปรับปรุงตนอยู่เสมอ ควรเอาอย่าง ทำให้ระลึกและเอ่ยอ้างด้วยซาบซึ้งภูมิใจ
    วตฺตา จ รู้จักพูดให้ได้ผล รู้จักชี้แจงให้เข้าใจ รู้ว่าเมื่อไรควรพูดอะไรอย่างไร คอยให้คำแนะนำว่ากล่าวตักเตือน เป็นที่ปรึกษาที่ดี
    วจนกฺขโม อดทนต่อถ้อยคำ คือ พร้อมที่จะรับฟังคำปรึกษาซักถามคำเสนอแนะวิพากษ์วิจารณ์ อดทน ฟังได้ไม่เบื่อ ไม่ฉุนเฉียว
    คมฺภีรญฺจ กถํ กตฺตา แถลงเรื่องล้ำลึกได้ สามารถอธิบายเรื่องยุ่งยากซับซ้อน ให้เข้าใจ และให้เรียนรู้เรื่องราวที่ลึกซึ้งยิ่งขึ้นไป
    โน จฏฐาเน นิโยชเย ไม่ชักนำในอฐาน คือ ไม่แนะนำในเรื่องเหลวไหล หรือชักจูงไปในทางเสื่อมเสีย
</pre>

<h1>Nagasena Project ( 3D model + Audio2Face : AI Monk ) : เอไอพระนักเทศน์</h1>

ไฟล์เสียงที่คัดสรรแล้ว - เป็นข้อความ - ทำความสะอาด - แยกกลุ่ม - รับข้อความ (เหตุการบ้านเมืองจากสื่อโซเชี่ยล เช่น ทวิตเตอร์ก็ได้) - ทำความสะอาด - คาดการอินเทน - เล่นคลิปธรรมะ หรือ เรียบเรียงธรรมะและสร้างเป็นไฟล์เสียง ที่เกี่ยวข้องแบบผสมผสานให้ลงตัว (ในระยะเวลาที่กำหนด) - รับฟังฟีดแบค - เรียนรู้ปรับปรุงระบบให้ดีขึ้น

<h4><a href="https://www.facebook.com/หลวงพ่อสุญญตา-182790273237003/">หลวงพ่อสุญญตา</a></h4>

<div>
 <h4> ธรรมเทศนาว่าด้วย - ปัญญา </h4>
  <p>พรรษากาลเทศนา กัณฑ์ 0๒ -:ไตรสิกขา : ศีลสิกขา-สมาธิสิกขา-ปัญญา... - bdds<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/3023.mp3' type='audio/mp3'></audio></p>
                <p>พรรษากาลเทศนา กัณฑ์ ๑๑ -:ไตรมาส : ศีลมาส-สมาธิมาส-ปัญญามาส - bdds<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/4002.mp3' type='audio/mp3'></audio></p>
                <p>ศิลปะแห่งการดูด้วย ยถาภูตสัมมัปปัญญา - bdds<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/8027.mp3' type='audio/mp3'></audio></p>
                <p>การมีธรรมมะสี่เกลอ : สติ ปัญญา สัมปชัญญะ สมาธิ - bdds<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/10009.mp3' type='audio/mp3'></audio></p>
                <p>คนไทยต้องเข้มแข็งด้วยปัญญา จงลุกขึ้นมาก้าวหน้าไป (๖๐.๕๖) - bdds<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/02_03.mp3' type='audio/mp3'></audio></p>
                <p>รักงาน คือรักแค่ไหน มีปัญญา คือรู้เท่าใด(38.54) - bdds<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/03_02.mp3' type='audio/mp3'></audio></p>
                <p>ฟังคำทำนาย ทำไมจึงมัวตื่นตูม แล้วภูมิปัญญา จะมีมาจากที่ไหน (119.54).mp3 - bdds<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/04_14.mp3' type='audio/mp3'></audio></p>
                <p>๐๓๐๑-ความสัมพันธ์ระหว่างจิตภาวนากับปัญญาภาวนา ๘๔.๕๘ - bdds<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/05_03.mp3' type='audio/mp3'></audio></p>
                <p>๐๘๐๑-จากจิตภาวนาสู่ปัญญาภาวนาตามวิธีสติปัฏฐาน ๔๙.๑๕ - bdds<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/05_21.mp3' type='audio/mp3'></audio></p>
                <p>การศึกษาเริ่มที่ตาหู จะดูฟังได้แค่ตัณหา หรือไปถึงปัญญา นี่คือตัวตัดสิน - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_18.mp3' type='audio/mp3'></audio></p>
                <p>โยมขอศีล พระให้สิกขาบท ขอสมาธิ ให้กรรมฐาน ขอปัญญา ให้คำสอนหรือข้อพิจารณา - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_28.mp3' type='audio/mp3'></audio></p>
                <p>แม้จะมีเพียงวินัยโดยธรรมชาติอย่างฝูงนกและกลีบดอกไม้ ก็ยังดีกว่าคนไร้ปัญญา ไม่รู้จักวินัย - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_29.mp3' type='audio/mp3'></audio></p>
                <p>อยากเป็นคนมีปัญญาดี ถ้าสติไม่มี ก็หมดทางเจริญปัญญา - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_35.mp3' type='audio/mp3'></audio></p>
                <p>ปัญญาเป็นแดนยิ่งใหญ่ ต้องพัฒนากันไป จนกลายเป็นโพธิญาณ - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_36.mp3' type='audio/mp3'></audio></p>
                <p>ในยุคข่าวสารต้องมีปัญญาแตกฉาน ทั้งภาครับและภาคแสดง - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_37.mp3' type='audio/mp3'></audio></p>
                <p>รักษาศีล ๘ อย่าพูดแค่ว่าได้บุญ ต้องรู้ว่าศีล ๘ มาหนุนให้ก้าวไปสู่การพัฒนาจิตใจและปัญญาอย่างไร - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_52.mp3' type='audio/mp3'></audio></p>
                <p>ถ้าไปถึงปัญญา ก็ไม่มัวหลงหาจริยธรรมสากล - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/10_01.mp3' type='audio/mp3'></audio></p>
                <p>รักงานคือรักแค่ไหน มีปัญญาคือรู้เท่าใด(๓๗.๕๙) - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/11_02.mp3' type='audio/mp3'></audio></p>
                <p>จะสมานฉันท์ ต้องสมานปัญญา (๒๙.๑๔) - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/11_05.mp3' type='audio/mp3'></audio></p>
                <p>ปรุงแต่งดี ก็ดี มีปัญญาถึง จึงไม่ปรุงแต่งได้ (๔๕.๕๙ - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/11_15.mp3' type='audio/mp3'></audio></p>
                <p>ถ้าไปถึงปัญญา ก็ไม่มัวหลงหาจริยธรรมสากล [53.33] - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/16_04.mp3' type='audio/mp3'></audio></p>
                <p>คนไทยต้องเข้มแข็งด้วยปัญญา จงลุกขึ้นมาก้าวหน้าไป (๖๐.๕๖) - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/16_14.mp3' type='audio/mp3'></audio></p>
                <p>โรงเรียนต้องช่วยสังคมไทย อนุรักษ์ความเจริญทางจิตใจและก้าวไปในปัญญา 0 - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/14_04.mp3' type='audio/mp3'></audio></p>
                <p>18 จะสมานฉันท์ ต้องสมานปัญญา (30.09) - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/18_18.mp3' type='audio/mp3'></audio></p>
                <p>โรงเรียนต้องช่วยสังคมไทยอนุรักษ์ความเจริญทางจิตใจ และก้าวไปในปัญญา (๔๖.๐๕) - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/12_04.mp3' type='audio/mp3'></audio></p>
                <p>รักงานคือรักแค่ไหน มีปัญญาคือรู้เท่าใด - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/20_07.mp3' type='audio/mp3'></audio></p>
                <p>ปรุงแต่งดี ก็ดี มีปัญญาถึง จึงไม่ปรุงแต่งได้ - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/20_15.mp3' type='audio/mp3'></audio></p>
                <p>วิสาขบูชา เตือนชาวพุทธก้าวให้ถึงปัญญา (50.44) - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/22_07.mp3' type='audio/mp3'></audio></p>
                <p>คนไทยไม่ใจแคบ แต่ระวังไว้อย่าให้ปัญญาแคบ (1.01.55) - payutto<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/22_10.mp3' type='audio/mp3'></audio></p>
                <p>มองด้วยตาปัญญา<br/><audio controls=''><source src='http://thammapedia.com/listen/char/mp3/th_009.mp3' type='audio/mp3'></audio></p>
                <p>หลุดพ้นด้วยปัญญา อบรมภิกษุสามเณร<br/><audio controls=''><source src='http://thammapedia.com/listen/char/mp3/th_015.mp3' type='audio/mp3'></audio></p>
                <p>มีศีลมีปัญญา<br/><audio controls=''><source src='http://thammapedia.com/listen/char/mp3/th_035.mp3' type='audio/mp3'></audio></p>
                <p>ศรัทธากับปัญญา<br/><audio controls=''><source src='http://thammapedia.com/listen/char/mp3/th_044.mp3' type='audio/mp3'></audio></p>
                <p>ปัญญาในวิมุตติ<br/><audio controls=''><source src='http://thammapedia.com/listen/char/mp3/th_088.mp3' type='audio/mp3'></audio></p>
                <p>ทัศนาจรทางปัญญา<br/><audio controls=''><source src='http://thammapedia.com/listen/char/mp3/th_051a.mp3' type='audio/mp3'></audio></p>
                <p>ปัญญามีมาเพราะใจสงบ - char<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/061.mp3' type='audio/mp3'></audio></p>
                <p>ดับไฟภายในด้วยสติปัญญา - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/108.mp3' type='audio/mp3'></audio></p>
                <p>ฆ่าความชั่วด้วยตัวปัญญา - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/125.mp3' type='audio/mp3'></audio></p>
                <p>อยู่ด้วยปัญญา ปัญหาไม่มี - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/156.mp3' type='audio/mp3'></audio></p>
                <p>การเข้าถึงธรรมด้วยปัญญา - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/185.mp3' type='audio/mp3'></audio></p>
                <p>ใช้ปัญญาแก้ปัญหาของเรา - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/196.mp3' type='audio/mp3'></audio></p>
                <p>สติและปัญญาต้องใช้ทุกกรณี - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/275.mp3' type='audio/mp3'></audio></p>
                <p>เปิดใจกว้าง ทางเพิ่มปัญญา - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/279.mp3' type='audio/mp3'></audio></p>
                <p>ใช้ปัญญาค้นหาธรรมแท้ - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/294.mp3' type='audio/mp3'></audio></p>
                <p>ใช้ปัญญาพิจารณาเพื่อปล่อยวาง - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/309.mp3' type='audio/mp3'></audio></p>
                <p>ชาวพุทธต้องเป็นอยู่ด้วยปัญญา - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/350.mp3' type='audio/mp3'></audio></p>
                <p>ใช้ปัญญาแก้ปัญหาสังคม - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/377.mp3' type='audio/mp3'></audio></p>
                <p>ใช้ปัญญาพิจารณาคิดค้น - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/380.mp3' type='audio/mp3'></audio></p>
                <p>แก้ปัญหาชีวิตด้วยธรรมะ (แก้ไขปัญหาชีวิตด้วยปัญญา) - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/389.mp3' type='audio/mp3'></audio></p>
                <p>ใช้ปัญญาพาตนให้พ้นทุกข์ - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/394.mp3' type='audio/mp3'></audio></p>
                <p>มีสติปัญญาพาให้สุข - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/413.mp3' type='audio/mp3'></audio></p>
                <p>วิธีรักษาสุขภาพจิต (สุขภาพดีเพราะปัญญาดี) - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/414.mp3' type='audio/mp3'></audio></p>
                <p>ความเชื่อต้องเจือด้วยปัญญา (รู้รักสามัคคี เพื่อความอยู่ดีของคนในชาติ) - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/432.mp3' type='audio/mp3'></audio></p>
                <p>ศรัทธาต้องคู่กับปัญญา - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/452.mp3' type='audio/mp3'></audio></p>
                <p>ชาวพุทธต้องอยู่ด้วยปัญญา - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/453.mp3' type='audio/mp3'></audio></p>
                <p>ตัวปฏิบัติคือ ศีล สมาธิ ปัญญา - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/471.mp3' type='audio/mp3'></audio></p>
                <p>ใช้สติปัญญาดับไฟข้างใน - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/494.mp3' type='audio/mp3'></audio></p>
                <p>ปัญญาสอนจิต - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/028.mp3' type='audio/mp3'></audio></p>
                <p>จิตที่สงบย่อมเกิดปัญญา - panya<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/048.mp3' type='audio/mp3'></audio></p>
                <p>อบรบ ศีล สมาธิ ปัญญา - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/112.mp3' type='audio/mp3'></audio></p>
                <p>สะสมบุญด้วยศีล สมาธิ ปัญญา - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/145.mp3' type='audio/mp3'></audio></p>
                <p>ปัญญาเป็นอริยสัจธรรม - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/155.mp3' type='audio/mp3'></audio></p>
                <p>ผู้มีปัญญาย่อมแสวงหาแต่ทางที่ชอบ - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/207.mp3' type='audio/mp3'></audio></p>
                <p>สติและปัญญาตามรักษาจิต - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/215.mp3' type='audio/mp3'></audio></p>
                <p>อุบายเจริญวิปัสสนาปัญญา - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/255.mp3' type='audio/mp3'></audio></p>
                <p>จิตจะดีได้ต้องอาศัยปัญญาอบรม - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/302.mp3' type='audio/mp3'></audio></p>
                <p>อบรบจิตเจริญปัญญา - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/352.mp3' type='audio/mp3'></audio></p>
                <p>ขี้ไถทองคำ ศิล สมาธิ ปัญญา - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/424.mp3' type='audio/mp3'></audio></p>
                <p>เจริญปัญญาอบรมจิต - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/461.mp3' type='audio/mp3'></audio></p>
                <p>ผู้มีปัญญาพาชีวิตรอด - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/472.mp3' type='audio/mp3'></audio></p>
                <p>ผู้มีปัญญาก็สามารถพาชีวิตให้พ้นทุกข์ได้ - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/500.mp3' type='audio/mp3'></audio></p>
                <p>ผู้มีปัญญามุ่งละกิเลส - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/524.mp3' type='audio/mp3'></audio></p>
                <p>การตายเป็นบ่อเกิดแห่งปัญญา - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/536.mp3' type='audio/mp3'></audio></p>
                <p>ทางดำเนินของผู้มีปัญญา - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/565.mp3' type='audio/mp3'></audio></p>
                <p>วัฏฏะวนคนมีปัญญาย่อมไม่หลง - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/582.mp3' type='audio/mp3'></audio></p>
                <p>การใช้ปัญญาในทางพระพุทธศาสนา - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/597.mp3' type='audio/mp3'></audio></p>
                <p>ผู้มีปัญญาย่อมแสวงบุญ - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/754.mp3' type='audio/mp3'></audio></p>
                <p>ชาวพุทธควรมีปัญญา - riean<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/755.mp3' type='audio/mp3'></audio></p>

                <h4> ธรรมเทศนาว่าด้วย - อริยสัจจ์ </h4>
                <p>อาสาฬหบูชาเทศนา พ.ศ. ๒๕๒๙ กัณฑ์ ๒ -: อริยสัจจ์<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/6027.mp3' type='audio/mp3'></audio></p>
                <p>อาสาฬหบูชาเทศนา พ.ศ. ๒๕๓๑ กัณฑ์ที่ ๑ -: อตัมมยตากับอริยสัจจส...<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/6030.mp3' type='audio/mp3'></audio></p>
                <p>สรุปปฎิจจสมุปบาทและอริยสัจจ์<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/12003.mp3' type='audio/mp3'></audio></p>
                <p>แม้จะพูดถึงอริยสัจสี่กันสักเท่าไร ก็ไม่มีทางเข้าใจ ถ้าไม่รู้หลักหน้าที่ต่ออริยสัจ<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_42.mp3' type='audio/mp3'></audio></p>
                <p>ก่อนจะเข้าเนื้อ มาดูหนังอริยสัจกันก่อน<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_43.mp3' type='audio/mp3'></audio></p>
                <p>ดูขันธ์ ๕ ให้เห็นการทำงานของชีวิต พอได้พื้นความเข้าใจที่จะไปเรียนอริยสัจ<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_44.mp3' type='audio/mp3'></audio></p>
                <p>ชอบอ้างกันนักว่าอริยสัจสี่ แต่แค่หน้าที่ปริญญา ก็ยังไม่รู้จัก  [23.00]<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/13_20.mp3' type='audio/mp3'></audio></p>
                <p>ชอบอ้างกันนักว่าอริยสัจสี่  แต่แค่หน้าที่ปริญญา ก็ยังไม่รู้จัก (ส่วน ถาม-ตอบ) [40.08]<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/13_21.mp3' type='audio/mp3'></audio></p>
                <p>ปัญญาเป็นอริยสัจธรรม<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/155.mp3' type='audio/mp3'></audio></p>

 <h4> ธรรมเทศนาว่าด้วย - อริยสัจจ์ </h4>
                <p>อาสาฬหบูชาเทศนา พ.ศ. ๒๕๒๙ กัณฑ์ ๒ -: อริยสัจจ์<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/6027.mp3' type='audio/mp3'></audio></p>
                <p>อาสาฬหบูชาเทศนา พ.ศ. ๒๕๓๑ กัณฑ์ที่ ๑ -: อตัมมยตากับอริยสัจจส...<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/6030.mp3' type='audio/mp3'></audio></p>
                <p>สรุปปฎิจจสมุปบาทและอริยสัจจ์<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/12003.mp3' type='audio/mp3'></audio></p>
                <p>แม้จะพูดถึงอริยสัจสี่กันสักเท่าไร ก็ไม่มีทางเข้าใจ ถ้าไม่รู้หลักหน้าที่ต่ออริยสัจ<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_42.mp3' type='audio/mp3'></audio></p>
                <p>ก่อนจะเข้าเนื้อ มาดูหนังอริยสัจกันก่อน<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_43.mp3' type='audio/mp3'></audio></p>
                <p>ดูขันธ์ ๕ ให้เห็นการทำงานของชีวิต พอได้พื้นความเข้าใจที่จะไปเรียนอริยสัจ<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_44.mp3' type='audio/mp3'></audio></p>
                <p>ชอบอ้างกันนักว่าอริยสัจสี่ แต่แค่หน้าที่ปริญญา ก็ยังไม่รู้จัก  [23.00]<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/13_20.mp3' type='audio/mp3'></audio></p>
                <p>ชอบอ้างกันนักว่าอริยสัจสี่  แต่แค่หน้าที่ปริญญา ก็ยังไม่รู้จัก (ส่วน ถาม-ตอบ) [40.08]<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/13_21.mp3' type='audio/mp3'></audio></p>
                <p>ปัญญาเป็นอริยสัจธรรม<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/155.mp3' type='audio/mp3'></audio></p>

                <h4> ธรรมเทศนาว่าด้วย - ทุกข์ </h4>
                <p>การดับทุกข์เป็นหน้าที่ของทุกคน<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/1011.mp3' type='audio/mp3'></audio></p>
                <p>ทำอย่างไรจึงจะไม่เป็นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/2015.mp3' type='audio/mp3'></audio></p>
                <p>ทุกข์และความดับไม่เหลือแห่งทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/2016.mp3' type='audio/mp3'></audio></p>
                <p>พรรษากาลเทศนา กัณฑ์ 0๔ -:การหาความสุขจากสิ่งที่เป็นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/4019.mp3' type='audio/mp3'></audio></p>
                <p>เทศน์วันออกพรรษา -:การออกจากสิ่งที่ทำให้เป็นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/5004.mp3' type='audio/mp3'></audio></p>
                <p>มาฆบูชาเทศนา กัณฑ์ ๓ -:การวางของหนักคือการดับทุกข์ <br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/5014.mp3' type='audio/mp3'></audio></p>
                <p>วิสาขบูชาเทศนา กัณฑ์ ๒ -:ทำลายเหตุแห่งความทุกข์กันเถิด<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/6009.mp3' type='audio/mp3'></audio></p>
                <p>อาสาฬหบูชาเทศนา พ.ศ. ๒๕๒๙ กัณฑ์ ๓ -: ความทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/6028.mp3' type='audio/mp3'></audio></p>
                <p>สิ่งแรกที่ต้องรู้จักนั้นคือความทุกข์.<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/12020.mp3' type='audio/mp3'></audio></p>
                <p>หนีทุกข์อยากมีสุขกันนัก แต่ไม่รู้จักว่าเจอมันเข้าจะเอาอย่างไร<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_55.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตและสังคมทุกข์ระทมถึงขั้นวิกฤต ก็เพราะคนจมติดอยู่แค่ความสุขที่พึ่งพาการเสพ<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_57.mp3' type='audio/mp3'></audio></p>
                <p>ไฮเทค ไฮทุกข์ (๓๐.๒๙)<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/15_08.mp3' type='audio/mp3'></audio></p>
                <p>หนีทุกข์อยากมีความสุขกันนัก  แต่ไม่รู้จักว่าเจอมันเข้าจะเอาอย่างไร(๓๐.๐๐)<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/21_09.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตและสังคมทุกข์ระทมถึงขั้นวิกฤต  ก็เพราะคนจะจมติดอยู่แค่ความสุขที่พึ่งพาการเสพ(๔๖.๓๖)<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/21_11.mp3' type='audio/mp3'></audio></p>
                <p>ถึงจะมีความสุข แต่จะให้เป็นสุขแท้ไม่มีทุกข์ ก็ต้องปฏิบัติต่อสุขนั้นให้ถูก (๕๒.๒๗)<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/21_14.mp3' type='audio/mp3'></audio></p>
                <p>สูตรแก้ทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/char/mp3/045.mp3' type='audio/mp3'></audio></p>
                <p>เห็นผิดแล้วทุกข์ เห็นถูกแล้วสบาย<br/><audio controls=''><source src='http://thammapedia.com/listen/char/mp3/050.mp3' type='audio/mp3'></audio></p>
                <p>อุปทานขันธ์ห้า...เป็นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/char/mp3/052.mp3' type='audio/mp3'></audio></p>
                <p>การปฏิบัติเพื่อพ้นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/char/mp3/087.mp3' type='audio/mp3'></audio></p>
                <p>ยืน เดิน นั่ง นอน ปราศจากทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/char/mp3/056A.mp3' type='audio/mp3'></audio></p>
                <p>ทางแก้ทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/042.mp3' type='audio/mp3'></audio></p>
                <p>ทางเกิดของเพลิงทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/097.mp3' type='audio/mp3'></audio></p>
                <p>สุขทุกข์อยู่ที่ใจ<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/113.mp3' type='audio/mp3'></audio></p>
                <p>วางแผนชีวิตพิชิตความทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/117.mp3' type='audio/mp3'></audio></p>
                <p>เป็นทุกข์ได้ทั้งยินร้ายยินดี<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/191.mp3' type='audio/mp3'></audio></p>
                <p>ความยึดมั่นถือมั่นเป็นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/232.mp3' type='audio/mp3'></audio></p>
                <p>เคล็ดลับของความดับทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/248.mp3' type='audio/mp3'></audio></p>
                <p>วิถีทางดับทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/250.mp3' type='audio/mp3'></audio></p>
                <p>การเกิดที่เป็นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/252.mp3' type='audio/mp3'></audio></p>
                <p>ถอนตนให้พ้นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/256.mp3' type='audio/mp3'></audio></p>
                <p>รู้จักสมมติ ปลดทุกข์ได้<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/277.mp3' type='audio/mp3'></audio></p>
                <p>การยึดถือเป็นเหตุของความทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/344.mp3' type='audio/mp3'></audio></p>
                <p>ปล่อยวางปลดทุกข์ จะสุขใจ<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/360.mp3' type='audio/mp3'></audio></p>
                <p>ธรรมที่ช่วยให้พ้นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/388.mp3' type='audio/mp3'></audio></p>
                <p>ใช้ปัญญาพาตนให้พ้นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/394.mp3' type='audio/mp3'></audio></p>
                <p>ทุกข์มีเพราะการยึดถือ<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/399.mp3' type='audio/mp3'></audio></p>
                <p>หลักการแก้ทุกข์ (หลักธรรมสำหรัแก้ปัญหาชีวิต)<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/404.mp3' type='audio/mp3'></audio></p>
                <p>แนวทางแก้หขความทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/416.mp3' type='audio/mp3'></audio></p>
                <p>ความทุกข์เกิดจากความยึดถือ<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/441.mp3' type='audio/mp3'></audio></p>
                <p>กิเลสเผาเราเป็นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/462.mp3' type='audio/mp3'></audio></p>
                <p>ดับเพลิงกิเลสเพลิงทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/463.mp3' type='audio/mp3'></audio></p>
                <p>รู้ทันรู้เท่าไม่เศร้าไม่ทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/480.mp3' type='audio/mp3'></audio></p>
                <p>เพราะเราโง่จึงเป็นทุกข์ (มองให้เห็นความเป็นจริง)<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/496.mp3' type='audio/mp3'></audio></p>
                <p>รู้จักคิดชีวิตไม่ทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/500.mp3' type='audio/mp3'></audio></p>
                <p>ฉลาดเป็นสุข ทุกข์เพราะโง่<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/521.mp3' type='audio/mp3'></audio></p>
                <p>สอนให้รู้เท่าทันทุกข์ตามความเป็นจริง<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/025.mp3' type='audio/mp3'></audio></p>
                <p>สุขทุกข์อยู่ที่ใจดีหรือใจร้าย<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/121.mp3' type='audio/mp3'></audio></p>
                <p>ผู้ใดไม่สำรวมจิตย่อมก่อทุกข์ให้ตน<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/122.mp3' type='audio/mp3'></audio></p>
                <p>บุคคลไม่ฝึกจิต ย่อมอยู่เป็นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/134.mp3' type='audio/mp3'></audio></p>
                <p>ควรถอนตนออกจากทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/135.mp3' type='audio/mp3'></audio></p>
                <p>จะพ้นทุกข์ได้ต้องอาศัยตนเอง<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/150.mp3' type='audio/mp3'></audio></p>
                <p>กิเลสตัณหาพาท่องทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/169.mp3' type='audio/mp3'></audio></p>
                <p>มีทุกข์อยู่ไม่รู้จักทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/172.mp3' type='audio/mp3'></audio></p>
                <p>ข้อปฎิบัติให้ถึงความดับทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/187.mp3' type='audio/mp3'></audio></p>
                <p>ไม่เห็นทุกข์จะพ้นทุกข์ได้อย่างไร<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/248.mp3' type='audio/mp3'></audio></p>
                <p>จะพ้นทุกข์ได้ต้องอาศัยฝึกจิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/284.mp3' type='audio/mp3'></audio></p>
                <p>การส่งจิตไปยึดสมบัติภายนอกเป็นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/286.mp3' type='audio/mp3'></audio></p>
                <p>ตันหาพาท่องทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/291.mp3' type='audio/mp3'></audio></p>
                <p>อนิจจัง ทุกข์ขัง อนัตตา<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/297.mp3' type='audio/mp3'></audio></p>
                <p>ภาวนารู้เท่าทุกข์ในขันธ์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/312.mp3' type='audio/mp3'></audio></p>
                <p>เพราะไม่รู้ธรรมของจริงจึงเที่ยวทุกข์ในสงสาร<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/321.mp3' type='audio/mp3'></audio></p>
                <p>ความทุกข์ในชีวิตมีมากมาย<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/327.mp3' type='audio/mp3'></audio></p>
                <p>ตันหาพาก่อทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/339.mp3' type='audio/mp3'></audio></p>
                <p>ผู้เกียจคร้านย่อมอยู่เป็นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/364.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตมีความทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/371.mp3' type='audio/mp3'></audio></p>
                <p>ทุกข์สิ่งเสื่อมและดับไป<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/382.mp3' type='audio/mp3'></audio></p>
                <p>สุขทุกข์อยู่กับเหตุ<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/406.mp3' type='audio/mp3'></audio></p>
                <p>ความยึดถือเป็นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/440.mp3' type='audio/mp3'></audio></p>
                <p>ชาติความเกิดเป็นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/455.mp3' type='audio/mp3'></audio></p>
                <p>ตัณหาพาท่องทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/465.mp3' type='audio/mp3'></audio></p>
                <p>พิจารณาทุกข์ในธาตุขันธ์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/469.mp3' type='audio/mp3'></audio></p>
                <p>เหตุแห่งสุข เหตุแห่งทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/478.mp3' type='audio/mp3'></audio></p>
                <p>ขึ้นชื่อว่าบาปแม้แต่น้อยก็มีทุกข์เป็นผล<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/484.mp3' type='audio/mp3'></audio></p>
                <p>ราคะตัณหาพาท่องทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/489.mp3' type='audio/mp3'></audio></p>
                <p>เพียรเห็นทุกข์ภัยในกามทั้งหลาย<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/491.mp3' type='audio/mp3'></audio></p>
                <p>เหตุแห่งทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/494.mp3' type='audio/mp3'></audio></p>
                <p>ผู้มีปัญญาก็สามารถพาชีวิตให้พ้นทุกข์ได้<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/500.mp3' type='audio/mp3'></audio></p>
                <p>ผู้เห็นทุกข์ต้องลุกขึ้นภาวนา<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/502.mp3' type='audio/mp3'></audio></p>
                <p>หาเลี้ยงทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/503.mp3' type='audio/mp3'></audio></p>
                <p>ตัณหาพาท่องทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/510.mp3' type='audio/mp3'></audio></p>
                <p>ทุกข์สมุทัย<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/513.mp3' type='audio/mp3'></audio></p>
                <p>ผู้อยู่ย่อมไม่มีที่พึ่งย่อมเป็นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/528.mp3' type='audio/mp3'></audio></p>
                <p>สงบกิเลส หมดเหตุแห่งทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/534.mp3' type='audio/mp3'></audio></p>
                <p>ตัณหาเหตุแห่งทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/567.mp3' type='audio/mp3'></audio></p>
                <p>การเกิดบ่อยเป็นทุกข์บ่อยๆ<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/578.mp3' type='audio/mp3'></audio></p>
                <p>ทุกข์เป็นภัยของสัตว์โลก<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/583.mp3' type='audio/mp3'></audio></p>
                <p>เพราะหลงเหยื่อล่อจึงไม่เบื่อทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/596.mp3' type='audio/mp3'></audio></p>
                <p>สุขทุกข์อยู่ที่จิตดวงเดียว<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/602.mp3' type='audio/mp3'></audio></p>
                <p>ออกแสวงหาทางพ้นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/606.mp3' type='audio/mp3'></audio></p>
                <p>ทุกข์หนอๆ<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/610.mp3' type='audio/mp3'></audio></p>
                <p>แดนเกิดแห่งทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/614.mp3' type='audio/mp3'></audio></p>
                <p>จะเป็นสุขก็ต้องเอาทุกข์เป็นทุนไปก่อน<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/616.mp3' type='audio/mp3'></audio></p>
                <p>ให้ทุกข์แก่ท่านทุกข์นั้นถึงตัว<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/619.mp3' type='audio/mp3'></audio></p>
                <p>ให้เห็นทุกข์ในชาติความเกิด<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/632.mp3' type='audio/mp3'></audio></p>
                <p>ติดสุขชั่วคราวย่อมเข้าถึงทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/640.mp3' type='audio/mp3'></audio></p>
                <p>ทุกข์คนต้องพัฒนาตัวเอง<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/656.mp3' type='audio/mp3'></audio></p>
                <p>ชี้ทางบรรเทาทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/658.mp3' type='audio/mp3'></audio></p>
                <p>เอาทุกข์เป็นทุนเอาบุญเป็นกำไร<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/666.mp3' type='audio/mp3'></audio></p>
                <p>เอาความดีเป็นเครื่องบรรเทาทุกข์ทางใจ000000<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/667.mp3' type='audio/mp3'></audio></p>
                <p>ยึดสิ่งใดย่อมทุกข์กับสิ่งนั้น<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/684.mp3' type='audio/mp3'></audio></p>
                <p>จะพ้นทุกข์ทางใจได้อย่างไร<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/690.mp3' type='audio/mp3'></audio></p>
                <p>คนเราพ้นทุกข์ไปไม่ได้เพราะความไม่รู้<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/691.mp3' type='audio/mp3'></audio></p>
                <p>จิตไม่ยอมอยู่กับทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/696.mp3' type='audio/mp3'></audio></p>
                <p>ก้าวสู่ทางพ้นทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/716.mp3' type='audio/mp3'></audio></p>
                <p>พิจารณาทุกข์ของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/718.mp3' type='audio/mp3'></audio></p>
                <p>อุปาทานขันธ์ห้าเป็นตัวทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/721.mp3' type='audio/mp3'></audio></p>
                <p>ธรรมเครื่องบรรเทาทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/722.mp3' type='audio/mp3'></audio></p>

                <h4> ธรรมเทศนาว่าด้วย - มรรค </h4>
                <p>พรรษากาลเทศนา กัณฑ์ 0๓ -:ไตรโลกุตตรธรรม : มรรค-ผล-นิพพาน<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/3024.mp3' type='audio/mp3'></audio></p>
                <p>อัฏฐังคิกมรรคยอกศิลปะแห่งการครองชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/8025.mp3' type='audio/mp3'></audio></p>
                <p>นับถือเทวดายังพอฟัง แต่ถ้ามัวหวังพึ่งขอผล ก็หล่นจากอริยมรรคไม่เหลือดี ตอนที่ ๑ (๔๘.๒๖)<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/02_08.mp3' type='audio/mp3'></audio></p>
                <p>นับถือเทวดายังพอฟัง แต่ถ้ามัวหวังพึ่งขอผล ก็หล่นจากอริยมรรคไม่เหลือดี ตอนที่ ๒ (๔๖.๒๗)<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/02_09.mp3' type='audio/mp3'></audio></p>
                <p>นับถือเทวดายังพอฟัง แต่ถ้ามัวหวังพึ่งขอผล ก็หล่นจากอริยมรรค ไม่เหลือดี(93.56).MP3<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/04_12.mp3' type='audio/mp3'></audio></p>
                <p>นับถือเทวดายังพอฟัง แต่ถ้ามัวหวังพึ่งขอผล ก็หล่นจากอริยมรรคไม่เหลือดี<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_13.mp3' type='audio/mp3'></audio></p>
                <p>ฝึกคน ๓ แดน คนก็เดินไปในวิถีชีวิตดีงามที่เรียกว่ามรรค<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_32.mp3' type='audio/mp3'></audio></p>
                <p>มรรคมีองค์ ๘ ก็กระจายออกไปจากวิถีชีวิตดีงาม ๓ แดน นี่เอง<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_33.mp3' type='audio/mp3'></audio></p>
                <p>ดูมรรคมีองค์ ๘ ให้เห็นวิถีชีวิตที่ดีงาม ว่าดำเนินไปอย่างไร<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_45.mp3' type='audio/mp3'></audio></p>
                <p>สัมมามรรค - มิจฉามรรค<br/><audio controls=''><source src='http://thammapedia.com/listen/char/mp3/043.mp3' type='audio/mp3'></audio></p>

                <h4> ธรรมเทศนาว่าด้วย - ชีวิต </h4>
                <p>การทำงานคือการปฏิบัติธรรม การมีชีวิตด้วยจิตว่าง<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/1015.mp3' type='audio/mp3'></audio></p>
                <p>การมีชีวิตด้วยจิตว่าง<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/1016.mp3' type='audio/mp3'></audio></p>
                <p>การมีนิพพานในชีวิตประจำวัน<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/1023.mp3' type='audio/mp3'></audio></p>
                <p>คุณค่าของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/2008.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตคืออะไร<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/2011.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตเป็นสิ่งที่ต้องพัฒนา<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/2012.mp3' type='audio/mp3'></audio></p>
                <p>ธรรมะในฐานะเป็นเครื่องดำเนินชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/2024.mp3' type='audio/mp3'></audio></p>
                <p>เป้าหมายของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/2030.mp3' type='audio/mp3'></audio></p>
                <p>ส่วนประกอบและโครงสร้างของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/3018.mp3' type='audio/mp3'></audio></p>
                <p>มาฆบูชาเทศนา กัณฑ์ ๑ -:การมีชีวิตอยู่เหนือความชั่ว-ดี<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/5021.mp3' type='audio/mp3'></audio></p>
                <p>มาฆบูชาเทศนา กัณฑ์ ๒ -:อตัมมยตา มนตราสำหรับชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/5024.mp3' type='audio/mp3'></audio></p>
                <p>มาฆบูชาเทศนา กัณฑ์ ๓ -:การมีชีวิตอยู่ด้วยธรรมะ<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/6001.mp3' type='audio/mp3'></audio></p>
                <p>มาฆบูชาเทศนา กัณฑ์ ๔ -:ทางเดินของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/6002.mp3' type='audio/mp3'></audio></p>
                <p>การทำชีวิตให้มีธรรมะ<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/7022.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตเป็นสิ่งที่พัฒนาได้และต้องพัฒนา<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/7030.mp3' type='audio/mp3'></audio></p>
                <p>การมีธรรมะในการครองชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/8002.mp3' type='audio/mp3'></audio></p>
                <p>ศาสนาของคู่กันกับชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/8010.mp3' type='audio/mp3'></audio></p>
                <p>ปรมัตถศิลป์แห่งการครองชีวิตตามทัศนของชาวพุทธ<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/8021.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตในฐานะเป็นวัตถุแห่งศิลปะ<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/8022.mp3' type='audio/mp3'></audio></p>
                <p>ศิลปะแห่งการมีชีวิตอยู่เหนือปัญหา<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/8023.mp3' type='audio/mp3'></audio></p>
                <p>ศิลปะสำหรับการมีชีวิตอยู่ในโลก<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/8024.mp3' type='audio/mp3'></audio></p>
                <p>อัฏฐังคิกมรรคยอกศิลปะแห่งการครองชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/8025.mp3' type='audio/mp3'></audio></p>
                <p>ศิลปะแห่งการอยู่กับนิพพานในชีวิตประจำวัน<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/8029.mp3' type='audio/mp3'></audio></p>
                <p>ศิลปะแห่งการมีชีวิตอยู่ด้วยจิตว่าง<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/9001.mp3' type='audio/mp3'></audio></p>
                <p>ธรรมะนั่นแหละคือคู่ชีวิตที่แท้จริง<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/9003.mp3' type='audio/mp3'></audio></p>
                <p>การมีชีวิตชนิดที่ไม่กัดเจ้าของ<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/9004.mp3' type='audio/mp3'></audio></p>
                <p>ความลึกซึ้งของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/9007.mp3' type='audio/mp3'></audio></p>
                <p>การมีชีวิตชนิดที่น่าพอใจ<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/9008.mp3' type='audio/mp3'></audio></p>
                <p>พลังผลักดันของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/9010.mp3' type='audio/mp3'></audio></p>
                <p>การมีธรรมะประกอบอยู่กับชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/9012.mp3' type='audio/mp3'></audio></p>
                <p>วิถีแห่งชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/9018.mp3' type='audio/mp3'></audio></p>
                <p>หลักการดำเนินชีวิตที่น่าพอใจ<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/9020.mp3' type='audio/mp3'></audio></p>
                <p>ธรรมะโดยแท้จริง เพื่อชีวิตที่สมบูรณ์<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/9028.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตนี้มีค่า<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/9030.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตบริหาร : การบริหารชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/10002.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตอันประเสริฐ<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/10029.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตว่าง<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/10030.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตกีฬา: ชีวิตที่สนุกเหมือนเล่นกีฬา<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/11001.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตคือขันธ์ทั้งห้ามิใช่ตัวตน.<br/><audio controls=''><source src='http://thammapedia.com/listen/bdds/mp3/12022.mp3' type='audio/mp3'></audio></p>
                <p>ทางสายกลาง เพื่อชีวิตสังคมที่สุขสมบูรณ์ (พระคันธกุฎี)<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/07_09.mp3' type='audio/mp3'></audio></p>
                <p>ฟื้นวินัยชาวพุทธขึ้นมา ให้เป็นวิถีชีวิตของสังคมไทย 41.44<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/08_16.mp3' type='audio/mp3'></audio></p>
                <p>พอบวชพ้นอกพ่อแม่ ต้องรู้ให้แน่ ว่าจะมีชีวิตเป็นอยู่อย่างไร<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_02.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตพระใหม่ เริ่มต้นอย่างไร จึงจะพอให้ชื่นใจว่าเราได้บวชเรียน<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_05.mp3' type='audio/mp3'></audio></p>
                <p>ถ้าเข้าถึงความจริงของธรรมชาติ แล้วเอามาจัดการชีวิตและสังคมให้ดีได้  ก็จบความหมายของพระพุทธศาสนา<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_27.mp3' type='audio/mp3'></audio></p>
                <p>การพัฒนาชีวิต พัฒนาสังคม จะไม่ล่มสลาย ถ้าวินัยยังอยู่เป็นฐาน<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_30.mp3' type='audio/mp3'></audio></p>
                <p>ฝึกคน ๓ แดน คนก็เดินไปในวิถีชีวิตดีงามที่เรียกว่ามรรค<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_32.mp3' type='audio/mp3'></audio></p>
                <p>มรรคมีองค์ ๘ ก็กระจายออกไปจากวิถีชีวิตดีงาม ๓ แดน นี่เอง<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_33.mp3' type='audio/mp3'></audio></p>
                <p>ดูขันธ์ ๕ ให้เห็นการทำงานของชีวิต พอได้พื้นความเข้าใจที่จะไปเรียนอริยสัจ<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_44.mp3' type='audio/mp3'></audio></p>
                <p>ดูมรรคมีองค์ ๘ ให้เห็นวิถีชีวิตที่ดีงาม ว่าดำเนินไปอย่างไร<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_45.mp3' type='audio/mp3'></audio></p>
                <p>ทางชีวิตดีงามมีอยู่ก็ดีแล้ว แต่คนที่ยังอยู่นอกทางเล่า ทำอย่างไรจะให้เขาเข้ามาเดิน<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_46.mp3' type='audio/mp3'></audio></p>
                <p>แสงอรุณยืนยันการขึ้นมาของดวงอาทิตย์ แล้วอะไรเป็นบุพนิมิตของการเข้าสู่วิถีชีวิตที่ดีงาม ตอนที่ ๑<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_48.mp3' type='audio/mp3'></audio></p>
                <p>แสงอรุณยืนยันการขึ้นมาของดวงอาทิตย์ แล้วอะไรเป็นบุพนิมิตของการเข้าสู่วิถีชีวิตที่ดีงาม ตอนที่ ๒<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_49.mp3' type='audio/mp3'></audio></p>
                <p>ทางชีวิตของอารยชน เริ่มต้นด้วยปัจจัย ๒ มีหน่วยหนุนประคองอีก ๕ รวมเป็นแสงอรุณ ๗ รัศมี<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_50.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตและสังคมทุกข์ระทมถึงขั้นวิกฤต ก็เพราะคนจมติดอยู่แค่ความสุขที่พึ่งพาการเสพ<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/09_57.mp3' type='audio/mp3'></audio></p>
                <p>มองอนาคตผ่านรากฐานความคิด ผ่านชีวิตท่านพุทธทาส  [57.34]<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/13_18.mp3' type='audio/mp3'></audio></p>
                <p>2 ทางแยกแห่งชีวิต ที่เริ่มจากอายตนะ (1. สายความรู้สึก 2. สายความรู้)<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/14_02.mp3' type='audio/mp3'></audio></p>
                <p>สู่ชีวิตแห่งการศึกษาและสร้างสรรค์ บนฐานของอายตนะ 6 1:07:46<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/14_03.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตพระที่แท้ อุทิศให้แก่โลก (๗๔.๓๐)<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/12_15.mp3' type='audio/mp3'></audio></p>
                <p>มองอนาคตผ่านรากฐานความคิด และชีวิตท่านพุทธทาส<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/20_16.mp3' type='audio/mp3'></audio></p>
                <p>จะเป็นใครก็มีความสุขได้ ขอเพียงให้ใช้ชีวิตให้เป็น (ใหม่) (๔๖.๓๒)<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/21_02.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตและสังคมทุกข์ระทมถึงขั้นวิกฤต  ก็เพราะคนจะจมติดอยู่แค่ความสุขที่พึ่งพาการเสพ(๔๖.๓๖)<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/21_11.mp3' type='audio/mp3'></audio></p>
                <p>พัฒนาชีวิตกันไปเถิด  ความสุขจะเกิดมีแน่ ไม่หนีไปไหน (๘๘.๒๓)<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/21_15.mp3' type='audio/mp3'></audio></p>
                <p>ปีใหม่ ต้อนรับหรือท้าทาย และจุดหมายชีวิต (1.02.22)<br/><audio controls=''><source src='http://thammapedia.com/listen/payutto/mp3/22_15.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตแต่งงาน ครอบครัว<br/><audio controls=''><source src='http://thammapedia.com/listen/char/mp3/011.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตไม่มีบทบอก<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/024.mp3' type='audio/mp3'></audio></p>
                <p>ชี้ทางชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/032.mp3' type='audio/mp3'></audio></p>
                <p>วิธีแก้ปัญหาชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/039.mp3' type='audio/mp3'></audio></p>
                <p>ฐานของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/041.mp3' type='audio/mp3'></audio></p>
                <p>จุดยืนของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/085.mp3' type='audio/mp3'></audio></p>
                <p>รากฐานที่มั่นคงของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/088.mp3' type='audio/mp3'></audio></p>
                <p>ฐานรองของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/089.mp3' type='audio/mp3'></audio></p>
                <p>ปัญหาชีวิตต้องพิชิตด้วยธรรมะ<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/094.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตกับสภาพแวดล้อม<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/115.mp3' type='audio/mp3'></audio></p>
                <p>ศีลธรรมเป็นกรอบชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/116.mp3' type='audio/mp3'></audio></p>
                <p>วางแผนชีวิตพิชิตความทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/117.mp3' type='audio/mp3'></audio></p>
                <p>ธรรมะในชีวิตประจำวัน<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/119.mp3' type='audio/mp3'></audio></p>
                <p>ธรรมชาติของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/126.mp3' type='audio/mp3'></audio></p>
                <p>แว่นธรรมส่องมองชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/127.mp3' type='audio/mp3'></audio></p>
                <p>สร้างชีวิตต้องคิดก้าวหน้า<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/130.mp3' type='audio/mp3'></audio></p>
                <p>ทำชีวิตให้เป็นสุขตามหลักธรรม<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/140.mp3' type='audio/mp3'></audio></p>
                <p>ทางเดินชีวิตที่ถูกต้อง<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/169.mp3' type='audio/mp3'></audio></p>
                <p>จงใช้ชีวิตให้เป็นประโยชน์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/171.mp3' type='audio/mp3'></audio></p>
                <p>เลิกสิ่งเสพติดชีวิตผ่องใส<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/182.mp3' type='audio/mp3'></audio></p>
                <p>ที่พึ่งและชีวิตใหม่<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/188.mp3' type='audio/mp3'></audio></p>
                <p>ศิลปะของการดำรงชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/192.mp3' type='audio/mp3'></audio></p>
                <p>ธรรมะที่ใช้แก้ปัญหาชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/220.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตและผลงานท่านพุทธทาส<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/224.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตในวัยเด็กของข้าพเจ้า<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/234.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตนี้ต้องการอะไร<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/249.mp3' type='audio/mp3'></audio></p>
                <p>ทางชีวิตที่ประเสริฐ<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/251.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตคืออะไร<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/257.mp3' type='audio/mp3'></audio></p>
                <p>ความคิดที่นำชีวิตถูกต้อง<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/274.mp3' type='audio/mp3'></audio></p>
                <p>แสงสว่างของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/278.mp3' type='audio/mp3'></audio></p>
                <p>เชื่อมั่นในธรรม นำชีวิตมั่นคง<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/286.mp3' type='audio/mp3'></audio></p>
                <p>สร้างความคิดริเริ่ม เสริมคุณค่าชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/293.mp3' type='audio/mp3'></audio></p>
                <p>เมตตา พาให้สุขทุกชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/297.mp3' type='audio/mp3'></audio></p>
                <p>ศีลธรรมเป็นระบบของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/313.mp3' type='audio/mp3'></audio></p>
                <p>ธรรมที่ทำให้ชีวิตเจริญก้าวหน้า<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/338.mp3' type='audio/mp3'></audio></p>
                <p>คุณธรรมนำชีวิตปลอดภัย<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/341.mp3' type='audio/mp3'></audio></p>
                <p>ศาสนาเป็นหลักพัฒนาชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/342.mp3' type='audio/mp3'></audio></p>
                <p>ตัวอย่างชีวิตที่น่าศึกษา<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/374.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตและงานของหลวงพ่อพุทธทาส<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/376.mp3' type='audio/mp3'></audio></p>
                <p>ธรรมนูญชีวิต (ศีลเป็นระบบของชีวิต)<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/379.mp3' type='audio/mp3'></audio></p>
                <p>สิ่งที่ชีวิตต้องการ<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/381.mp3' type='audio/mp3'></audio></p>
                <p>แก้ปัญหาชีวิตด้วยธรรมะ (แก้ไขปัญหาชีวิตด้วยปัญญา)<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/389.mp3' type='audio/mp3'></audio></p>
                <p>หน้าที่เป็นสิ่งสำคัญของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/392.mp3' type='audio/mp3'></audio></p>
                <p>พระพุทธองค์ยังทรงมีชีวิตอยู่<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/396.mp3' type='audio/mp3'></audio></p>
                <p>ความถูกต้องเป็นฐานของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/397.mp3' type='audio/mp3'></audio></p>
                <p>หลักการแก้ทุกข์ (หลักธรรมสำหรัแก้ปัญหาชีวิต)<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/404.mp3' type='audio/mp3'></audio></p>
                <p>วางแผนชีวิตให้ถูกต้อง<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/418.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตที่รู้ผิดทางสร้างปัญหา<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/433.mp3' type='audio/mp3'></audio></p>
                <p>รู้ผิด ชีวิตเดือนร้อน<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/444.mp3' type='audio/mp3'></audio></p>
                <p>ใช้เวลาให้มีค่ากับชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/473.mp3' type='audio/mp3'></audio></p>
                <p>ใช้ชีวิตให้มีค่ากับเวลาที่ผ่านไป<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/493.mp3' type='audio/mp3'></audio></p>
                <p>รู้จักคิดชีวิตไม่ทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/500.mp3' type='audio/mp3'></audio></p>
                <p>กิเลสท่วมใจเป็นภัยแก่ชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/panya/mp3/516.mp3' type='audio/mp3'></audio></p>
                <p>ศรัทธาและปัจจัยแห่งชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/036.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตคือการต่อสู้ ศัตรูคือยากำลัง<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/038.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตย่อมหมุนไปตามกรรม<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/094.mp3' type='audio/mp3'></audio></p>
                <p>แก่นแห่งชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/126.mp3' type='audio/mp3'></audio></p>
                <p>แนะนำข้อปฏิบัติในการดำเนินชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/127.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตจะตกต่ำถ้าเอากิเลสเป็นผู้นำ<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/137.mp3' type='audio/mp3'></audio></p>
                <p>ควรพัฒนาชีวิตให้สูงขึ้น<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/227.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตกับที่พึง<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/234.mp3' type='audio/mp3'></audio></p>
                <p>ผู้ไม่ภาวนาย่อมพาชีวิตให้ตกต่ำ<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/243.mp3' type='audio/mp3'></audio></p>
                <p>ศัตรูของชีวิตคือจิตที่ไม่ได้ฝึก<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/258.mp3' type='audio/mp3'></audio></p>
                <p>ภาวนารู้เท่าชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/279.mp3' type='audio/mp3'></audio></p>
                <p>อย่าปล่อยชีวิตให้เสียเปล่า<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/288.mp3' type='audio/mp3'></audio></p>
                <p>ธรรมกับชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/289.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตย่อมหมุนไปตามกรรม<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/308.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตในวัฏฏวน<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/316.mp3' type='audio/mp3'></audio></p>
                <p>ในพุทธศาสนานี้มุ่งสันติสุขให้แก่ชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/319.mp3' type='audio/mp3'></audio></p>
                <p>ความทุกข์ในชีวิตมีมากมาย<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/327.mp3' type='audio/mp3'></audio></p>
                <p>อุบายแก้ปัญหาชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/334.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตมีความทุกข์<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/371.mp3' type='audio/mp3'></audio></p>
                <p>สิ่งจำเป็นต่อชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/376.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตคือการต่อสู้<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/400.mp3' type='audio/mp3'></audio></p>
                <p>อย่าหลงผิดชีวิตจะเป็นหมัน<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/403.mp3' type='audio/mp3'></audio></p>
                <p>เหตุปัจจัยของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/404.mp3' type='audio/mp3'></audio></p>
                <p>เมื่อจิตไม่ดี ชีวิตก็เสียเปล่า<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/414.mp3' type='audio/mp3'></audio></p>
                <p>สละชีวิตเพื่อรักษาศิล<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/432.mp3' type='audio/mp3'></audio></p>
                <p>การฝึกจิตเพื่อชีวิตที่สูงขึ้น<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/433.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตขึ้นอยู่กับการกระทำ<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/448.mp3' type='audio/mp3'></audio></p>
                <p>จิตที่ฝึกดีชีวิตนี้ย่อมไม่มีปัญหา<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/458.mp3' type='audio/mp3'></audio></p>
                <p>ความเป็นมาและภัยของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/459.mp3' type='audio/mp3'></audio></p>
                <p>ผู้มีปัญญาพาชีวิตรอด<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/472.mp3' type='audio/mp3'></audio></p>
                <p>หน้าที่สำคัญของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/499.mp3' type='audio/mp3'></audio></p>
                <p>ผู้มีปัญญาก็สามารถพาชีวิตให้พ้นทุกข์ได้<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/500.mp3' type='audio/mp3'></audio></p>
                <p>กิเลสเป็นศัตรูของชีวิตอันดี<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/516.mp3' type='audio/mp3'></audio></p>
                <p>ปฏิบัติธรรมเพื่อพัฒนาชีวิตให้สูงขึ้น<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/523.mp3' type='audio/mp3'></audio></p>
                <p>เหตุปัจจุบันของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/527.mp3' type='audio/mp3'></audio></p>
                <p>พัฒนาจิตชีวิตจะดีขึ้น<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/544.mp3' type='audio/mp3'></audio></p>
                <p>สร้างฐานของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/613.mp3' type='audio/mp3'></audio></p>
                <p>ปัญหาต่างๆของชีวิตเกิดจากกิเลส<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/617.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตมีน้อยอย่าปล่อยให้สูญเปล่า<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/621.mp3' type='audio/mp3'></audio></p>
                <p>เตื่อนตนสอนจิตชีวิตใกล้ตาย<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/623.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตมีน้อยอย่าปล่อยใจให้ไร้ที่พึ่ง<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/626.mp3' type='audio/mp3'></audio></p>
                <p>ให้เวลาแก้ชีวิตบาง<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/631.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตนี้ไม่นานหนอ<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/649.mp3' type='audio/mp3'></audio></p>
                <p>การปฏิบัติธรรมเป็นสิ่งจำเป็นต่อชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/668.mp3' type='audio/mp3'></audio></p>
                <p>ปัจจัยของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/693.mp3' type='audio/mp3'></audio></p>
                <p>เอาธรรมนำชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/717.mp3' type='audio/mp3'></audio></p>
                <p>พิจารณาทุกข์ของชีวิต<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/718.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตจะตกตํ่าถ้าเอากิเลสนำทาง<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/720.mp3' type='audio/mp3'></audio></p>
                <p>ชีวิตจะพ้นภัยถ้าอาศัยธรรมนำทาง<br/><audio controls=''><source src='http://thammapedia.com/listen/riean/mp3/749.mp3' type='audio/mp3'></audio></p>
 </div>
