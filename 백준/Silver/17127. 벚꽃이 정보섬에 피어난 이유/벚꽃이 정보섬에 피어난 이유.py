import math 

N = int(input()) 
A = list(map(int, input().split()))

# 완전 탐색 ? 4개로 나누는 조합을 모두 구하고, 가장 큰 값을 반환 
# N이 10 이하이기 때문에 가능 
ans = 0 
# 각각의 반복 변수가 각 나무에 포함되는 번호의 '끝' 인덱스

# O(N^3) * O(N) : 리스트에 있는 숫자 더하기
for i in range(1, N-2) : 
    for j in range(i+1, N-1) : 
        for k in range(j+1, N) : # N-2  
            ans = max(ans, math.prod(A[:i]) + math.prod(A[i:j]) + math.prod(A[j:k]) + math.prod(A[k:]))
                
print(ans)

