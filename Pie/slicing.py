jumin = "950304-1234567"
# 인덱스는 0부터 시작 
print("성별:" + jumin[7])
print("연:" + jumin[0:2]) #0:2 0~2직전 인덱스까지 출력
print("월:" + jumin[2:4])
print("일:" + jumin[4:6])

print("생년월일" + jumin[:6]) #처음부터 값을 출력할때는 0생략가능, 처음부터 6직전까지 출력
print("뒤 7자리" + jumin[7:]) #7부터 끝까지 값 출력 
print("뒤 7자리(뒤에부터):" + jumin[-7: ]) #맨 뒤에서 7번째부터 끝까지 