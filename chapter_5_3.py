[a,b] = [10,20]
(c,d) = (10,20)

print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)

tuple_test = 10,20,30,40
print("#괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test:",tuple_test)
print("type(tuple_test):",type(tuple_test))
print()

a,b,c = 10,20,30
print("#괄호가 없는 튜플을 활용한 할당")
print("a:",a)
print("b:",b)
print("c:",c)

print("#교환 전 값")
print("a:",a)
print("b:",b)
print()

a,b = b,a 

print("# 교환 후 값")
print("a:",a)
print("b:",b)
print()

def test():
    return (10,20)


a,b = test()
print("a:",a)
print("b:",b)
print()

def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("안녕하세요")

call_10_times(print_hello)


def power(item):
    return item * item
def under_3(item):
    return item < 3

list_input_a = [1,2,3,4,5]

output_a = map(power, list_input_a)
print("map() 함수의 실행결과")
print("map(power, list_input_a):",output_a)
print("map(power,list_input_a):",list(output_a))
print()

output_b = filter(under_3,list_input_a)
print("#filter() 함수의 실행결과")
print("filter(under_3, list_input_a):",output_b)
print("filter(under_3,list_input_a):",list(output_b))
print()

powerlam = lambda x: x*x
under_3lam = lambda x: x<3

list_input_a= [1,2,3,4,5]

output_a = map(powerlam, list_input_a)
print("map() 함수의 실행결과")
print("map(power, list_input_a):",output_a)
print("map(power,list_input_a):",list(output_a))
print()

output_b = filter(under_3lam,list_input_a)
print("#filter() 함수의 실행결과")
print("filter(under_3, list_input_a):",output_b)
print("filter(under_3,list_input_a):",list(output_b))
print()


list_input_a= [1,2,3,4,5]

output_a = map(lambda x:x*x, list_input_a)
print("map() 함수의 실행결과")
print("map(power, list_input_a):",output_a)
print("map(power,list_input_a):",list(output_a))
print()

output_b = filter(lambda x:x<3,list_input_a)
print("#filter() 함수의 실행결과")
print("filter(under_3, list_input_a):",output_b)
print("filter(under_3,list_input_a):",list(output_b))
print()

file = open("basic.txt","w")
file.write("hello python programming...!")
file.close()

with open("basic_with.txt","w") as file:
    file.write("hello python programming...!")


import random

hanguls = list ("가나다라마바사아자차카타파하고노도로모보소오조초코토포호거너더러머버서어저처커터퍼허")
with open("info.txt","w") as file:
    for i in range(1000):
        name = random.choice(hanguls) +random.choice(hanguls)+random.choice((hanguls))
        weight = random.randrange(40,200)
        height = random.randrange(150,240)
        file.write("{},{},{}\n".format(name,weight,height))

with open("info.txt","r") as file:
    for line in file:
        (name,weight,height) = line.strip().split(",")
        if(not name)or(not weight)or (not height):
            continue
        bmi = int(weight)/((int(height)/100)**2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상체중"
        else:
            result = "저체중"

        print('\n'.join([
            "이름 : {}",
            "몸무게:{}",
            "키:{}",
            "BMI:{}",
            "결과:{}"
        ]).format(name,weight,height,bmi,result))
        print()

def test1():
    print("function call")
    yield "test"

print("a pass")
test1()
print("b pass")
test1()

print(test())

def test2():
    print("a pass")
    yield 1
    print("b pass")
    yield 2
    print("c pass")

output = test2()
print("d pass")
a = next(output)
print(a)
print("e pass")
b = next(output)
print(b)
print("f pass")
#c = next(output)
#print(c)

#next(output)

numbers = [1,2,3,4,5,6]

print("::".join(map(str,numbers)))

numbers = list(range(1,10+1))

print ("홀수")
print(list(filter(lambda x:x%2==1,numbers)))

print ("3이상 7미만")
print(list(filter(lambda x: 3 <= x <7,numbers)))

print("제곱해서 50미만")
print(list(filter(lambda x: x** 2 < 50,numbers )))