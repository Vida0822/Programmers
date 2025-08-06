"""
접근 : 부분 집합
"""

def dfs(n, sm, ans, cnt):
    global ANS

    # 가지치기
    if sm > R:
        return

    # [0] 종료 조건
    if n == N:
        ans.sort() # O(NlogN)

        # w정답 조건
        if L <= sm <= R and ans[-1]-ans[0] >= X :
            ANS += 1

        return

    # [1] 재귀 호출
    # ans.append(A[n]) # debug: 정렬 했을때 pop 위치 달라짐
    dfs(n+1, sm+A[n], ans+[A[n]],cnt+1) # 포함
    # ans.pop()

    dfs(n+1, sm, ans ,cnt) # 포함 X


################################################
N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))

ANS = 0
dfs(0, 0, [] ,0)
print(ANS)

