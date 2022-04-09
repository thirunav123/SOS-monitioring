import time
import datetime
def get_shift(ct):
    startA=datetime.time(6,0,00)
    startB=datetime.time(14,30,00)
    startC=datetime.time(22,30,00)
    if startA<ct<startB:
        return 'A'
    if startB<ct<startC:
        return 'B'
    else:
        return 'C'
date=datetime.datetime.now()
a=date.strftime("%I.%M.%S_%p")
print(a)
# print(type(str(date.date())))
print(date.hour)
print(date.minute)
print(date.second)
print(get_shift(datetime.time(date.hour,date.minute,date.second)))