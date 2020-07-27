import time,datetime
epochseconds=time.time()
print(epochseconds)
t=time.ctime(epochseconds)
print(t)
dt=datetime.datetime.today()
print('current date : {}/{}/{}'.format(dt.day,dt.month,dt.year))
print('current time : {}:{}:{}'.format(dt.hour,dt.minute,dt.second))