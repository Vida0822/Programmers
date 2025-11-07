"""
강사님 코드
"""

def dfs(n, sm):
    global ans

    # [0] 종료 조건
    # 가지치기
    if ans <= sm:  # 이미 최소값인 ans보다 크거나 같다면 (최소값일 때 유리)
        return  # 갱신 가능성 X

    # 정답 조건
    if n == N:
        ans = min(ans, sm)
        return

    # [1] 재귀 호출
    for j in range(N):  # 각 열 조회
        if not v[j]:
            v[j] = 1
            dfs(n + 1, sm + arr[n][j])
            v[j] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    v = [0] * N
    ans = 100
    dfs(0, 0)
    print(f'#{t} {ans}')