T = int(input())
for t in range(1, T+1) :
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # arr = [0]*(N+1) + [[0]+list(map(int, input().split())) for _ in range(N)]
 
    # Brute Force
    res = 0
    for i in range(N-M+1): # 검사를 시작할 위치 (i, j)
        for j in range(N-M+1):
            sm = 0
            for x in range(M): # 그 위치부터 MxM 내 숫자 다 더하고
                for y in range(M):
                    sm += arr[i+x][j+y]
            res = max(res, sm) # max 값 갱신
 
    print(f'#{t} {res}')