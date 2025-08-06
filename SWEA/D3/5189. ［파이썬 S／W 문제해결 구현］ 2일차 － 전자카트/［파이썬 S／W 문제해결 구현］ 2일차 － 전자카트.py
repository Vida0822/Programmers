"""
강사님 코드
: 패딩 사용

N: 방문한 구역 수
--> 종료 조건 : n == N
"""

def dfs(n, sm, cur):
    global ans

    # if ans <= sm+arr[cur][1]:
    #     return
    # -> FAIL: 다 돌지 않았는데 1로 복귀하는 비용이 엄청 커서 ans 값을 초과한 경우 검사를 종료해버림
    #          (실제로 몇군데 들려 돌아가다보면 ans 값보다 작을 수 있는데! )

    # [0] 종료 조건
    if n == N :  # 모든 구역 방문
        ans = min(ans, sm+arr[cur][1])
        return

    for j in range(2, N+1):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, sm+arr[cur][j] ,j)
            v[j] = 0

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())

    arr = [[0]*(N+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]
    ans = 100*N

    # 구역수, 비용합, 기준구역번호
    v = [0]*(N+1)
    dfs(1, 0, 1)
    print(f'#{tc} {ans}')
