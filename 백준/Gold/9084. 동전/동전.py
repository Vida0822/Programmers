T = int(input()) 

for _ in range(T) : 
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    
    # 동전 각각을 개수 상관없이 골라서 합치는 문제 
    # dp[i] : i원을 만들 수 있는 경우의 수 
    dp = [0]*(M+1)
    dp[0] = 1  # +1이 아닌 그 이전 값 자체를 더해주기 때문에 0원인 경우는 1로 해줘야함
    # 각각의 동전에 대해 
    for coin in coins : 
        # 목표금액을 만드는 경우의 수에 
        # (목표금액-해당동전금액)을 만드는 경우의 수를 더한다.
        # --> 그 동전이 여러번 사용될 수 있는 경우도 적용 가능 
        # ex. 5원동전, 10원 동전 --> dp[10] = 1+1 = 2, dp[20] = 2+1 = 3 
        for i in range(M+1) : 
            if coin <= i : 
                dp[i] += dp[i-coin]
    print(dp[M])            