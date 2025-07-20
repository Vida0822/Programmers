import math 

N = int(input())
A = [float(input()) for _ in range(N)]

# 1. Brute Force 
# O(N^3) 
# max_v = 0 
# for i in range(1, N):  # 고르는 개수
#    for j in range(0, N-i) : 
#        max_v = max(max_v, math.prod(A[j:j+i])) 
#        print(A[j:j+i], max_v) 
              
#print(round(max_v, 4) )

#2. DP 
for i in range(1, N) : 
    A[i] = max(A[i], A[i] * A[i-1]) 
    # A[i] : i까지 포함하는 수열의 최대곱
    #        --> 이전 항을 포함하는 최대수열*해당항 vs 해당항부터 시작 

print('%0.3f' % max(A))


