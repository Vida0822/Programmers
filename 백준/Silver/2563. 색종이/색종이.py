N = int(input())
metrix = [[0]*101 for _ in range(101)]

for i in range(N) : 
    X, Y = map(int, input().split())  
    
    for x in range(X, X+10) : 
        for y in range(Y, Y+10) : 
            metrix[x][y] = 1 
            
width = 0 
for x in range(101) :  # O(100^2)
    for y in range(101) : 
        if metrix[x][y] == 1  :
            width += 1 
print(width)        

            