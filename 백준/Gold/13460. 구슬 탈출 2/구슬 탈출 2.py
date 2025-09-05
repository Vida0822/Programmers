# [0]
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]

for i in range(N):
    for j in range(M) :
        if arr[i][j] == 'R':
            ri, rj = i, j
        elif arr[i][j] == 'B':
            bi, bj = i, j

debug = 0

# [1]
def move(si, sj, dr):
    back = -1
    di, dj = delta[dr]
    for cnt in range(1, 10):  # 최대 이동 가능 cnt : 10
        ni, nj = si+di*cnt, sj+dj*cnt

        if arr[ni][nj] == '#' :
            return cnt + back # DEBUG : back 자체가 좌표를 빼주는 거잖아!! 더해줘야지  (헷갈리면 아예 back_cnt 를 하고 빼주던가 -> 변수가 뭘 의미하는지 정확히 기억)
        elif arr[ni][nj] in ('R', 'B'):
            back -= 1
        elif arr[ni][nj] == 'O':
            return cnt
        else : # '.' 일때
            pass

def dfs(n, ri, rj, bi, bj, dr):  # 이동한 횟수
    global ANS

    # [0] 종료 조건
    if n > ANS:
        return False

    # [1] 핵심 로직 : 해당 방향으로 구슬 이동
    # 0. 이동할 횟수 반환
    r_cnt = move(ri, rj, dr)
    b_cnt = move(bi, bj, dr)

    # 1. 이동 가능한지 확인
    # 두 구슬 다 이동 X
    if r_cnt == 0 and b_cnt == 0 :
        return False

    # 2. 실제 이동
    di, dj = delta[dr]
    nri, nrj = ri+r_cnt*di, rj+r_cnt*dj # 빨간공
    nbi, nbj = bi+b_cnt*di, bj+b_cnt*dj # 파란공

    # 3. 종료 조건 체크
    if arr[nbi][nbj] == 'O': # 파란공 들어가면 실패 !
        return False
    if arr[nri][nrj] == 'O': # 빨간공만 들어가면 성공 !
        ANS = min(ANS, n)
        return True

    # [2] 재귀 호출 (종료 조건 불만족시)
    for d in range(4):
        arr[ri][rj], arr[bi][bj] = '.', '.'
        arr[nri][nrj], arr[nbi][nbj] = 'R', 'B'
        dfs(n+1, nri, nrj, nbi, nbj, d)
        arr[nri][nrj], arr[nbi][nbj] = '.', '.' # 이걸 먼저 해야함 (nri, nrj == ri, rj 인 경우)
        arr[ri][rj], arr[bi][bj] = 'R', 'B'  # 항상 write 복구를 나중에 !


ANS = 11
# for i in range(1, 11): # 이거 대체 왜해준거지....? 의미 없는 코드 X
for dr in range(4): # 첫번째 방향은 반복문으로 정해줌 -> n = 1
    if dfs(1, ri, rj, bi, bj, dr):
        break

# [2]
print(ANS if ANS != 11 else -1)
