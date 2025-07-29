import sys
sys.setrecursionlimit(10000)

def dfs(r, c):
    v[r][c] = 1
    width[res-1] += 1

    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
        nr, nc = r+dr, c+dc
        if 0 <= nr < M and 0 <= nc < N and metrix[nr][nc] == 0 and v[nr][nc] == 0:
                dfs(nr, nc)

# 1. 그래프 만들기
M, N, K = map(int, input().split()) # 행, 열 , 직사각형 개수

metrix = [[0]*N for _ in range(M)]
for _ in range(K) :
    c1, r1, c2, r2 = map(int, input().split())
    for r in range(r1, r2) :
        for c in range(c1, c2) :
            metrix[r][c] = 1

# 2. 전체 좌표 탐색 (빈칸찾기)
v = [[0]*N for _ in range(M)]
res = 0
width = []
for r in range(M) :
    for c in range(N) :
        if metrix[r][c] == 0 and v[r][c] == 0 :
            res += 1
            width.append(0)
            dfs(r, c)

print(res)
print(*sorted(width))