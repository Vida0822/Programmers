# (di, dj ) in ([-1,0]...) --> 튜플 형태가 편함! (dx, dy 배열보다는!)

H, W= map(int, input().split())
arr = [input() for _ in range(H)]
times = [[-1]*W for _ in range(H)]

# 1. Flag를 이용한 분기
for h in range(H) :
    flag = False # 해당 행에 구름을 만났는지 여부
    sm = 0
    for w in range(W) :
        if arr[h][w] == 'c':
            times[h][w] = 0
            if not flag :
                flag = True
            if flag :
                sm = 0
        else:
            if not flag :
                times[h][w] = -1
            if flag :
                sm += 1
                times[h][w] = sm

for time in times :
    print(*time)

