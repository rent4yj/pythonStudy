dic={
    "name" : "7d 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin" : "필리핀"
    }

print("name:",dic["name"])
print("type:",dic["type"])
print("ingredient:",dic["ingredient"])
print("origin:",dic["origin"])

dic["name"] = "8d 건조 망고"
print("name:",dic["name"])

print("ingredient:",dic["ingredient"][1])

dic["price"] = 5000
print("price : ",dic["price"])

print(dic)
del dic["ingredient"]
print(dic)

dic2={
    "test" : "test"
}
print("요소추가 이전:",dic2)
dic2["name"]="새로운 이름"
dic2["head"]="새로운 정신"
dic2["body"]="새로운 몸"
print("요소 추가 이후:",dic2)

print("요소제거 이전 :",dic)
del dic["name"]
del dic["type"]
print("요소제거 이후 : ",dic)

key = input(">접근하고자 하는 키 :")
print(key)

print(dic2[key])
if key in dic2:
    print(dic2[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")



value = dic2.get(key)
print("값:",value)
if value == None:
    print("존재하지 않는 키에 접근 했었습니다. ")
for key in dic2:
    print(key,":",dic2[key])
