from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
g = [[5]*N for _ in range(N)]  # 땅 양분
tree = [[[] for _ in range(N)] for _ in range(N)]

# 나무 심기
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

# 8방향
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

for _ in range(K):
    dead = [[[] for _ in range(N)] for _ in range(N)]

    # 봄
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                tree[i][j].sort()
                alive = []
                for age in tree[i][j]:
                    if g[i][j] >= age:
                        g[i][j] -= age
                        alive.append(age + 1)
                    else:
                        dead[i][j].append(age)
                tree[i][j] = alive

    # 여름
    for i in range(N):
        for j in range(N):
            for age in dead[i][j]:
                g[i][j] += age // 2

    # 가을
    for i in range(N):
        for j in range(N):
            for age in tree[i][j]:
                if age % 5 == 0:
                    for d in range(8):
                        ni = i + dx[d]
                        nj = j + dy[d]
                        if 0 <= ni < N and 0 <= nj < N:
                            tree[ni][nj].append(1)

    # 겨울
    for i in range(N):
        for j in range(N):
            g[i][j] += A[i][j]

# 정답 출력
ans = 0
for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])
print(ans)
