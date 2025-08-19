dirs = {0:(-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)} # 북동남서
def move(ci, cj, cd) :

    di, dj = dirs[cd]
    ni, nj = ci + di*arr[ci][cj], cj+dj*arr[ci][cj]

    if not (0 <= ni < N and 0 <= nj < M):
        return -1, -1

    return ni, nj

def trap(si) :

    ci, cj, cd = si, 0, 1
    while True :
        ci, cj = move(ci, cj, cd)
        cd = (cd+1)%4
        if ci == -1:
            return False
        if (ci, cj, cd) in v:
            return True
        v.add((ci, cj, cd))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ANS = []
for i in range(N):
    v = {(i, 0, 1)}
    if trap(i):
        ANS.append(i)

# 정답 출력
if ANS :
    print(len(ANS))
    for a in ANS :
        print(a+1, end=' ')
else:
    print(0)