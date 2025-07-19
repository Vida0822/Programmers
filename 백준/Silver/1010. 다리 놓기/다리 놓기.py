T = int(input())

# 경우의 수 : M 개 중 N개를 고르는 경우의 수 mCn 
for _ in range(T) : 
    N, M = map(int, input().split())

    # 1. 직접 구현 
    N = min(N, M-N) 
    up = 1 
    for n in range(N) :
        up*=(M-n) # 
    
    down = 1 
    for n in range(1, N+1) : 
        down*=n 

    print(up//down)

