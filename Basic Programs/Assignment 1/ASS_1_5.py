import os 
time = float (input("Enter the Seconds:"))  
day = time//(24*3600) 
time = time%(24*3600) 
hour = time // 3600 
time %=3600 
minute = time // 60
time %= 60 
second = time 
print("Day:Hours:Minute:Second ->%d:%d:%d:%d"%(day,hour,minute,second))