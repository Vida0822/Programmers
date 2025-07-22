N = int(input())

for i in range(1, N+1) : 
    print(' '*(N-i),'*'*i, sep='') # sep=''안하면 공백 두고 출력