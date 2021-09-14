list_a = [1,2,3,4,5]
list_reversed = reversed(list_a)
print("# reversed() 함수")
print("list(1,2,3,4,5):",list(list_reversed))
print()

print("#reversed()함수와 반복문")
print("for i in reversed([1,2,3,4,5]):")
for i in reversed(list_a):
    print (" - ",i)


example_list = ["요소A","요소B","요소C"]

print("# 단순 출력")
print(example_list)
print()

print("#enumberrate()함수 적용 출력")
print(enumerate(example_list))
print()

print("#list()함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

print("#반복문과 조합하기")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i,value))


example_dic = {
       "key A":"valA",
       "key B":"valB",
       "key C":"valC",
   }

print("#딕셔너리의 item()함수")
print("item():",example_dic.items())
print()

print("#딕셔너리의 items() 함수와 반복문 조합하기")

for key, element in example_dic.items():
    print("dictionary[{}]={}".format(key,element))

array = []

for i in range(0, 20, 2):
    array.append(i*i)
print(array)

array = [i * i for i in range(0,20,2) ]
print(array)

array = ["사과","자두","초콜릿","바나나","체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]

print(output)

number = int (input("정수 입력>"))
if number %2 ==0:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은)짝수 입니다.""".format(number,number))
else:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은)홀수 입니다.""".format(number,number))
print()
if number %2 ==0:
    print("""입력한 문자열은 {}입니다.
{}는(은)짝수 입니다.""".format(number,number))
else:
    print("""입력한 문자열은 {}입니다.
{}는(은)홀수 입니다.""".format(number,number))
if number %2 ==0:
    print("입력한 문자열은 {}입니다. {}는(은)짝수 입니다.".format(number,number))
else:
    print("입력한 문자열은 {}입니다. {}는(은)홀수 입니다.".format(number,number))

test = (
    "이렇게 입력해도"
    "하나의 문자열로 연결되어"
    "생성됩니다."
)

print("test:",test)
print("type(test):",type(test))

number = int(input("정수 입력>"))
if number%2 == 0:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 짝수 입니다."
    ).format(number,number))
else:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 홀수 입니다."
    ).format(number,number))