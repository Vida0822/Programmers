import math
T = int(input())
for _ in range(T) :
    M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    mul = 1
    for i in range(N) :
        mul *= arr[i][0]
    ans = (1, mul)
    
  #  print(-(1e9*(N+1)))
    for j in range(M) :
        mul = 1
        for i in range(N) :
            mul *= arr[i][j]

        if ans[1] <= mul :
            ans = (j+1, mul)

    print(ans[0])
