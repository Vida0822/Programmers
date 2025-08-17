N, M = map(int, input().split())

for i in range(N, M+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1) : # 절반이 아닌 제곱근 전까지만 확인하면 됨
        if i%j == 0 :
            break 
    else: 
        print(i)
        
