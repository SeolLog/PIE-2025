# a = 5 #int(정수)
# b = '5' #str    
# c = 5.0 #float(실수)

# print(a+a) #int + int
# print()
# print(b+b) #str + str
# print(a*b) #int + str

'''
가능
문자 * 문자
정수 * 정수 

불가능
문자 + 숫자
숫자 * 문자
'''

''''
# 군집 자료형: 여러데이터를 모은 집합 형태 자료형
1) 리스트(list): 데이터를 순차적으로 저장(열거형)
2) 튜플(tuple): 값을 변경할 수 없는 열거형  집합
3) 세트(set): 순서가 없고 중복이 허용되지 않는 집합
4) 사전(dictionary): 키와 값의 쌍으로 구성된 집합 

자료형 변환
- 파이썬은 사용자가 자료형을 결정하지 않기 때문에 편리하기도 하지만 데이터가 사용자의 의도와 다른 자료형이 될 수도 있다.
이때는 각 데이터들의 자료형을 원하는 것으로 변경해야 한다.
ex) input()사용, 정수와 실수의 사용 등

- 자료형 변환(typecasting)방법: 원하는 자료형 함수에 값을 넣는다.
ex) str(10), int('10'), int(1.5), list('hello') etc
'''

# input()으로 숫자 입력받기

# a=int(input("write a number")) # a에 값을 넣었을 때 str로 출력됨, 따라서 숫자를 출력하려면 int변환 필요

# print(a+a)

# float <-> int
num = 5.0
range(int(num))
#range() 함수안에는 int가 들어감, float X

a=input('숫자하나입력')
b=int(a)
c=float(a)

print(type(a))
print(type(b))
print(type(c))