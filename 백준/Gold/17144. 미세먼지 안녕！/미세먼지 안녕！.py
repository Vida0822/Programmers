delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def oob(ni, nj) :
    return not (0 <= ni < N and 0 <= nj < M)

def spread() :
    '''
    미세먼지 퍼지는 정도를 조건따라 계산해서 A 배열 변경
    :return: X
    '''
    cp = [[0]*M for _ in range(N)]

    # 1) 각 먼지의 증감값 도출
    for ci in range(N): # delta 적용할거면 무조건 ci, cj로 쓰자
        for cj in range(M):
            if A[ci][cj] == -1:
                continue

            t = A[ci][cj] // 5
            if t > 0:
                cnt = 0
                for di, dj in delta:
                    ni, nj = ci+di, cj+dj

                    # 범위 체크
                    if oob(ni, nj) or A[ni][nj] == -1:
                        continue

                    cp[ni][nj] += t
                    # A[ni][nj] += t
                    cnt += 1
                cp[ci][cj] -= cnt*t
                # A[ci][cj] -= cnt*t

    # 2) 증감값 A 배열에 반영
    for i in range(N):
        for j in range(M):
            if A[i][j] != -1 :
                A[i][j] += cp[i][j]


def refresh_up(si, sj, ei, ej) :
    '''
    위의 공기청정기로 A 배열 값들 가장자리만 <반시계> 회전 (A배열 변경)
    :param si, sj: 대상 직사각형 좌상단 좌표
    :param ei, ej: 대상 직사각형 우하단 좌표
    :return: X
    '''

    # 왼쪽 끝열 ↓
    for i in range(ei-1, si-1, -1):
        if A[i+1][sj] == -1 :
            continue
        A[i+1][sj] = A[i][sj]

    # 맨위 1열 ←
    for j in range(sj+1, ej+1) :
        A[si][j-1] = A[si][j]

    # 오른쪽 끝열 ↑
    for i in range(si+1, ei+1) :
        A[i-1][ej] = A[i][ej]

    # 맨아래 끝열 →
    for j in range(ej-1, sj-1, -1):
        if j == sj:
            A[ei][j] = 0
        A[ei][j+1] = A[ei][j]

    A[up[0]][up[1]] = -1


def refresh_dwn(si, sj, ei, ej):
    '''
    위의 공기청정기로 A 배열 값들 가장자리만 <시계> 회전 (A배열 변경)
    :param si, sj: 대상 직사각형 좌상단 좌표
    :param ei, ej: 대상 직사각형 우하단 좌표
    :return: X
    '''

    # 왼쪽 끝열 ↑
    for i in range(si+1, ei+1):
        if A[i-1][sj] == -1:
            continue
        A[i-1][sj] = A[i][sj]

    # 맨아래 끝열 ←
    for j in range(sj+1, ej+1):
        A[ei][j-1] = A[ei][j]

    # 오른쪽 끝열 ↓
    for i in range(ei-1, si-1, -1):
        A[i+1][ej] = A[i][ej]

    # 맨위 1열 →
    for j in range(ej-1, sj-1, -1):
        if j == sj:
            A[si][j] = 0
        A[si][j+1] = A[si][j]

    A[dwn[0]][dwn[1]] = -1

# [0] 시뮬레이션 준비
N, M, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 공기 청정기 찾기
for i in range(N):
    if A[i][0] == -1:
        up = (i, 0)
        dwn = (i+1, 0)
        break
    # debug = 0

# [1] 시뮬레이션 실행
for _ in range(T):
    # 1) 미세먼지 확산
    spread()
    debug = 1

    # 2) 공기 청정 (위, 반시계)
    refresh_up(0, 0, up[0], M-1)
    # debug = 2

    # 3) 공기 청정 (아래, 시계)
    refresh_dwn(dwn[0], 0, N-1, M-1)
    debug = 3


# [2] 시뮬레이션 출력
ans = 0
for i in range(N):
    for j in range(M) :
        if A[i][j] != -1:
            ans += A[i][j]
# debug = 4
print(ans)