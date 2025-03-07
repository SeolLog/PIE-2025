print("안녕하세요") 

# 한문장을 주석 처리하고 싶을 때 문장 맨 앞에 #을 붙여줌
'''여러줄 주석을 처리할때
    앞뒤 문장에 ''' '''으로 주석 처리
'''

''' 
변수: 데이터를 담아주는 역할 
변수를 만들어주려면 변수명과 값이 필요
지정되지 않은 변수명을 입력하면 에러 발생
'''

a = 10
b = 5
print(a) # 변수 a를 출력
print('a') # 따옴표를 감싸면 문자

print(b)
print(a+b)

b = 7
print(a+b)

'''
첫글자로는 영어, _(언더바)만 가능
구성: 영어, _ , 숫자
대소문자를 구분해서 사용하므로 A, a는 전혀다름

# 내장 함수 사용법
함수이름(인자 값, 인자 값, 인자 값) -> 리턴 값
'''
print("hey")
# 인자 값: hey, 리턴 값: 없음
# print: 출력

#input 입력
id = input("ID를 입력해주세요")

print('hello', id)

''' 
자료형: 데이터를 따룰 때 데이터의 종류

변수를 만들 때 사용자가 자료형을 결정하지 않아도 파이썬 내부에서 자동으로 자료형을 판단하여 적용됨

자료형 확인은 type()함수로 확인 가능

필요에 따라 자료형 변경 가능

숫자형
1) 정수형 int
2) 실수형 float
3)
'''