"""
1차 시도 : dfs (백트래킹)
- 풀이 시간 : 1시간 / 실패 (왕을 만나지 않는다면 영원히 이동 가능하다)

2차 시도 : bfs
- 풀이 시간 : 20분 / 가장 가까운 곳부터 방문하기에 도착만하면 그게 가장 최단거리
"""

from collections import deque

# 상의 8방향 이동 (최종 위치, 중간 2칸)
moves = [
    ((-3, -2), (-1, 0), (-2, -1)),
    ((-3, 2), (-1, 0), (-2, 1)),
    ((-2, -3), (0, -1), (-1, -2)),
    ((2, -3), (0, -1), (1, -2)),
    ((3, -2), (1, 0), (2, -1)),
    ((3, 2), (1, 0), (2, 1)),
    ((-2, 3), (0, 1), (-1, 2)),
    ((2, 3), (0, 1), (1, 2)),
]

def bfs(ci, cj):

    # [0] 필요한 자료형
    q = deque()
    v = [[0]*9 for _ in range(10)]

    # [1] 첫 방문
    q.append((ci, cj, 0))
    v[ci][cj] = 1

    # [2] 인접 노드 순회 (가까운 곳부터 방문하기에 도착만하면 가장 최소로 이동한 것! )
    # bfs: '최단거리'
    while q:
        ci, cj, cnt = q.popleft()

        if ci == R2 and cj == C2 :
            return cnt

        for (di, dj), (mi, mj), (m2i, m2j) in moves:
            if (ci+mi == R2 and cj+mj == C2) or (ci+m2i == R2 and cj+m2j == C2):
                continue

            ni, nj = ci+di, cj+dj
            if not (0 <= ni < 10 and 0 <= nj < 9) :
                continue

            if not v[ni][nj]:
                v[ni][nj] = 1
                q.append((ni, nj, cnt+1))
                # print(ci, cj ,'->', ni, nj)


R1, C1 = map(int, input().split())  # 상 위치
R2, C2 = map(int, input().split())  # 왕 위치


ANS = bfs(R1, C1)

print(ANS if ANS != 0 else -1)
