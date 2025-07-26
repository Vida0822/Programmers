N = int(input()) 
lst = list(map(int, input().split())) 

for i in lst : # 1, 
    for j in range(2, (i+1)//2+1) : 
        if i % j == 0: 
            N -= 1 
            break
    if i == 1 : 
        N -= 1 
        
print(N)
           