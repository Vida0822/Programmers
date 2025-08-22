"""
DP
"""

n = int(input())
dp = [0]*(n+1)

# 초기식
dp[0] = 1
dp[1] = 1

# 점화식
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

# 답 출력
print(dp[n]%10007)
