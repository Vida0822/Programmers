from collections import deque
delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def oob(ni, nj) :
    return not (0 <= ni < N and 0 <= nj < N)

def bfs(si, sj, cw) :
    '''
    :param si, sj: 상어의 좌표
    :param cw: 상어의 무게
    :return: 먹을 수 있는 물고기 (최소만 X, 일단 전부 넣는다)
    '''

    # [0] 필요한 자료형
    q = deque()
    v = [[0]*N for _ in range(N)]
    ret = []

    # [1] 첫 방문
    q.append((si, sj))
    v[si][sj] = 1

    # [2] 순회
    while q:
        ci, cj = q.popleft()

        if 0 < A[ci][cj] < cw:
            ret.append((ci, cj, v[ci][cj]-1))

        for di, dj in delta:
            ni, nj = ci+di, cj+dj

            # 범위
            if oob(ni, nj):
                continue

            # 미방문
            if v[ni][nj] :
                continue

            if A[ni][nj] <= cw:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))
    return ret



# [0] 시뮬레이션 준비
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 상어 찾기
for i in range(N): # O(N^2)
    for j in range(N):
        if A[i][j] == 9:
            A[i][j] = 0
            ci, cj = i, j
            break
cw = 2

# [1] 시뮬레이션 실행
time = 0 # ans
eat = 0
while True:
    # 1. 먹을 수 있는 물고기 : 이동 가능 + 크기 작음
    fishes = bfs(ci, cj, cw)
    # debug = 0

    # 2. 종료 조건
    if not fishes:
        break

    fishes.sort(key=(lambda x : (x[2], x[0], x[1])))
    ni, nj, cnt = fishes.pop(0)
    # debug = 1


    # 3. 물고기 먹기
    A[ni][nj] = 0
    eat += 1
    # debug = 2

    # 4. 이동 시간 누적
    time += cnt
    # debug = 3

    # 5. 크기 비교
    if eat == cw:
        cw += 1
        eat = 0

    # 6. 이동 : 좌표 변환
    ci, cj = ni, nj



# [2] 시뮬레이션 출력
print(time)


