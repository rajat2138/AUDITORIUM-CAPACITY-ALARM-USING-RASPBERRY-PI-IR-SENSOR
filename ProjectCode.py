#Public View Link :   https://thingspeak.com/channels/908978


import RPi.GPIO as g
import time
import urllib.request
import requests

g.setmode(g.BCM)
sensor1=17
sensor2=27
g.setup(sensor1,g.IN)
g.setup(sensor2,g.IN)

url='https://api.thingspeak.com/update?api_key='
key='O4C891AWW0FD9Y4U'

count=0 #Count Of Person

while True :
    s1=g.input(17)
    s2=g.input(27)
    if s1==1 and s2 == 1:
        time.sleep(0.5)
        continue

    if(s1==1):
        time.sleep(0.75)
        s1=g.input(17)
        s2=g.input(27)
        if  s2 == 1:
            count+=1
            print('A person entered')
            print('Count is ', count,'\n')
            header='&field1={}'.format(count)
            new_url= url + key + header
            v= urllib.request.urlopen(new_url)
            time.sleep(1.5)

    elif  s2 == 1:
        time.sleep(0.75)
        s1=g.input(17)
        s2=g.input(27)
        if s1==1:
            if count>0:
                count-=1
                print('A person left')
                print('Count is ', count,'\n')
                header='&field1={}'.format(count)
                new_url= url + key + header
                v= urllib.request.urlopen(new_url)
                time.sleep(1.5)
