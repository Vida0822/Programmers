def dfs(n, ans):
    # [0] 종료조건
    if n == N:
        print(*ans)

    # [1] 재귀 호출
    for j in range(1, N+1):
        if v[j] == 0:
            v[j] = 1
            ans.append(j)  # 이렇게 하면 메모리 절약 : 매번 ans 배열을 새로 만드는게 아닌 값만 넣고 빼고 
            dfs(n+1, ans)
            v[j] = 0
            ans.pop()

N = int(input())
v = [0]*(N+1)
dfs(0, [])
