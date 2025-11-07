from collections import deque

def oob(ni, nj):
    return not (0 <= ni < N and 0 <= nj < M)


def crush(j, arr):
    '''
    구슬을 떨어트려 벽돌을 터트리는 함수 (연쇄 작용)
    :return: narr 변화된 map
    '''
    narr = [lst[:] for lst in arr]
    q = deque()

    # 1. 처음 터트릴 위치 찾기
    for i in range(N):
        if arr[i][j] > 0 :
            q.append((i, j, arr[i][j]))
            # narr[i][j] = 0
            break

    # 2. 터트리기 (연쇄적으로)
    while q:
        ci, cj, ck = q.popleft()

        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)) :
            for cnt in range(ck):
                ni, nj = ci+di*cnt, cj+dj*cnt

                if oob(ni, nj) or narr[ni][nj] == 0 :
                    continue

                if narr[ni][nj] > 0 :
                    q.append((ni, nj, narr[ni][nj]))
                    narr[ni][nj] = 0
                    # break  # 더 이상 해당 방향으로 가면 안됨 -> 아님 가도됨

    return narr


def down(arr):
    '''
    중력을 적용해서 arr을 변경시키는 함수 (two-pointer 활용)
    :param narr:
    :return:
    '''

    narr = []

    for j in range(M):
        lst = []
        for i in range(N-1, -1, -1):
            # print(len(arr[i]) , i)
            if arr[i][j] == 0 :
                continue
            else:
                lst.append(arr[i][j])
        narr.append(lst+[0]*(N-len(lst)))

    # 전치 행렬 (반시계 회전)
    return list(map(list, zip(*narr)))[::-1]


def check(arr):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 :
                cnt += 1
    return cnt


def dfs(n, arr):
    global K, N, M, ans

    '''
    해당 회차의 구슬을 떨어트러 벽돌을 터트리는 함수
    :param n: 떨어트린 구슬 개수
    :param sm:
    :param arr: 현재 경우의수까지의 변경된 map
    :return:
    '''

    # [0] 종료 조건
    if n == K :
        ans = min(ans, check(arr))
        return

    # [1] 핵심 로직
    for j in range(M):

        # 1. 구슬 없애주기
        narr = crush(j, arr) # 여기서 복사 배열 반환됨

        # 2. 중력 적용
        narr = down(narr)

        # [2] 재귀 호출
        dfs(n+1, narr)


def solve(arr):
    dfs(0, arr)
    return ans


#####################
TC = int(input())
for tc in range(1, TC+1):
    K, M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = N * M * 10
    ANS = solve(arr) # 남은 벽돌 개수의 최소값
    print(f"#{tc} {ANS}")