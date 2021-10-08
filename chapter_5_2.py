from typing import Counter


def factorial(n):
    output = 1
    for i in range(1,n+1):
        output *=i
    return output

print("1!:",factorial(1))
print("2!:",factorial(2))
print("3!:",factorial(3))
print("4!:",factorial(4))
print("5!:",factorial(5))
print()
def factorial_v2(n):
    if n  == 0:
        return 1
    else:
        return n * factorial(n-1)

print("1!:",factorial(1))
print("2!:",factorial(2))
print("3!:",factorial(3))
print("4!:",factorial(4))
print("5!:",factorial(5))
print()

def fibonacci(n):
    if n ==1:
        return 1
    if n ==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print("fibonacci(1):",fibonacci(1))
print("fibonacci(2):",fibonacci(2))
print("fibonacci(3):",fibonacci(3))
print("fibonacci(4):",fibonacci(4))
print("fibonacci(5):",fibonacci(5))

counter = 0

def fibonacci2(n):
    print("fibo({})를 구합니다.".format(n))
    global counter
    counter +=1
    if n ==1:
        return 1
    if n ==2:
        return 1
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)
    
fibonacci2(20)
print("--")
print("fibo(20)계산에 활용된 덧셈 횟수는 {}번 입니다.".format(counter))
print()

dictionary={
    1:1,
    2:2,
}

def fibonacci3(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci3(n-1) + fibonacci3(n-2)
        dictionary[n] = output
        return output
print("fibonacci(10):",fibonacci3(10))
print("fibonacci(20):",fibonacci3(20))
print("fibonacci(30):",fibonacci3(30))
print("fibonacci(40):",fibonacci3(40))
print("fibonacci(50):",fibonacci3(50))
print("fibonacci(1000):",fibonacci3(1000))
