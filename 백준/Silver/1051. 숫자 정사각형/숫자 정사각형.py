N, M = map(int, input().split())
# 직사각형
arr = []
for _ in range(N) :
    arr.append(list(map(int, input())))

memo = [-1 for i in range(10)] # i가 적혀있는 정사각형 중 최대 변 길이

# 직사각형의 각 칸을 이동하면서
for x in range(N) :
    for y in range(M) :

        # 해당 칸에서 정사각형을 하나씩 키우면서 만듬 (변이 직사각형 끝에 닿을때까지) 
        for i in range(min(N-x, M-y)):
            nx = x + i
            ny = y + i

            # 만약 네개의 꼭지점이 모두 같으면
            if arr[x][y] == arr[nx][y] == arr[x][ny] == arr[nx][ny] :
                # 최대값 갱신
                memo[arr[x][y]] = max(memo[arr[x][y]], i+1)

# 최대넓이 = 최대변**2
print(max(memo)**2)