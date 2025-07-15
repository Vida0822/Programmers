X = int(input())
N = int(input())

SUM = 0 
for _ in range(N) : 
    a, b = map(int, input().split())
    SUM += a*b 

if SUM == X : 
    print('Yes')
else :
    print('No')
    