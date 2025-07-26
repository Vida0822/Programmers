N = int(input())  # <= 1000 
scores = list(map(int, input().split())) 

M = max(scores) # O(N)
# sm = 0  
#for sc in scores :  
#    sm += sc/M*100
sm = sum(sc/M*100 for sc in scores ) 
# O(N) not O(2N) ! 
# 1) 제너레이터 표현'식'을 생성 : 식만 생성한거지 아직 순회/값 계산 X 
# 2) 실제로 참조할 때 순차적으로 계산 (sum()이 인자로 받은 이터러블 순회하면서 하나씩 꺼내 더함)
# ※ 제네레이터는 리스트처럼 미리 만드는게 x 
print(sm/N)
    

