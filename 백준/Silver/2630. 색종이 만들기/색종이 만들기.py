def check(arr):
    c = arr[0][0]

    L = len(arr)
    for i in range(L):
        for j in range(L):
            if arr[i][j] != c:
                return False
    else:
        return True


def dfs(arr):

    # [0] 종료 조건
    if check(arr):
        CNT[arr[0][0]] += 1
        return

    # [1] 재귀 호출
    L = len(arr)//2
    lu = []
    ru = []
    for li in range(L) :
        lu.append(arr[li][:L])
        ru.append(arr[li][L:])

    ld = []
    rd = []
    for li in range(L, 2*L):
        ld.append(arr[li][:L])
        rd.append(arr[li][L:])

    dfs(lu)
    dfs(ru)
    dfs(ld)
    dfs(rd)



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

CNT = [0]*2
dfs(arr)
print(CNT[0])
print(CNT[1])
