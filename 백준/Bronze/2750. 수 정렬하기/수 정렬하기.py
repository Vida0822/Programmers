def dfs(lst):

    # [0] 종료 조건
    if not lst : # debug : pop from empty list --> left, right가 빈 리스트일 때 아래애서 그냥 pop을 시도
        return []
    if len(lst) == 1:
        return [lst.pop()]

    # [1] 단위 작업
    piv = lst.pop()
    left = []
    right = []

    for l in lst:
        if l <= piv :
            left.append(l)
        else:
            right.append(l)

    # [2] 재귀 호출 
    return dfs(left) + [piv] + dfs(right)


N = int(input())
A = [int(input()) for _ in range(N)]
ans = dfs(A)

for a in ans:
    print(a)

