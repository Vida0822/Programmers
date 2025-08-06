T = int(input())
 
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    res = 0
    # 좌표를 하나씩 선회하면서
    for x in range(N) :
        for y in range(M) :
 
            # 중앙값 갱신
            sm = arr[x][y]
 
            # 중앙값(dx)만큼 양 옆(좌우) 범위의 합을 구함
            for dx in range(-arr[x][y],arr[x][y]+1) :
                nx = x + dx
                if 0 <= nx < N and x != nx: # 격자내의 범위인지 확인
                    sm += arr[nx][y]
            # 중앙값(dx)만큼 위 아래(상하) 범위의 합을 구함
            for dy in range(-arr[x][y],arr[x][y]+1) :
                ny = y + dy
                if 0 <= ny < M and y != ny:
                    sm += arr[x][ny]
 
            # 최대값 갱신
            res = max(res, sm)
 
    print(f'#{t} {res}')