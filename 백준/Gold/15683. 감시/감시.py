"""
2차 도전
=> 수정 포인트 : 하나의 델타 배열로 관리하고 경우 따라 참조
"""
def test(cp_A):
    for a in cp_A:
        print(*a)
    print()

def oob(ni, nj):
    return not (0 <= ni < N and 0 <= nj < M)

def check(cp_A):
    '''

    :param cp_A: 감시영역 표시된 배열
    :return: 사각지대(0) 개수
    '''
    cnt = 0
    for i in range(N):
        for j in range(M):
            if cp_A[i][j] == 0:
                cnt += 1
    return cnt

def spread(cctv):
    '''
    감시 영역을 표시한 복사 배열을 반환
    :param cctv: cctv가 위치한 좌표
    :return: cp_A
    '''

    cp_A = [lst[:] for lst in A]
    for ci, cj in cctv:
        directions = v[ci][cj]
        for idx in directions:
            di, dj = delta[idx]
            ni, nj = ci, cj

            while True:
                # 감시 영역 표시
                ni, nj = ni+di, nj+dj

                if oob(ni, nj):
                    break
                if cp_A[ni][nj] == 6:
                    break
                if cp_A[ni][nj] == 0 :
                    cp_A[ni][nj] = '#'

    debug = 1
    return cp_A

def dfs(n, i, j) :
    '''
    각 cctv의 방향을 결정해 조합
    :param n: 방향을 정해준 cctv 개수
    :param i, j: 이전 검사 위치
    :return: X -> ANS 값만 갱신
    '''
    global ANS
    # [0] 종료 조건
    if n == cctv_cnt :
        cp_A = spread(cctv)
        cnt = check(cp_A)
        ANS = min(ANS, cnt)

        # test(cp_A)
        return

    # [1] 재귀 호출
    # 각 cctv 방향 결정
    for ci in range(i, N):
        for cj in range(M):
            if ci == i and cj < j :
                continue
            if v[ci][cj] :
                continue
            if 1 <= A[ci][cj] <= 5:
                directions = look_up[A[ci][cj]]
                for d in directions :
                    v[ci][cj] = d
                    dfs(n+1, ci, cj)
                    v[ci][cj] = 0

# [0] 시뮬레이션 준비
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# cctv 개수
cctv = []
for i in range(N):
    for j in range(M):
        if 1 <= A[i][j] <= 5:
            cctv.append((i, j))
cctv_cnt = len(cctv)

delta = {0:(-1, 0), 1:(0, -1), 2:(1, 0), 3:(0, 1)} # 상, 좌, 하, 우
look_up = {1:[(0,), (1,), (2,), (3,)],
           2:[(0, 2), (1, 3)],
           3:[(0, 1), (1, 2), (2, 3), (0, 3)],
           4:[(0, 1, 2), (1, 2, 3), (0, 1, 3), (0, 2, 3)],
           5:[(0, 1, 2, 3)]}

# [1] 시뮬레이션 실행
ANS = N*M+1
v = [[0]*M for _ in range(N)]
dfs(0, 0, 0)

# [2] 시뮬레이션 출력
print(ANS)


# 계속 실수 : 2차원 백트래킹 j 좌표