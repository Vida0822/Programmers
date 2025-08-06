T = int(input())
 
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    res = 0
    for x in range(N) :
        for y in range(M) :
            sm = arr[x][y]
            for dx, dy in ([-1, 0], [1, 0], [0, -1], [0, 1]):
                nx = x + dx
                ny = y + dy
 
                if 0 <= nx < N and 0 <= ny < M:
                    sm += arr[nx][ny]
            res = max(res, sm)
 
    print(f'#{t} {res}')