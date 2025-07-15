N, M = map(int, input().split())
bags = [i for i in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    tmp = bags[i] 
    bags[i] = bags[j] 
    bags[j] = tmp 
    
print(*bags[1:])

