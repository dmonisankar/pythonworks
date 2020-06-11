
import datetime

t = datetime.time(1,15,30)

print (t)

print ('hour :', t.hour)
print ('minute :', t.minute)
print ('second:', t.second)
print ('microsecond :', t.microsecond)
print ('tzinfo ;' ,t.tzinfo)


today = datetime.date.today()
print ( 'Today :', today)

one_day = datetime.timedelta(days=1)
print ('One day :', one_day)

yesterday = today- one_day
print ( 'yesterday:', yesterday)

tomorrow = today + one_day
print ( 'tomorrow:', tomorrow)

print ('tomorrow -yesterday :',tomorrow -yesterday)
print ('yesterday - tomorrow:',yesterday - tomorrow)