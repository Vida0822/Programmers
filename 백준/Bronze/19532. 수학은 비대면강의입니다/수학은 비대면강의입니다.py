a, b, c, d, e, f = map(int, input().split()) 

ans = (0, 0) 
# 완전 탐색 : x, y 에 범위 내 모든 값을 대입 
for x in range(-999, 1000) : 
    for y in range(-999, 1000) : 
        if a*x+b*y==c and d*x+e*y==f : 
            print(x, y)