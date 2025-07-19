T = int(input()) 
    
for _ in range(T) : 
    k, n = int(input()), int(input())

    # 1. top-down 
#    count = down(k-1, n)
    
    # 2. bottom-up 
    apart = [[0]*(n+1) for _ in range(k+1)] 
    apart[0] = list(range(n+1))

    for i in range(1, k+1) : 
        for j in range(1, n+1) : 
            apart[i][j] = apart[i][j-1] + apart[i-1][j]
    
    print(apart[k][n])
    