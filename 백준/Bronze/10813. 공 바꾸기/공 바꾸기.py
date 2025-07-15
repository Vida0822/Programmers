N, M = map(int, input().split())
bags = [i for i in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())

    # 1. swap 직접 
#    tmp = bags[i] 
#    bags[i] = bags[j] 
#    bags[j] = tmp 
    
    # 2. tuple unpacking
    bags[i], bags[j] = bags[j], bags[i]
#   (bags[i], bags[j]) = (val1, val2) --> 튜플 객체 생성 후 대입(언패킹) 
    
print(*bags[1:])

