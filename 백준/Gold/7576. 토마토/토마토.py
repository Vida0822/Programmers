"""
시간복잡도 : 3xO(NxM)

[구상]
q에 전달해주는 요소로 좌표 뿐 아닌 (현재 좌표 토마토가 익는데 걸린 days +1) 같이 전달
1) q가 빌때까지 날짜 누적하고
2) q가 다 빈후 전체검사해서 0이 남아있으면 -1, 없으면 days 반환
"""

from collections import deque
import sys

def solve() :

    # 1. 그래프 만들기
    input = sys.stdin.readline
    M , N = map(int, input().split())
    adj = [list(map(int, input().split())) for _ in range(N)]

    # 전체 좌표 순회하면서 좌표가 1(익은 토마토 시작점) 이면 큐에 집어넣음
    q = deque()
    v = [[0]*M for _ in range(N)]
    for i in range(N) :
        for j in range(M) :
            if adj[i][j] == 1 :
                q.append((i, j, 0))
                v[i][j] = 1

    # 2. 탐색 시작 
    d = -1
    while q:
        ci, cj, d = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj

            # 범위 체크
            if not (0 <= ni < N and 0 <= nj < M) :
                continue

            if adj[ni][nj] == 0 and v[ni][nj] == 0 :
                adj[ni][nj] = 1
                v[ni][nj] == 1
                q.append((ni, nj, d+1)) # 전달하는 세번째 요소 : 현재 좌표까지 걸린 날짜


    # 3. 안 익은 토마토 남았는지 확인
    for i in range(N) :
        for j in range(M) :
            if adj[i][j] == 0:
                return -1
    else:
        return d


print(solve())
