N,M = map(int,input().split())

# A = [[] for _ in range(M)]
A = [[0]*M for _ in range(N)]
# 1) [0]*M --> [0,0,..,M]
# 2) [0,0,..,M]*N = [0,0,..,M],[0,0,..,M],[0,0,..,M]
# 3) [] --> [[0,0,..,M],[0,0,..,M],[0,0,..,M]]
# ※ [[0]*M]*N
B = []


for i in range(N) : 
#    A.append(list(map(int, input().split())))
    
    A[i] = list(map(int, input().split()))
        
for i in range(N) : 
    B.append(list(map(int, input().split())))

for i in range(N) : 
    for j in range(M) : 
        print(A[i][j] + B[i][j] , end=' ')
    print()
        
    