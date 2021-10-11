try:
    number_input_a = int(input("정수입력>"))
    print("원의 반지름:",number_input_a)
    print("원의 둘레:",2*3.14*number_input_a)
    print("원의 넓이:",3.14*number_input_a*number_input_a)
except Exception as exception:
    print("type(exception):",type(exception))
    print("exception:",exception)

list_number = [52,324,534,23,100]
try:
    number_input_a = int(input("정수입력>"))
    print("{}번째 요소:{}".format(number_input_a,list_number[number_input_a]))
except Exception as exception:
    print("type(exception):",type(exception))
    print("exception:",exception)

try:
    number_input_a = int(input("정수입력>"))
    print("{}번째 요소:{}".format(number_input_a,list_number[number_input_a]))
except ValueError as exception:
    print("정수를 입력하세요")
    print("exception:",exception)

except IndexError as exception:
    print("인덱스를 벗어 났어요")
    print("exception:",exception)

list_number = [52,273,32,72,100]

try:
    number_input = int(input("정수 입력>"))
    print("{}번째 요소:{}".format(number_input,list_number[number_input]))
    raise NotImplementedError
except ValueError as exception:
    print("정수를 입력해 주세요!")
    print(type(exception),exception)
except IndexError as exception:
    print("리스트 인덱스를 벗어 났어요?")
    print(type(exception),exception)
except Exception as exception:
    print("미리 파악하지 못한 예외가 발생")
    print(type(exception),exception)

