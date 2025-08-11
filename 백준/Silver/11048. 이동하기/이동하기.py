N, M = map(int, input().split())

# A = [0]*(N+1) + [[0]+list(map(int, input().split())) for _ in range(N)] # 패딩 필요
A = [[0]*(N+1)] + [[0]+list(map(int, input().split())) for _ in range(N)] # 패딩 debug... 행 패딩 붙일때 2차원 배열로 만들어서 붙여야함 주의


# [0] 테이블 정의
dp = [[0]*(M+1) for _ in range(N+1)]

# [1] 초기값
dp[1][1] = A[1][1]

# [2] 점화식 -->  O(N*M)
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) # 패딩 있기때문에 범위체크 X
        dp[i][j] += A[i][j]

# [3] 답 부분 출력
print(dp[N][M])
