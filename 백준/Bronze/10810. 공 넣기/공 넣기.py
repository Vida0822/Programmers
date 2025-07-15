N, M = map(int, input().split()) 

# bag = list(N)
# list 길이 지정 : 반복문 활용
# bag = list(0 for i in range(N+1))
bag = [0] * (N+1) # --> 직관적, 가독성 good 

for _ in range(M): 
    i, j, k = map(int, input().split()) 
    
    for t in range(i, j+1) : 
        bag[t] = k 

print(*bag[1:]) # list의 범위를 지정해서 요소 print --> 이렇게 하면 [] 까지 같이 출력됨 
