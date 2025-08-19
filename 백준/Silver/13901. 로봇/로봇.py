R, C = map(int, input().split())
K = int(input())
arr = [[0]*C for _ in range(R)]

for _ in range(K):
    i, j = map(int, input().split())
    arr[i][j] = 2 # 장애물

si, sj = map(int, input().split())
S = list(map(int, input().split()))

delta = {1:(-1,0), 2:(1, 0), 3:(0, -1), 4:(0, 1)}
def move(ci, cj, i):
    cd = S[i]
    cnt = 0
    while True :
        ni, nj = ci+delta[cd][0], cj + delta[cd][1]

        if not (0 <= ni < R and 0 <= nj < C) or arr[ni][nj]:
            i += 1
            cd = S[i%len(S)]
            cnt += 1
        else:
            arr[ni][nj] = 1
            ci, cj = ni, nj
            cnt = 0

        if cnt == len(S):
            return ci, cj


arr[si][sj] = 1
print(*move(si, sj, 0))
