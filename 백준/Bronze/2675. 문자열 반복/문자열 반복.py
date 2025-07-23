T = int(input())

for _ in range(T):
    # 공백을 기준으로 다른 자료형 입력 받음 --> 좋은 방법 있을까? 
    R, S = input().split()
    R = int(R)

    print(*[s*R for s in S], sep='') 
    # end=''를 하면 각 요소간은 그대로 공백 구분되어서 출력되고, 개행을 안함 
    # 요소간 공백 출력 안하려면 sep=''로 지정해줘야함
