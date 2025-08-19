
TC = int(input())
def turn(cd, c):

    if c == 'L':
        cd = (cd-1)%4
    else:
        cd = (cd+1)%4

    return cd

dirs = {0:(1, 0), 1:(0, 1), 2:(-1, 0), 3:(0, -1)}
def move(ci, cj, cd, c):
    global max_i, min_i, max_j, min_j

    if c == 'F' :
        ni, nj = ci + dirs[cd][0], cj+dirs[cd][1]
    else:
        ni, nj = ci + dirs[(cd+2)%4][0], cj + dirs[(cd+2)%4][1]

    max_i, min_i = max(max_i, ni), min(min_i, ni)
    max_j, min_j = max(max_j, nj), min(min_j, nj)

    return ni, nj


for _ in range(TC):
    command = input()
    ci, cj, cd = 0, 0, 0 # [위, 오, 아래, 왼]

    max_i, min_i = 0, 0
    max_j, min_j = 0, 0
    for c in command:
        if c in ('L', 'R'):
            cd = turn(cd, c)
        else:
            ci, cj = move(ci, cj, cd, c)
    # print((max_i, min_i), (max_j , min_j))
    print((max_i-min_i)*(max_j - min_j))