
N = int(input())

# [0] dp 테이블 정의
# dp[i]: 1로부터 i를 만드는데 사용한 연산 횟수 최소값
dp = [0]*(N+1)

# [1] 초기값
dp[1] = 0

# [2] 반복문으로 채우기
for i in range(2, N+1):
    dp[i] = dp[i-1]+1

    if i%2 == 0 :
        dp[i] = min(dp[i], dp[i//2] +1)

    if i%3 == 0 :
        dp[i] = min(dp[i], dp[i//3] +1)

# print(dp)
print(dp[N])

