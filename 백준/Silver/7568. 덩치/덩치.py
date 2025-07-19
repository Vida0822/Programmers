N = int(input()) 
mans = []

# 중복 있는 순위 매기기
for _ in range(N) : 
    mans.append(list(map(int, input().split())))

# 완전 탐색 : 자신보다 몸무게와 키 모두 큰 사람 수 세기 
for i in range(N) : 
    count = 1 
    for j in range(N) : 
        if mans[i][0] < mans[j][0] and mans[i][1] < mans[j][1] : 
            count += 1 
    print(count, end = ' ')
    



    
        
        
        
    