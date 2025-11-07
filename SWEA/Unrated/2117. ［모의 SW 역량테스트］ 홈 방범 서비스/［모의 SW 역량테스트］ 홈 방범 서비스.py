TC = int(input())

def oob(ni, nj):
    return not (0 <= ni < N and 0 <= nj < N)


def make_dia(ci, cj, K):
    '''
    중심 좌표가 ci, cj고, 중심좌표로부터 각 꼭지점까지 길이가 K인 마름모 표시 (범위밖제외)
    :param si:
    :param sj:
    :param K:
    :return:
    '''

    v = [[0]*N for _ in range(N)]
    sj = ej = cj
    if not oob(ci-K, cj): v[ci-K][cj] = 1
    if not oob(ci+K, cj): v[ci+K][cj] = 1

    for i in range(ci-K+1, ci+K+1):
        if i <= ci:
            sj -= 1
            ej += 1
        else:
            sj += 1
            ej -= 1

        for j in range(sj, ej+1):
            if 0 <= i < N and 0 <= j < N:
                v[i][j] = 1

    return v


def score():
    global ans

    # [0]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 1 and arr[i][j] == 1:
                cnt += 1

    # [1]
    # 수익
    gain = M*cnt
    lose = (K**2)+((K-1)**2)
    profit = gain-lose
    if profit >= 0:
        ans = max(ans, cnt)

for tc in range(1, TC+1) :
    # [0]
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = -1
    # [1]
    for ci in range(N):
        for cj in range(N):  # 중심 좌표
            for K in range(1, 2*N):
                # 1. 마름모 만들기
                v = make_dia(ci, cj, K-1) # 도시 크기
                debug = 0

                # 2. 점수 계산
                score() # ans 갱신
                debug = 1


    print(f'#{tc} {ans}')




