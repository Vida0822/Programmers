import copy
from collections import deque

def virus(lab): # BFS
    # [0] 필요한 자료형
    q = deque()
    v = [[0]*M for _ in range(N)]
    copy_lab = copy.deepcopy(lab)

    # [1] 첫방문
    for si in range(N):
        for sj in range(M):
            if copy_lab[si][sj] == 2:
                q.append((si, sj))
                v[si][sj] = 1

    # [2] 순회
    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj

            if not (0 <= ni < N and 0 <= nj < M):
                continue
            if v[ni][nj] == 0 and copy_lab[ni][nj] == 0:
                v[ni][nj] = 1
                copy_lab[ni][nj] = 2
                q.append((ni, nj))

    return copy_lab


def cnt(copy_lab) : # Brute-Force
    cnt = 0
    for i in range(N):
        for j in range(M):
            if copy_lab[i][j] == 0:
                cnt += 1
    return cnt

def build_walls(n, si, sj): # Backtracking
    global ANS

    # [0] 종료 조건
    if n == 3:
        copy_lab = virus(lab)
        ANS = max(ANS, cnt(copy_lab))
        return

    # [1] 재귀 호출
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                build_walls(n+1, i, j)
                lab[i][j] = 0


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
ANS = 0

build_walls(0, 0, 0)
print(ANS)