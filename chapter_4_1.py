list_a =[1,2,3,4]
list_b =[5,6,7,8]
print(list_a[3:4])
print(list_a)
print(list_a+list_b)

list_a.append(5)
print("append 5 넣으면",list_a)
list_a.insert(0,10)
print("insert(0,10) 넣으면",list_a)

list_a.extend([0,9,8,7,6])
print("extend(0,9,8,7,6,) 넣으면",list_a)

list_a.extend(list_b)
print("extend(list_b) 넣으면",list_a)
del list_a[3:6]
print("del list_a[3:6] 넣으면",list_a)
list_a.pop(7)
print(".pop(7) 넣으면",list_a)
list_a.remove(7)
print("remove(7) 넣으면",list_a)
list_a.clear()
print("clear를 넣으면",list_a)

if 0 in list_a:
    print("0이 있습니다.")
else:
    print("0이 없습니다.")

array = [273,32,103,57,52]

for element in array:
    print(element)