string_a = "{}".format(10)

print(string_a)
print(type(string_a))

string_a = "{} 만원".format(5000)
string_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
string_c = "{}{}{}".format(3000 , 4000 , 5000 )
string_d = "{}{}{}".format(1,"문자열",True)


print(string_a)
print(string_b)
print(string_c)
print(string_d)

string_a = "{}{}{}".format(5000,1,2,3,4)
#string_b = "{}{}{}".format(5000)

print(string_a)
print(string_b)


output_a = "{:d}".format(52)
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)
print("기본")
print(output_a)
print("특정칸에 출력")
print(output_b)
print(output_c)
print("빈칸에 0 체우기")
print(output_d)
print(output_e)

output_a = "{:+d}".format(52)
output_b = "{:+d}".format(-52)
output_c = "{:d}".format(52)
output_d = "{:d}".format(-52)
print("기호와 함께 출력하기")
print(output_a)
print(output_b)
print(output_c)
print(output_d)

output_a = "{:+5d}".format(52)
output_b = "{:+5d}".format(-52)
output_c = "{:=+5d}".format(52)
output_d = "{:=+5d}".format(-52)
output_e = "{:+05d}".format(52)
output_f = "{:+05d}".format(-52)

print("조합")
print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)
print(output_f)

output_a = "{:f}".format(52.275)
output_b = "{:15f}".format(52.275)
output_c = "{:+15f}".format(52.275)
output_d = "{:+015f}".format(52.275)
print("부동소숫점 출력")
print(output_a)
print(output_b)
print(output_c)
print(output_d)

output_a = "{:15.3f}".format(52.275)
output_b = "{:15.2f}".format(52.275)
output_c = "{:15.1f}".format(52.275)
print("부동소숫점 출력")
print(output_a)
print(output_b)
print(output_c)

output_a = 52.0
output_b = "{:g}".format(output_a)
print("의미없는 소숫점 지우기")
print(output_a)
print(output_b)

print("대소문자 변환")

a = "Hello Python Programming...!"
b = a.upper()
print(b)
b = a.lower()
print(b)

a = """
    안녕하세요    
문자열의 함수를 알아봅니다.
"""
print(a)
print(a.strip())
print(a.lstrip())
print(a.rsplit())

a = "train10"
b = "asdfsa"
c = "sadfas"
d = "234234"
e = "234234"
f = "  "
g = "sdadfas"
h = "LSAJLFJ"

print(a.isalnum())
print(b.isalpha())
print(c.isidentifier())
print(d.isdecimal())
print(e.isdigit())
print(f.isspace())
print(g.islower())
print(h.isupper())

output_a = "안녕안녕하세요"
print(output_a.find("안녕"))
print(output_a.rfind("안녕"))
print("안녕" in output_a)
print("잘자" in output_a)

output_a = "10 20 30 40 50"
print(output_a.split(" "))

