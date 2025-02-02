'''
숫자형
1) 정수형 int
2) 실수형 float
3) 복소수 complex

- 연산
- 내장함수
ex) round(), range(), pow()

a + b  a더하기 b
a - b  a빼기 b
a * b  a곱하기 b

* 나누기는 float형태로 출력됨 
a / b  a나누기 b
a // b a를 b로 나눈 몫 
a % b a를 b로 나눈 나머지
a ** b a의 b제곱
'''

a = 3  #정수형 int
b = 5 #정수형 int
c = 2.0 #실수형 float   
'''수학에서 2.0은 정수이지만 파이썬에서는 형태를 보고 추측하므로 실수로 구분됨
2(정수형 int)와 2.0(실수형 float)은 전혀 다름!!!
둘 중하나라도 실수면 실수형태로 출력
'''
d = 1.5 #실수형 float


print(a+b)  
print(a-b)
print(a*b)
print(a/b) 
print(a//b)
print(a%b)
print(a**b)

'''
논리형
1) bool
True 참 / False 거짓
- 참과 거짓을 나타내는 자료형
- 주로 비교, 논리 연산자로 만들어짐
- 조건문에 활용

비교연산자
< 작다
<= 작거나 같다
> 크다
>= 크거나 같다
== 같다
!= 같지 않다

논리 연산자
x or y   x나 y 둘 중 하나만 참이면 참
x and y  x,y 모두 참이여야 참
not x  x가 참이면 거짓, x가 거짓이면 참  
'''

x = 10
y = -10

print(x>0)
print(y>0)
print()
print(x>y)
print(x<y)
print()
print(x==10)
print(x==y)
print(x!=y)
print()
print(x>0 or y>0)
print(x>0 and y>0)
print()
print(x>0)
print(not x>0)

'''
문자열형 str
- '' 또는 ""에 감싸져있다
- 문자열 메소드
ex) split(), join(), upper(), lower(), replace()
- 연산 불가(예외: 문자+문자 , 문자*정수)
- 문자와 문자열을 구분하지 않음!
- 문자는 글자 한개, 문자열은 글자가 한개이상
'''

