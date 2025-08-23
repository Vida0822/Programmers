TC = int(input())

for _ in range(TC):
    n = int(input())

    # dp 테이블 : n을 1,2,3으로 구성하는 경우의 수
    dp = [0]*(n+1)

    if n < 3:
        print(n)
        # ※ 채워지는 초기 테이블 인덱스보다 검사 범위가 작은 경우 고려해줘야함
    else:
        # 초기 테이블
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4

        # 점화식
        for i in range(4, n+1) :
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        # 결과 출력
        print(dp[n])

