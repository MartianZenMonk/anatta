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
2* เผยแพร่คลิปให้อาสาสมัครที่สนใจฟังแล้ว สรุปว่า เหมาะกับคนที่มีทุกข์เรื่องอะไร มีปัญหาอะไร นิสัยแบบไหน หรือ สรุปเนื้อหาเป็น passages และโดยอาจมีแนะนำ ว่า ฟังที่นาทีเท่าไหร่ แล้วกระโดดไปนาทีไหน ทั้งนี้เพราะบางคลิปอาจจะมีน้ำมาก ถ้าทำระบบเล่นได้ตามเวลา ก็ไม่ต้องตัดต่อคลิป แต่แน่นอนว่าเก็บคลิปค้นฉบับไว้ด้วย <br/>
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
https://www.facebook.com/หลวงพ่อสุญญตา-182790273237003/

<div>
 <h4> ธรรมเทศนาว่าด้วย - ปัญญา </h4>
                <!-- Display the countdown timer in an element -->
                <p>พรรษากาลเทศนา กัณฑ์ 0๒ -:ไตรสิกขา : ศีลสิกขา-สมาธิสิกขา-ปัญญา... - bdds<br/><audio controls=''><source src='thammapedia.com/listen/bdds/mp3/3023.mp3' type='audio/mp3'></audio></p>
                <p>พรรษากาลเทศนา กัณฑ์ ๑๑ -:ไตรมาส : ศีลมาส-สมาธิมาส-ปัญญามาส - bdds<br/><audio controls=''><source src='thammapedia.com/listen/bdds/mp3/4002.mp3' type='audio/mp3'></audio></p>
                <p>ศิลปะแห่งการดูด้วย ยถาภูตสัมมัปปัญญา - bdds<br/><audio controls=''><source src='thammapedia.com/listen/bdds/mp3/8027.mp3' type='audio/mp3'></audio></p>
                <p>การมีธรรมมะสี่เกลอ : สติ ปัญญา สัมปชัญญะ สมาธิ - bdds<br/><audio controls=''><source src='thammapedia.com/listen/bdds/mp3/10009.mp3' type='audio/mp3'></audio></p>
                <p>คนไทยต้องเข้มแข็งด้วยปัญญา จงลุกขึ้นมาก้าวหน้าไป (๖๐.๕๖) - bdds<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/02_03.mp3' type='audio/mp3'></audio></p>
                <p>รักงาน คือรักแค่ไหน มีปัญญา คือรู้เท่าใด(38.54) - bdds<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/03_02.mp3' type='audio/mp3'></audio></p>
                <p>ฟังคำทำนาย ทำไมจึงมัวตื่นตูม แล้วภูมิปัญญา จะมีมาจากที่ไหน (119.54).mp3 - bdds<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/04_14.mp3' type='audio/mp3'></audio></p>
                <p>๐๓๐๑-ความสัมพันธ์ระหว่างจิตภาวนากับปัญญาภาวนา ๘๔.๕๘ - bdds<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/05_03.mp3' type='audio/mp3'></audio></p>
                <p>๐๘๐๑-จากจิตภาวนาสู่ปัญญาภาวนาตามวิธีสติปัฏฐาน ๔๙.๑๕ - bdds<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/05_21.mp3' type='audio/mp3'></audio></p>
                <p>การศึกษาเริ่มที่ตาหู จะดูฟังได้แค่ตัณหา หรือไปถึงปัญญา นี่คือตัวตัดสิน - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/09_18.mp3' type='audio/mp3'></audio></p>
                <p>โยมขอศีล พระให้สิกขาบท ขอสมาธิ ให้กรรมฐาน ขอปัญญา ให้คำสอนหรือข้อพิจารณา - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/09_28.mp3' type='audio/mp3'></audio></p>
                <p>แม้จะมีเพียงวินัยโดยธรรมชาติอย่างฝูงนกและกลีบดอกไม้ ก็ยังดีกว่าคนไร้ปัญญา ไม่รู้จักวินัย - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/09_29.mp3' type='audio/mp3'></audio></p>
                <p>อยากเป็นคนมีปัญญาดี ถ้าสติไม่มี ก็หมดทางเจริญปัญญา - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/09_35.mp3' type='audio/mp3'></audio></p>
                <p>ปัญญาเป็นแดนยิ่งใหญ่ ต้องพัฒนากันไป จนกลายเป็นโพธิญาณ - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/09_36.mp3' type='audio/mp3'></audio></p>
                <p>ในยุคข่าวสารต้องมีปัญญาแตกฉาน ทั้งภาครับและภาคแสดง - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/09_37.mp3' type='audio/mp3'></audio></p>
                <p>รักษาศีล ๘ อย่าพูดแค่ว่าได้บุญ ต้องรู้ว่าศีล ๘ มาหนุนให้ก้าวไปสู่การพัฒนาจิตใจและปัญญาอย่างไร - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/09_52.mp3' type='audio/mp3'></audio></p>
                <p>ถ้าไปถึงปัญญา ก็ไม่มัวหลงหาจริยธรรมสากล - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/10_01.mp3' type='audio/mp3'></audio></p>
                <p>รักงานคือรักแค่ไหน มีปัญญาคือรู้เท่าใด(๓๗.๕๙) - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/11_02.mp3' type='audio/mp3'></audio></p>
                <p>จะสมานฉันท์ ต้องสมานปัญญา (๒๙.๑๔) - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/11_05.mp3' type='audio/mp3'></audio></p>
                <p>ปรุงแต่งดี ก็ดี มีปัญญาถึง จึงไม่ปรุงแต่งได้ (๔๕.๕๙ - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/11_15.mp3' type='audio/mp3'></audio></p>
                <p>ถ้าไปถึงปัญญา ก็ไม่มัวหลงหาจริยธรรมสากล [53.33] - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/16_04.mp3' type='audio/mp3'></audio></p>
                <p>คนไทยต้องเข้มแข็งด้วยปัญญา จงลุกขึ้นมาก้าวหน้าไป (๖๐.๕๖) - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/16_14.mp3' type='audio/mp3'></audio></p>
                <p>โรงเรียนต้องช่วยสังคมไทย อนุรักษ์ความเจริญทางจิตใจและก้าวไปในปัญญา 0 - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/14_04.mp3' type='audio/mp3'></audio></p>
                <p>18 จะสมานฉันท์ ต้องสมานปัญญา (30.09) - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/18_18.mp3' type='audio/mp3'></audio></p>
                <p>โรงเรียนต้องช่วยสังคมไทยอนุรักษ์ความเจริญทางจิตใจ และก้าวไปในปัญญา (๔๖.๐๕) - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/12_04.mp3' type='audio/mp3'></audio></p>
                <p>รักงานคือรักแค่ไหน มีปัญญาคือรู้เท่าใด - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/20_07.mp3' type='audio/mp3'></audio></p>
                <p>ปรุงแต่งดี ก็ดี มีปัญญาถึง จึงไม่ปรุงแต่งได้ - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/20_15.mp3' type='audio/mp3'></audio></p>
                <p>วิสาขบูชา เตือนชาวพุทธก้าวให้ถึงปัญญา (50.44) - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/22_07.mp3' type='audio/mp3'></audio></p>
                <p>คนไทยไม่ใจแคบ แต่ระวังไว้อย่าให้ปัญญาแคบ (1.01.55) - payutto<br/><audio controls=''><source src='thammapedia.com/listen/payutto/mp3/22_10.mp3' type='audio/mp3'></audio></p>
                <p>มองด้วยตาปัญญา<br/><audio controls=''><source src='thammapedia.com/listen/char/mp3/th_009.mp3' type='audio/mp3'></audio></p>
                <p>หลุดพ้นด้วยปัญญา อบรมภิกษุสามเณร<br/><audio controls=''><source src='thammapedia.com/listen/char/mp3/th_015.mp3' type='audio/mp3'></audio></p>
                <p>มีศีลมีปัญญา<br/><audio controls=''><source src='thammapedia.com/listen/char/mp3/th_035.mp3' type='audio/mp3'></audio></p>
                <p>ศรัทธากับปัญญา<br/><audio controls=''><source src='thammapedia.com/listen/char/mp3/th_044.mp3' type='audio/mp3'></audio></p>
                <p>ปัญญาในวิมุตติ<br/><audio controls=''><source src='thammapedia.com/listen/char/mp3/th_088.mp3' type='audio/mp3'></audio></p>
                <p>ทัศนาจรทางปัญญา<br/><audio controls=''><source src='thammapedia.com/listen/char/mp3/th_051a.mp3' type='audio/mp3'></audio></p>
                <p>ปัญญามีมาเพราะใจสงบ - char<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/061.mp3' type='audio/mp3'></audio></p>
                <p>ดับไฟภายในด้วยสติปัญญา - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/108.mp3' type='audio/mp3'></audio></p>
                <p>ฆ่าความชั่วด้วยตัวปัญญา - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/125.mp3' type='audio/mp3'></audio></p>
                <p>อยู่ด้วยปัญญา ปัญหาไม่มี - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/156.mp3' type='audio/mp3'></audio></p>
                <p>การเข้าถึงธรรมด้วยปัญญา - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/185.mp3' type='audio/mp3'></audio></p>
                <p>ใช้ปัญญาแก้ปัญหาของเรา - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/196.mp3' type='audio/mp3'></audio></p>
                <p>สติและปัญญาต้องใช้ทุกกรณี - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/275.mp3' type='audio/mp3'></audio></p>
                <p>เปิดใจกว้าง ทางเพิ่มปัญญา - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/279.mp3' type='audio/mp3'></audio></p>
                <p>ใช้ปัญญาค้นหาธรรมแท้ - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/294.mp3' type='audio/mp3'></audio></p>
                <p>ใช้ปัญญาพิจารณาเพื่อปล่อยวาง - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/309.mp3' type='audio/mp3'></audio></p>
                <p>ชาวพุทธต้องเป็นอยู่ด้วยปัญญา - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/350.mp3' type='audio/mp3'></audio></p>
                <p>ใช้ปัญญาแก้ปัญหาสังคม - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/377.mp3' type='audio/mp3'></audio></p>
                <p>ใช้ปัญญาพิจารณาคิดค้น - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/380.mp3' type='audio/mp3'></audio></p>
                <p>แก้ปัญหาชีวิตด้วยธรรมะ (แก้ไขปัญหาชีวิตด้วยปัญญา) - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/389.mp3' type='audio/mp3'></audio></p>
                <p>ใช้ปัญญาพาตนให้พ้นทุกข์ - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/394.mp3' type='audio/mp3'></audio></p>
                <p>มีสติปัญญาพาให้สุข - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/413.mp3' type='audio/mp3'></audio></p>
                <p>วิธีรักษาสุขภาพจิต (สุขภาพดีเพราะปัญญาดี) - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/414.mp3' type='audio/mp3'></audio></p>
                <p>ความเชื่อต้องเจือด้วยปัญญา (รู้รักสามัคคี เพื่อความอยู่ดีของคนในชาติ) - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/432.mp3' type='audio/mp3'></audio></p>
                <p>ศรัทธาต้องคู่กับปัญญา - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/452.mp3' type='audio/mp3'></audio></p>
                <p>ชาวพุทธต้องอยู่ด้วยปัญญา - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/453.mp3' type='audio/mp3'></audio></p>
                <p>ตัวปฏิบัติคือ ศีล สมาธิ ปัญญา - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/471.mp3' type='audio/mp3'></audio></p>
                <p>ใช้สติปัญญาดับไฟข้างใน - panya<br/><audio controls=''><source src='thammapedia.com/listen/panya/mp3/494.mp3' type='audio/mp3'></audio></p>
                <p>ปัญญาสอนจิต - panya<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/028.mp3' type='audio/mp3'></audio></p>
                <p>จิตที่สงบย่อมเกิดปัญญา - panya<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/048.mp3' type='audio/mp3'></audio></p>
                <p>อบรบ ศีล สมาธิ ปัญญา - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/112.mp3' type='audio/mp3'></audio></p>
                <p>สะสมบุญด้วยศีล สมาธิ ปัญญา - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/145.mp3' type='audio/mp3'></audio></p>
                <p>ปัญญาเป็นอริยสัจธรรม - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/155.mp3' type='audio/mp3'></audio></p>
                <p>ผู้มีปัญญาย่อมแสวงหาแต่ทางที่ชอบ - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/207.mp3' type='audio/mp3'></audio></p>
                <p>สติและปัญญาตามรักษาจิต - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/215.mp3' type='audio/mp3'></audio></p>
                <p>อุบายเจริญวิปัสสนาปัญญา - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/255.mp3' type='audio/mp3'></audio></p>
                <p>จิตจะดีได้ต้องอาศัยปัญญาอบรม - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/302.mp3' type='audio/mp3'></audio></p>
                <p>อบรบจิตเจริญปัญญา - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/352.mp3' type='audio/mp3'></audio></p>
                <p>ขี้ไถทองคำ ศิล สมาธิ ปัญญา - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/424.mp3' type='audio/mp3'></audio></p>
                <p>เจริญปัญญาอบรมจิต - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/461.mp3' type='audio/mp3'></audio></p>
                <p>ผู้มีปัญญาพาชีวิตรอด - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/472.mp3' type='audio/mp3'></audio></p>
                <p>ผู้มีปัญญาก็สามารถพาชีวิตให้พ้นทุกข์ได้ - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/500.mp3' type='audio/mp3'></audio></p>
                <p>ผู้มีปัญญามุ่งละกิเลส - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/524.mp3' type='audio/mp3'></audio></p>
                <p>การตายเป็นบ่อเกิดแห่งปัญญา - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/536.mp3' type='audio/mp3'></audio></p>
                <p>ทางดำเนินของผู้มีปัญญา - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/565.mp3' type='audio/mp3'></audio></p>
                <p>วัฏฏะวนคนมีปัญญาย่อมไม่หลง - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/582.mp3' type='audio/mp3'></audio></p>
                <p>การใช้ปัญญาในทางพระพุทธศาสนา - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/597.mp3' type='audio/mp3'></audio></p>
                <p>ผู้มีปัญญาย่อมแสวงบุญ - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/754.mp3' type='audio/mp3'></audio></p>
                <p>ชาวพุทธควรมีปัญญา - riean<br/><audio controls=''><source src='thammapedia.com/listen/riean/mp3/755.mp3' type='audio/mp3'></audio></p>
                </div>
