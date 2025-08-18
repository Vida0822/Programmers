from collections import deque
delta = {0: (0, 0), 1:(0, -1), 2:(-1, 0), 3:(0, 1), 4: (1, 0)}

def move(ci, cj, cd):
    ni, nj = ci+delta[cd][0], cj+delta[cd][1]

    if not (1 <= ni <= N and 1 <= nj <= M):
        cd += 2 if cd in (1, 2) else -2
        ni, nj = ci+delta[cd][0], cj+delta[cd][1]

    return ni, nj, cd

def roll(cd): # 주사위 상태 변경
    # 1(왼쪽, 서)
    if cd == 1:
        dice[3], dice[4], dice[1], dice[5] = dice[4], dice[1], dice[5], dice[3]
        # Refactoring: 리스트도 자동 변환... 된다!

    # 2 (위쪽, 북)
    elif cd == 2 :
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]

    # 3 (오른쪽, 동)
    elif cd == 3 :
        dice[3], dice[5], dice[1], dice[4] = dice[5], dice[1], dice[4], dice[3]

    # 4 (아래쪽, 남)
    elif cd == 4:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]


def score(si, sj):

    # [0] 필요한 자료형
    q = deque()
    v = [[0]*(M+1) for _ in range(N+1)]

    # [1] 첫방문
    q.append((si, sj))
    v[si][sj] = 1

    # [2] 순회
    scr = arr[si][sj]
    cnt = 1
    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if not (1 <= ni <= N and 1 <= nj <= M):
                continue
            if v[ni][nj] == 0 and arr[ni][nj] == scr:
                v[ni][nj] = 1
                q.append((ni, nj))
                cnt += 1

    return scr*cnt


def direct(ci, cj, cd):

    A = dice[3]
    B = arr[ci][cj]

    if A > B :
        cd = cd+1 if cd+1 != 5 else 1
    elif A < B:
        cd = cd-1 if cd-1 != 0 else 4

    return cd


############# MAIN ###############
N, M, K = map(int, input().split())
arr = [[0]*(M+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]

dice = [2, 1, 5, 6, 4, 3]
ci, cj, cd = 1, 1, 3
ANS = 0
for _ in range(K):
    ci, cj, cd = move(ci, cj, cd)
    roll(cd)
    ANS += score(ci, cj)
    cd = direct(ci, cj, cd)
print(ANS)