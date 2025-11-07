"""
접근
퀵 정렬

조건
- N <= 10^6 --> 최악의 경우 N log N으로 짜야함
"""
def dfs(lst):
    L = len(lst)
    # [0] 종료 조건
    if L == 0:
        return []
    elif L == 1 :
        return [lst.pop()]
    # else :
    #     pass

    # [1] 단위 작업
    piv = lst.pop()
    left = []
    right = []
    for i in range(L-1): # debug: piv을 pop()했기때문에 길이 1 줄음
        if lst[i] <= piv:
            left.append(lst[i])
        else :
            right.append(lst[i])

    # [2] 재귀 호출
    return dfs(left) + [piv] + dfs(right)


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    A = list(map(int, input().split()))
    # print(A)
    print(f'#{tc} {dfs(A)[N//2]}')
