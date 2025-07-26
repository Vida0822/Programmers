# 이항계수 : 주어진 크기 집합에서 원하는 개수만큼 뽑는 가지수 (순서X) 
# => 즉, 조합 
import math 

N, K = map(int, input().split()) 
# K = min(K, N-K) # K가 0이 되는 경우 생김

# O(K)
print(math.prod(N-i for i in range(K)) // math.prod(i for i in range(1, K+1)))