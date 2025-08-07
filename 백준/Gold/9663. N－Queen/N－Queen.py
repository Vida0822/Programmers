"""
강사님 코드
- 백트래킹
- 규칙성을 찾을 때 (i, j)를 표시하고 시각적으로 찾는 연습

"""

def dfs(n):
    global ans

    # [0] 종료 조건
    if n == N:
        ans += 1
        return

    # [1] 재귀 호출
    for j in range(N):
        # if v1[j] == v2[j] == v3[j] == 0: --> 비교 무조건 3번 :시간 낭비
        if v1[j] == 0 and v2[n+j] == 0 and v3[n-j] == 0:
            v1[j] = v2[n+j] = v3[n-j] = 1
            dfs(n+1)
            v1[j] = v2[n+j] = v3[n-j] = 0


N = int(input())

v1 = [0]*N
v2 = [0]*2*N
v3 = [0]*2*N

ans = 0
dfs(0)
print(ans)