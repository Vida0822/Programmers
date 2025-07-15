# "공백으로 주어진다" --> map(int, input().split()) : 배열로 바꾼 후 대입
# "각 줄마다 주어진다" --> input(), input() : 각각 입력받음
x = int(input()) 
y = int(input()) 

# 1. 다중 if : 조건을 모두 표시 
# if x > 0 and y > 0:
#     print(1) 
# if x < 0 and y > 0 : 
#     print(2) 
# if x < 0 and y < 0 : 
#     print(3)
# if x > 0 and y < 0 : 
#     print(4)

# 2. elif/else 사용 : 중복 조건 생략
if x > 0 : 
    if y > 0 : 
        print(1) 
    else : 
        print(4) 
else : 
    if y > 0 : 
        print(2) 
    else : 
        print(3)

    

