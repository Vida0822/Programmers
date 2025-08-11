"""
강사님 코드 
: 1차원 dp테이블 --> 불필요한 메모리 낭비 방지 
"""
N, M = map(int, input().split())
# A = [[0]*(M+1)] + [[0]+list(map(int, input().split())) for _ in range(N)]

dp = [0]*(M+1)
for _ in range(1, N+1):
    lst = [0]+list(map(int, input().split()))
    for j in range(1, M+1):
        dp[j] = lst[j] + max(dp[j], dp[j-1])
        # 1) dp[j] : i-1행에서 j열까지의 최대값 == dp[i-1][j]
        # 2) dp[j-1] : i행에서 j-1열까지의 최대값  == dp[i][j-1]

print(dp[M])


