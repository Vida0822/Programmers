N, K = map(int, input().split()) 
A = []
for _ in range(N) : 
    A.append(int(input()))
    
# greedy : 높은 금액의 동전 사용할 수록 good
count = 0 
while K > 0 : 
    count += K//A[N-1]
    K -= (K//A[N-1])*A[N-1]
    N -= 1 
       
print(count)    
