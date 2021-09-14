for i in range(5):
    print(str(i)+"=반복 변수")
print()
for i in range(5,10):
    print(str(i)+"=반복 변수")
print()
for i in range(0,10,3):
    print(str(i)+"=반복 변수")
print()

array = [273,32,103,57,52]

for i in range(len(array)):
    print("{}번째 반복:{}".format(i,array[i]))
print()
for i in range(4,0-1,-1):
    print("{}번째 반복:{}".format(i,array[i]))
print()
for i in reversed(range(len(array))):
    print("{}번째 반복:{}".format(i,array[i]))
print()
'''
while True:
    print(".",end="")
'''
i = 0
while i<10:
    print("{}번째 반복입니다.".format(i))
    i+=1

list_test = [1,2,1,2]
value = 2

while value in list_test:
    list_test.remove(value)

print(list_test)

import time
number = 0

target_tick = time.time()+5
while time.time()<target_tick:
    number+=1
print("5초동안 {}번 반복했습니다.".format(number))


i =0

while True:
    print("{}번째 반복문입니다.".format(i))
    i+=1
    intput_text = input(">종료하시겠습니까?(y) : ".format(i))
    if intput_text in ["y","Y"]:
        print("반복을 종료합니다.")
        break


numbers = [5,15,6,20,7,25]

for number in numbers:
    if number <10:
        continue
    print(number)