N = int(input())  # < 100
A = list(map(int, input().split()))
M = int(input())
S = [list(map(int, input().split())) for _ in range(M)]

A.insert(0, 0) 
for s in S : 
    if(s[0] == 1) :
        for i in range(1, N+1) : 
            if i%s[1] == 0 : 
                A[i] = 0 if A[i] == 1 else 1
        
    else :
        left = right = s[1] 
        while left > 0 and right <= N and A[left] == A[right] : 
            left -= 1 
            right += 1 
        
        for i in range(left+1, right) : 
            A[i] = 0 if A[i] == 1 else 1 

for i in range(1, len(A)) : 
    print(A[i], end =' ') 
    if i % 20 == 0 : 
        print()
    

