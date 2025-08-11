N = int(input())
A = list(map(int, input().split()))

# [0] dp 테이블 정의
dp = [0]*N

# [1] 초기값
dp[0] = A[0]

# [2] 점화식
ANS = dp[0] # Edge 고려 (n=1) 이 값보다 큰 수열 합이 나오면 갱신되고, 큰 수열 합이 없으면 해당 값이 정답이 됨
for i in range(1, N) :
    dp[i] = max(dp[i-1]+A[i], A[i])
    ANS = max(ANS, dp[i])

# [3] 답 출력
print(ANS)
