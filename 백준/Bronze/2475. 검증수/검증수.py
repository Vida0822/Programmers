# 검증수 : sum(각 숫자**2 ) % 10 

lst = list(map(int, input().split()))
sm = 0
for i in lst : 
    sm += i**2 

print(sm%10)

    