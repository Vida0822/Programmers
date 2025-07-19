N = int(input()) 

xys = []
for _ in range(N) : 
    xys.append(list(map(int,input().split())))
    
xys.sort()

for xy in xys : 
    print(*xy)
