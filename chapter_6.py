print("start program")
list_a =[1,2,3,4,5,6,7,8,9,10]
list_a[1]


try:
    number_input_a = int(input("정수 입력>"))
    print("원에 반지름", number_input_a)
    print("원에 둘레:",2*3.14*number_input_a)
    print("원의 넓이:", 3.14*number_input_a*number_input_a)
except:
    pass
#    print("정수를 입력하지 않았습니다.")

list_input_b =["23","49","57","스파이"]
print(list_input_b)

list_number = []
for item in list_input_b:

    try:
        float(item)
        list_number.append(item)
        print(item)
    except:
        print("errror")

print("{}내부에 있는 숫자는".format(list_input_b))
print("{}입니다.".format(list_number))

try:
    number_input_a = int(input("정수 입력>"))
except:
    print("예외가 발생햇습니다.")
    print("정수를 입력하지 않았습니다.")
else:
    print("예외가 발생하지 않았습니다.")
    print("원에 반지름", number_input_a)
    print("원에 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
finally:
    print("프로그램이 끝났습니다.")


try:
    file = open("info.txt","w")
    zzzz.zzz()
except Exception as e:
    print(e)
finally:
    file.close()
print("file close check")
print("file.closed:",file.closed)

def test():
    print("1line")
    try:
        print("try 1line")
        return
        print("befor return")
    except:
        print("except")
    else:
        print("else")
    finally:
        print("finally")
    print("rast line")
test()