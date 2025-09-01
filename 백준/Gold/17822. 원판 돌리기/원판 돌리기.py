from collections import deque

def oob(ni):
    return not (0 <= ni < N)

def rotate(i, d, k):
    '''
    특정 원판 line을 shift 시키는 함수

    :param line: shift 시킬 원판 라인
    :param d: 0)시계, 1)반시계
    :param k: shift 칸 수
    :return: X -> 바로 원판 상태 변경
    '''

    # 시계
    if d == 0 :
        for _ in range(k):
            arr[i].insert(0, arr[i].pop()) # 여유되면 deque로 변경
    # 반시계
    elif d == 1:
        for _ in range(k):
            arr[i].append(arr[i].pop(0))

def change(si, sj, cp_arr, arr): # BFS
    '''
    BFS로 인접 방문해가며 숫자가 같으면 cp 배열에 0 표시 (숫자 지우기)
    :param arr: 회전시킨 원판
    :return: cp_arr
    '''

    # [0] 필요한 자료형
    q = deque()

    # [1] 첫 방문
    q.append((si, sj, arr[si][sj]))
    v[si][sj].add(arr[si][sj])

    # [2] 순회
    while q:
        ci, cj, cn = q.popleft()

        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ni, nj = ci+di, (cj+dj)%M

            if oob(ni) or not arr[ni][nj]:
                continue

            if cn in v[ni][nj]:
                continue

            nn = arr[ni][nj]
            q.append((ni, nj, nn))
            v[ni][nj].add(cn)

            # 원판 갱신
            if cn == nn :
                cp_arr[ci][cj] = 0
                cp_arr[ni][nj] = 0

    return cp_arr

def change_2(cp_arr):
    '''

    :param arr: 수가 삭제되지 않은 원판
    :return: 각각 +1, -1 한 원판
    '''
    sm = 0
    cnt = 0
    # 1. 평균 구하기
    for i in range(N):
        for j in range(M):
            if cp_arr[i][j] > 0 :
                sm += cp_arr[i][j]
                cnt += 1
    if cnt == 0 :
        return cp_arr

    mean = sm/cnt

    # 2. 각 원판 값 바꾸기
    for i in range(N):
        for j in range(M):
            if cp_arr[i][j] == 0:
                continue
            if cp_arr[i][j] > mean:
                cp_arr[i][j] -= 1
            elif cp_arr[i][j] < mean:
                cp_arr[i][j] += 1

    return cp_arr


# [0] 준비
N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

debug = 0

# [1] 실행
for _ in range(T):
    # 1. 회전
    x, d, k = map(int, input().split())

    for i in range(1, N+1):
        if i%x == 0:
            rotate(i-1, d, k)
    debug = 1

    # 2. 원판 갱신 (숫자 변경)
    cp_arr = [lst[:] for lst in arr]
    v = [[set() for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not v[i][j] and arr[i][j]:
                change(i, j, cp_arr, arr)
                debug = 2

    # 3. 원판 갱신 X
    if arr == cp_arr :  # 이거 값 비교만 되나 ? (수정 필요)
        cp_arr = change_2(cp_arr)
        debug = 3
    arr = cp_arr


# [2] 출력
ANS = 0
for i in range(N):
    for j in range(M):
        ANS += arr[i][j]
print(ANS)