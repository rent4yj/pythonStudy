import math as m
import random
import random as r
import sys
import os
import datetime
import time
from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
soup = BeautifulSoup(target,"html.parser")
for location in soup.select("location"):
    print("도시",location.select_one("city").string)
    print("날씨", location.select_one("wf").string)
    print("최저기온", location.select_one("tmn").string)
    print("최고기온", location.select_one("tmx").string)
    print()

output = target.read()

print(output)

print("wait 5second")
time.sleep(5)
print("program quit")

print("time is now")
now = datetime.datetime.now()
print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")
print()

print("format times")
output_a = now.strftime("%y.%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
                                            now.month,\
                                            now.day,\
                                            now.hour,\
                                            now.minute,\
                                            now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
print(output_a)
print(output_b)
print(output_c)
print()

print("os:",os.name)
print("현재폴더:",os.getcwd())
print("현재 폴더 내부요소:",os.listdir())

os.mkdir("hello")
os.rmdir("hello")

with open("original.txt","w")as file:
    file.write("hello")
os.rename("original.txt","new.txt")

os.remove("new.txt")
os.system("dir")

m.sin(1)

print("random module")

print("-random():",r.random())

print("-uniform(10,20):",r.uniform(10,20))

print("-random():",r.random())

print(sys.argv)
print("--------")
print("getwindowsversion:()",sys.getwindowsversion())
print("--------")
print("copyright:",sys.copyright)
print("--------")
print("version:",sys.version)
sys.exit()

