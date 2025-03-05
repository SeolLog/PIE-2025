# 난수: 무작위 숫자를 출력
from random import *

# 0.0~1.0미만의 임의의 값 생성
print(random())

print(random() * 10) #0.0~10.0미만의 임의의 값 생성
print(int(random() * 10)) # 0~10미만의 임의의 값 생성
print(int(random()) * 10 + 1) #1~10이하의 임의의 값 생성

print(int(random())+1) # 1~45이하의 임의의 값 생성 

print(randrange(1,46)) #1~46미만의 임의의 값 생성 

print(randint(1,45)) #1~45이하의 임의의 값 생성 


