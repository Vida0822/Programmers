"""
1차 시도
최단 거리를 구해야하는 상황이 여러개
=> 최대한 bfs 로직을 공통으로 빼고, 리턴값을 visited로해 상황에 맞게 활용
=> 시간 초과나면... BFS 하는중에 최소값 갱신하고 그걸 리턴하는 로직으로 재구성....

* 유의할 상태값 : 연료 --> 중간 중간 체크

종료 조건
1. 이동 도중에 연료가 바닥나서 다음 출발지나 목적지로 이동할 수 없으면
2. 모든 손님을 이동시킬 수 없는 경우에도 -1을 출력
--> 결국 1번이랑 2번은 같은 조건 아닌가... ?

문제: 사람들의 si, sj -> ei, ej 연결......

2차시도 
set&map 활용 디버깅 실패... 비효율적이라도 그냥 v기준 사람들 list 정렬
"""

from collections import deque

# [0]
N, M, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ti, tj = map(int, input().split())
ti, tj = ti-1, tj-1 # DEBUG: 계속 이거 빼주는거 빼먹는다

people = []
for _ in range(M) :
    si, sj, ei, ej = map(int, input().split())
    people.append((si-1, sj-1, ei-1, ej-1))
# people_arr = [[0]*N for _ in range(N)]
# people_set = set()
# for idx in range(M):
#     si, sj, ei, ej = map(int, input().split())
#     people_set.add((si-1, sj-1)) # DEBUG: -1 해주는거 계속 까먹는다...
#     people_arr[si-1][sj-1] = (ei-1, ej-1)

debug = 0

Exception
# [1]
def oob(ni, nj):
    return not (0 <= ni < N and 0 <= nj < N)

# def find_min_person(v):
#     mn = (-1, -1, 400)
#     changed = False
#     for i in range(N):
#         for j in range(N) :
#             if (i, j) in people_set:
#                 if v[i][j] < mn[2] and v[i][j] != -1 : # DEBUG) 조건 추가: 이동 불가능
#                     changed = True
#                     mn = (i, j, v[i][j])
#     if not changed: # DEBUG : 데리러갈 수  있는 손님이 없을 때 이상한 값이 반환돼서 key error 발생
#         return None
#     else:
#         return mn
    # return mn

def bfs(si, sj) :
    '''
    단순히 모든 좌표로의 최단 거리를 구하는 함수 (여러 상황에서 호출함을 대비)
    :param si, sj:
    :return: visited 배열
    '''
    # [0]
    q = deque()
    v = [[-1]*N for _ in range(N)] # DEBUG : 거리 정보 정확성 위해 0대신 -1로 채워줌

    # [1]
    q.append((si, sj))
    v[si][sj] = 0

    # [2]
    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ni, nj = ci+di, cj+dj

            # 범위밖
            if oob(ni, nj):
                continue
            # 벽
            if arr[ni][nj]:
                continue
            # 방문 --> DEBUG : 계속 이거 빼먹는다...
            if v[ni][nj] != -1:
                continue
            # 이동 가능
            v[ni][nj] = v[ci][cj]+1
            q.append((ni, nj))

    return v

def solve(L):
    # global L
    global ti, tj

    for _ in range(M):
        # 1. 최단 거리 승객 찾기
        v = bfs(ti, tj)
        # for p in people:
        #     print(*p)
        people.sort(key=lambda p: (-v[p[0]][p[1]], -p[0], -p[1])) # 수정 필요...

        si, sj, ei, ej = people.pop()
        cnt = v[si][sj]
        debug = 1

        # 2. 택시 이동 (상태값 체크)
        if cnt == -1 : # 가로 막혀서 이동 불가
            return -1
        if L < cnt: # 연료 없어서 이동 불가
            return -1
        else: # 이동 가능
            L -= cnt # 연료 감소
            ti, tj = si, sj  # 실제 이동
        debug = 2

        # 3. 승객 -> 도착지 이동 (상태값 체크)
        # pi, pj = people_arr[si][sj]
        v = bfs(si, sj)
        cnt = v[ei][ej]

        if cnt == -1: # 가로 막혀서 이동 불가
            return -1
        if L < cnt: # 연료 없어서 이동 불가
            return -1
        else:  # 이동 가능
            L += cnt # '승객을 태워 이동하면서 소모한 연료' 양의 두 배가 충전
            ti, tj = ei, ej # 이동
            # people_arr[pi][pj] = 0 # 도착지 map에서 삭제
        debug = 3

    return L

# [2]
print(solve(L))