# 00000 -> 10101
 
dirs = [(0, 1), (1, 0), (1, 1), (-1, 1)] # 가로, 세로, 대각선
 
def solve(N, arr) :
    for x in range(N):
        for y in range(N):
            if arr[x][y] != 'o' :
                continue
            for dr in dirs:  # 특정 좌표에 대해 가로, 세로, 대각선 검사(우방향만)
                cnt = 1
                nx = x + dr[0]
                ny = y + dr[1]
 
                while 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
                    cnt += 1
                    nx += dr[0]
                    ny += dr[1]
 
                if cnt == 5:
                    return 'YES'
    return 'NO'
 
T = int(input())
for t in range(1, T+1) :
    N = int(input())
    arr = [input() for _ in range(N)]
    print(f'#{t} {solve(N , arr)}')