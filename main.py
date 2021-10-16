import test_module as test
#import test_package.module_a as a
#import test_package.module_b as b
from test_package import *

print(module_a.variable_a)
print(module_b.variable_b)

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))
print("#메인의 --name__ 출력하기")
print(__name__)
print()