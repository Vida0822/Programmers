N, M = map(int, input().split()) 
cards = list(map(int, input().split()))

# 1. 카드 정렬 
cards.sort() 

# 2. 완전 탐색 (3중 반복문)
# 카드의 합이 M이하인 모든 경우를 구하고, 그중 가장 큰 값을 반환 
result = 0 

# 코드 기억 : 중복 없는 모든 조합을 구하는 코드 
for i in range(N) : 
    for j in range(i+1, N) : 
        for k in range(j+1, N) : 
            if cards[i]+cards[j]+cards[k] <= M :
                result = max(result, cards[i]+cards[j]+cards[k])

print(result)    
    
    
