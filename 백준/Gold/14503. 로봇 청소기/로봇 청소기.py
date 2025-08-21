delta = {0: (-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)} # 북, 동, 남, 서

def back(ci, cj, cd):

    di, dj = delta[(cd-2)%4]
    ni, nj = ci+di, cj+dj
    if not (0 <= ni < N and 0 <= nj < M) or arr[ni][nj] == 1 :
        return -1, -1

    return ni, nj


def front(ci, cj, cd, v):

    ni, nj = ci+delta[cd][0], cj+delta[cd][1]

    if not (0 <= ni < N and 0 <= nj < M) :
        return ci, cj
    if arr[ni][nj] == 1 or v[ni][nj] == 1:
        return ci, cj

    return ni, nj


# 입력
N, M = map(int, input().split())
si, sj, sd = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 청소 시작
def solve(ci, cj, cd):
    ANS = 0
    v = [[0]*M for _ in range(N)]

    while True :
        # 1. 해당 칸 청소
        if not v[ci][cj]:
            v[ci][cj] = 1
            ANS += 1

        # 2. 주변 4칸 확인
        cnt = 0
        for di, dj in delta.values():
            ni, nj = ci+di, cj+dj

            # 범위 체크
            if not (0 <= ni < N and 0 <= nj < M):
                continue

            # 청소X + 빈칸 O 인지 확인
            if v[ni][nj] == 0 and arr[ni][nj] == 0:
                cnt += 1

        # 3. 이동 : case 1/2
        if cnt == 0:
            ci, cj = back(ci, cj, cd)
            if ci == -1 and cj == -1 :
                return ANS
        else:
            ni, nj = ci, cj
            while ni == ci and nj == cj :
                cd = (cd-1)%4
                ni, nj = front(ci, cj, cd, v) # 빈칸으로 갈 때까지 회전
            ci, cj = ni, nj

    return ANS


print(solve(si, sj, sd))