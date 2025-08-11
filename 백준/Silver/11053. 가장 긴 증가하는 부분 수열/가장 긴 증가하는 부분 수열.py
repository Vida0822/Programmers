

N = int(input())
A = list(map(int, input().split()))

# [0] 테이블 정의
# dp[i] : i자리까지 조사했을 때 가능한 최대 수열 길이 -> debug: i를 포함하는 최장 증가 수열 길이
dp = [0]*N

# [1] 초기값
dp[0] = ANS = 1

# [2] 점화식
for i in range(1, N): # O(N^2) : N <= 1000
    dp[i] = 1

    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)
    ANS = max(ANS, dp[i])

# [3] 정답 출력
# print(dp)
print(ANS)

