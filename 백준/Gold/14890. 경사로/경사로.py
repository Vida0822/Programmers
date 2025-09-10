# [0]
N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr_t = list(map(list, zip(*arr)))

# [1]
def put(lst, v):
    h = lst[0]
    l = 1
    for j in range(1, N):
        if h == lst[j]:
            l += 1
        elif h > lst[j]:
            h = lst[j]
            l = 1
            continue
        elif h < lst[j]:
            if lst[j]-h > 1:
                return False
            if l < L :
                return False
            for jj in range(j-1, j-L-1, -1):
                if v[jj] == 1:
                    return False
                v[jj] = 1
            h = lst[j]
            l = 1
    return True


ANS = 0
for i in range(N):

    # 행
    lst = arr[i]
    v = [0]*N
    if put(lst, v) and put(lst[::-1], v[::-1]) :
        # print(lst)
        ANS += 1

    # 열
    lst = arr_t[i]
    v = [0]*N
    debug = 0
    if put(lst, v) and put(lst[::-1], v[::-1]):
        # print(lst)
        ANS += 1

# [2]
print(ANS)