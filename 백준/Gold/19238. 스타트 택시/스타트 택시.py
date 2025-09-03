"""
조건
- NxN

접근 방법
1. 모든 손님까지의 최단 거리 구하기 (완탐으로 찾고 -> 각각 BFS)
2. 그 중 가장 가까운 손님 반환 (거리 -> 행 -> 열 기준)
3. 택시 이동 -> 연료 (-)
4. 그 손님의 도착지까지 최단 거리 구하기
5. 택시 이동 -> 연료 (-) -> 연료 (+)

"""
from collections import deque
import sys
input = sys.stdin.readline

# [0]
N, M, F = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ti, tj = map(int, input().split())
ti -= 1
tj -= 1

people = []
for _ in range(M):
    si, sj, ei, ej = map(int, input().split())
    people.append((si-1, sj-1, ei-1, ej-1)) # DEBUG: 계속 패딩 안하는데 문제에서 입력하는 좌표에서 1 안빼줌
    # si, sj, ei, ej
debug = 0

# [1]
def bfs(si, sj):
    """
    그냥 모든 칸으로의 최단 거리를 구하는 함수
    (최단 거리 손님 찾기, 도착지 찾기 로직 통일하기 위해 그냥 v 배열 반환)
    :return: v
    """
    # [0]
    q = deque()
    v = [[0]*N for _ in range(N)]

    # [1]
    q.append((si, sj))
    v[si][sj] = 1

    # [2]
    while q :
        ci, cj = q.popleft()

        for di, dj in ((-1 ,0), (0, -1), (0, 1), (1, 0)) :
            ni, nj = ci+di, cj+dj

            if not (0 <= ni < N and 0 <= nj < N):
                continue
            if v[ni][nj] or arr[ni][nj]: # 방문 or 벽
                continue

            v[ni][nj] = v[ci][cj] + 1
            q.append((ni, nj))

    return v


def find(ti, tj):
    '''
    최단 거리 손님을 찾는 함수
    :param ti, tj: 택시 출발 위치
    :return: 최단 거리 손님 정보 (출발지, 도착지, 거리)
    '''
    # 현재 칸에서 모든 칸으로의 최단 거리 구하기
    v = bfs(ti, tj)
    # 해당 거리 자체를 기준으로 사람들 정렬  (1. 거리순, 2. 행순 , 3. 열순)
    people.sort(key=lambda p: (-v[p[0]][p[1]], -p[0], -p[1]))
    # 태울 손님 결정
    si, sj, ei, ej = people.pop()
    d = v[si][sj]-1 # DEBUG : 거리 자체는 v 배열에서 1 빼서 반환해야함 !!!

    return si, sj, ei, ej, d


def go():
    global ti, tj, F
    debug = 'S'
    # 1. 태울 최단 거리 손님 찾기
    si, sj, ei, ej, dist = find(ti, tj)
    debug = 1

    # 2. 택시 -> 손님 이동
    if dist == -1 :
        return False
    if F >= dist:
        F -= dist
    else:
        return False
    debug = 2

    # 3. 손님 -> 도착지 이동
    v = bfs(si, sj)
    dist = v[ei][ej] -1
    debug = 3
    if dist == -1 :
        return False
    if F >= dist:
        # F -= dist
        # F += dist*2
        F += dist
    else:
        return False
    ti, tj = ei, ej
    debug = 4
    return True


# 모든 손님에 대해 운전 시도하기
for _ in range(M) :
    if not go():
        F = -1
        break

# [2]
print(F)




