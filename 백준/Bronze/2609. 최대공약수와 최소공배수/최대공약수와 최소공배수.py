sm, bg = sorted(map(int, input().split()))
# sm = min(A, B) 
# bg = max(A, B) 

res1 = res2 = 1 
for i in range(1, sm+1): 
    # 최대공약수 
    if sm%i == 0 and bg%i == 0 :
        res1 = i 

    # 최소공배수 
    if bg*i % sm == 0 and res2 == 1: 
        res2 = bg*i

print(res1, res2, sep='\n')
