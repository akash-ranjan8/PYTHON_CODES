from datetime import *
import time
ldates=[]
d1=date(2018,6,12)
d2=date(2017,6,12)
d3=date(2016,6,12)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()
time.sleep(5)
for d in ldates:
    print(d)