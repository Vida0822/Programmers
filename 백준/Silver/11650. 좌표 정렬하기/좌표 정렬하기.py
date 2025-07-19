N = int(input()) 

xys = []
for _ in range(N) : 
    xys.append(list(map(int,input().split())))
    
xys.sort(key=lambda xy:(xy[0],xy[1]))

for xy in xys : 
    print(xy[0], xy[1])
