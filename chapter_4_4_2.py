

number = int(input("정수입력>"))

if number %2 ==0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 짝수 입니다."
    ]).format(number,number))
else:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 홀수 입니다."
    ]).format(number,number))

number=[1,2,3,4,5,6]
r_num = reversed(number)

print("reversed numbers :",r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))