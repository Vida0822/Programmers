from collections import deque

def oob(ni, nj) :
    return not (0 <= ni < 2**N and 0 <= nj < 2**N)

def devide(si, sj, ei, ej, arr):
    '''
    si, sj 로부터 arr의 (2**Lx2**L)만큼 추출하는 함수

    :param si, sj:  추출 시작 위치
    :param si, sj:  추출 완료 위치
    :param arr:  전체 arr
    :return: 추출한 sub_arr
    '''
    sub_arr = [[0]*(ej-sj) for _ in range(ei-si)]
    for i in range(n):
        for j in range(n): # arr내 위치
            sub_arr[i][j] = arr[si+i][sj+j]
    return sub_arr

def rotate(sub_arr):
    '''

    :param sub_arr: 추출한 sub_arr을 회전 시키는 함수
    :return: 회전된 sub_arr
    '''
    rot_arr = [lst[:] for lst in sub_arr]
    for i in range(n):
        for j in range(n):
            rot_arr[j][n-1-i] = sub_arr[i][j]
    return rot_arr


def attach(si, sj, ei, ej, rot_arr):
    '''
    기존 arr에 회전된 배열을 반영하는 함수
    :param si, sj: 반영 시작 위치
    :param rot_arr: 회전된 배열
    :return: 재배치한 배열
    '''

    for i in range(si, ei):
        for j in range(sj, ej):
            att_arr[i][j] = rot_arr[i%n][j%n]
    return att_arr

def chg_arr(arr):
    '''
    인접 4칸에 얼음이 2개 이하로 있으면 해당 칸 얼음 1 감소
    :param att_arr: 회전해서 붙인 얼음
    :return: 감소한 얼음 반영한 칸
    '''
    cp_arr = [lst[:] for lst in arr]
    for ci in range(2**N):
        for cj in range(2**N):
            cnt = 0
            for di, dj in ((-1 , 0), (0, -1), (0, 1), (1, 0)):
                ni, nj = ci+di, cj+dj

                if oob(ni, nj):
                    continue

                if arr[ni][nj] > 0 :
                    cnt += 1

            if cnt < 3 :
                cp_arr[ci][cj] -= 1

    return cp_arr

def bfs(si, sj) :
    global mem_cnt
    global mem_mx

    # [0] 자료형
    q = deque()
    mem = 0

    # [1] 첫방문
    q.append((si, sj))
    v[si][sj] = 1

    mem += 1
    mem_cnt += arr[i][j]

    # [2] 순회
    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj

            if oob(ni, nj):
                continue
            if v[ni][nj] :
                continue
            if arr[ni][nj] > 0 :
                mem_cnt += arr[ni][nj] # 얼음 합
                mem += 1 # 칸 수

                q.append((ni, nj))
                v[ni][nj] = 1

    mem_mx = max(mem_mx, mem)

# [0] 준비
N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
# t = 1
# for i in range(2**N):
#     for j in range(2**N):
#         arr[i][j] = t
#         t += 1

L_list = list(map(int, input().split()))
debug = 0

# [1] 실행
for i in range(Q):
    L = L_list[i]
    n = 2**L

    att_arr = [[0] * (2**N) for _ in range(2 ** N)]
    for si in range(0, 2**N, n) :  # 2**N+1: 정사각형 총 길이
        for sj in range(0, 2**N, n):
            ei, ej = si+n, sj+n

            # 1. 격자 나누기
            sub_arr = devide(si, sj, ei, ej, arr)
            debug = 1

            # 2. 회전 하기
            rot_arr = rotate(sub_arr)
            debug = 2

            # .3 붙이기
            att_arr = attach(si, sj, ei, ej, rot_arr)
            debug = 3

    arr = att_arr
    # 4. 얼음양 감소 (완탐, 인접 4칸)
    arr = chg_arr(arr)
    debug = 4


# [2] 정답
# ANS1 = 0
# for a in arr :
#     ANS1 += sum(a)

v = [[0]*(2**N) for _ in range(2**N)]
mem_cnt = 0
mem_mx = 0
for i in range(2**N):
    for j in range(2**N):
        if arr[i][j] > 0 and not v[i][j]:
            bfs(i, j)

print(mem_cnt)
print(mem_mx)