"""
강사님 코드 1 
: 부분 수열/집합 정석 코드 --> 포함/미포함
"""

def dfs(n, sm, cnt):
    global ans

    # [0] 종료 조건
    if n == N:
        if cnt > 0 and sm == S: # cnt > 0 : 크기가 양수인 부분 수열
            ans += 1
        return

    # [1] 재귀 호출
    dfs(n+1, sm+lst[n], cnt+1) # 선택
    dfs(n+1, sm, cnt) # 선택 X


N, S = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0
dfs(0, 0, 0)

print(ans)