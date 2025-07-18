N, M = map(int, input().split()) 
cards = list(map(int, input().split()))

# [조합]
# cards.sort() --> 완전탐색이므로 정렬 필요 X 

# 1. 완전 탐색, 3중 반복문
# 카드의 합이 M이하인 모든 경우를 구하고, 그중 가장 큰 값을 반환 
result = 0 

# 코드 기억 : 중복 없는 모든 조합을 구하는 코드 


# 2. permutaions, combinations(Intertools) : 순열, 조합 라이브러리                

from itertools import combinations 

for card in combinations(cards, 3) : # cards에서 3개를 뽑는 조합 리스트 
    if result < sum(card) <= M : 
        result = sum(card)

print(result)    
    
    
