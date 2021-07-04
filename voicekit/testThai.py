import os
import sys
import datetime

today = datetime.datetime.now() 
text = "../thaivoices/words/today.mp3 ../thaivoices/words/day.mp3 ../words/thaivoices/weekday/"+today.strftime('%w')+".mp3"
text += " ../thaivoices/words/at.mp3 ../thaivoices/59/"+today.strftime('%d')+".mp3"+" ../thaivoices/month/0.mp3 ../thaivoices/month/"+today.strftime('%m')+".mp3"
text += " ../thaivoices/words/time.mp3 ../thaivoices/59/"+today.strftime('%H')+".mp3"+" ../thaivoices/words/hour.mp3"
text += " ../thaivoices/59/"+today.strftime('%M')+".mp3"+" ../thaivoices/words/minute.mp3"


text += " ../thaivoices/words/buddhaday.mp3 ../thaivoices/words/next.mp3 ../thaivoices/words/is.mp3 ../thaivoices/words/day.mp3"
text += " ../thaivoices/weekday/"+today.strftime('%w')+".mp3 ../thaivoices/words/at.mp3 ../thaivoices/59/"+today.strftime('%d')+".mp3"
text += " ../thaivoices/month/0.mp3 ../thaivoices/month/"+today.strftime('%m')+".mp3"


print(text)
os.system("mpg123 "+text)
                                        