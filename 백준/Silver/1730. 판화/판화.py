N = int(input())
arr = [['.']*N for _ in range(N)]
command = input()

com_map = {'U':1, 'D':2, 'L':3, 'R':4}
dirs = {1:(-1,0), 2:(1, 0), 3:(0, -1), 4:(0, 1)}

def move(com, ci, cj) :
    com = com_map[com]
    di, dj = dirs[com]
    ni, nj = ci+di, cj+dj

    # 범위 체크
    if not (0 <= ni < N and 0 <= nj < N):
        return ci, cj

    # 방향 표시
    if com in (1, 2):
        arr[ci][cj] = '|' if arr[ci][cj] != '-' and arr[ci][cj] != '+' else '+'
        arr[ni][nj] = '|' if arr[ni][nj] != '-' and arr[ni][nj] != '+' else '+'
    elif com in (3, 4):
        arr[ci][cj] = '-' if arr[ci][cj] != '|' and arr[ci][cj] != '+' else '+'
        arr[ni][nj] = '-' if arr[ni][nj] != '|' and arr[ni][nj] != '+'  else '+'

    return ni, nj


ci, cj = 0, 0
for com in command:
    ci, cj = move(com, ci, cj)

for a in arr :
    print(''.join(a))

