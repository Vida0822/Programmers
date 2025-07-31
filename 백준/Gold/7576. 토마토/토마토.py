"""
시간복잡도 : 3xO(NxM)
"""

from collections import deque
import sys

def solve() :
    input = sys.stdin.readline

    M , N = map(int, input().split())
    adj = [list(map(int, input().split())) for _ in range(N)]

    q = deque()
    v = [[0]*M for _ in range(N)]
    for i in range(N) :
        for j in range(M) :
            if adj[i][j] == 1 :
                q.append((i, j, 0))
                v[i][j] = 1

    d = -1
    while q:
        ci, cj, d = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj

            if not (0 <= ni < N and 0 <= nj < M) :
                continue

            if adj[ni][nj] == 0 and v[ni][nj] == 0 :
                adj[ni][nj] = 1
                v[ni][nj] == 1
                q.append((ni, nj, d+1))


    for i in range(N) :
        for j in range(M) :
            if adj[i][j] == 0:
                return -1
    else:
        return d

print(solve())