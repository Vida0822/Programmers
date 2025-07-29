import sys
sys.setrecursionlimit(500000)

def dfs(ci, cj) :
    v[ci][cj] = 1

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
        ni, nj = ci+di, cj+dj

        if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == 255 and v[ni][nj] == 0 :
            dfs(ni, nj)


# 1. 그래프 만들기 (픽셀 입력하기)
N , M = map(int, input().split())
graph = [[0]*M for _ in range(N)]

input_arr = [list(map(int, input().split())) for _ in range(N)]
T = int(input())

for i in range(N) :
    lst = input_arr[i]

    for j in range(0, M*3-2, 3) :
        if T <= sum(lst[j:j+3])/3 :
            graph[i][j//3] = 255

# 2. 전체 좌표 완전 탐색
res = 0
v = [[0]*M for _ in range(N)]
for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 255 and v[i][j] == 0 :
            res += 1
            dfs(i, j)

print(res)