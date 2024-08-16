from datetime import datetime,time,timedelta
from playsound import playsound
import time as t

alarme = time(17,11)
now = datetime.now()

a=datetime.combine(now.date(),alarme)
time_until_alarm = a - now

if time_until_alarm.total_seconds()<0:
    a +=timedelta(days=1)
    time_until_alarm=a-now

if time_until_alarm.total_seconds()>10:
    t.sleep(time_until_alarm.total_seconds() - 10)

while True:
    current_time = datetime.now().time()
    #print(current_time.second)
    if current_time.hour == alarme.hour and current_time.minute == alarme.minute:
        playsound(r'C:\Users\User\Desktop\unice\info\M1\entrainement\python\alarme\tropical-alarm-clock-168821.mp3')
        break
    t.sleep(1)