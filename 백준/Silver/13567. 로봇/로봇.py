
dirs = {0 : {0, 0}, 1:(0, -1), 2:(1, 0), 3:(0, 1), 4:(-1, 0)}
def turn(cd, ord):
    if ord == 0 :
        nd = (cd-1) if (cd-1) != 0 else 4
    else :
        nd = (cd+1) if (cd+1) != 5 else 1
    return nd

def move(ci, cj, cd, ord):
    di, dj = dirs[cd]
    ni, nj = ci+di*ord, cj+dj*ord

    # 범위 체크
    if not (0 <= ni <= M and 0 <= nj <= M):
        return -1, -1
    return ni, nj

M , n = map(int, input().split())

ci, cj, cd = 0, 0, 3
res = True
for _ in range(n):
    com, ord = input().split()

    if com == 'TURN' :
        cd = turn(cd, int(ord))
    else:
        ci, cj= move(ci, cj, cd, int(ord))
        if (ci, cj) == (-1, -1):
            res = False
            break

if res :
    print(cj, ci)
else:
    print(-1)

