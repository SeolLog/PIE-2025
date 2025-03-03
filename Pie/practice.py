# 250303
animal = "강아지"
name = "연탄이"
age = 4
hobby="산책"
is_adult = age >= 3

print("우리집" + animal + "이름은" + name + "에요")

# 정수형은 str()로 감싸주기
# boolean형도 str()로 감싸주기
# 문자열과 숫자를 더할때는 str()으로 감싸야하지만
# 쉼표를 써주면 str()필요 없음 
print(name +"는"+ str(age) + "살 이며," + hobby + "를 아주 좋아해요.")
print(name + "는  어른일까요?" + str(is_adult))


