from collections import deque
def chk_linked(ans):
    # [0] 필요한 자료형
    cnt = 1
    q = deque()
    v2 = [[0]*5 for i in range(5)]

    # [1] 첫방문
    si, sj = ans[0]
    q.append((si, sj))
    v2[si][sj] = 1

    # [2] 순회
    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj

            if not (0 <= ni < 5 and 0 <= nj < 5):
                continue

            if not v2[ni][nj] and (ni, nj) in ans :
                v2[ni][nj] = 1
                cnt += 1
                q.append((ni, nj))
    if cnt == 7:
        return True
    else :
        return False

def chk_cnt(ans) :
    cnt = 0
    for i, j in ans :
        if adj[i][j] == 'S':
            cnt +=1
    if cnt >= 4 :
        return True
    return False


def dfs(n, i, ans):
    global ANS

    # [0] 종료조건
    if len(ans) == 7:
        if chk_linked(ans) and chk_cnt(ans):
            ANS += 1
        return

    # [1] 재귀호출
    for i in range(i, 25) :
        r = i//5
        c = i%5
        dfs(n+1,i+1, ans+[(r,c)])



adj = [list(input()) for _ in range(5)]
ANS = 0
dfs(0, -0, [])

print(ANS)