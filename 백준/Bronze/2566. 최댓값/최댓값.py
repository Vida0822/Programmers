metrix = [] 

max_v = -1
ans = (-1, -1)
for i in range(9) : 
    # metrix[i][j] = int(sys.stdin.read(2).strip())
    # 한 문자씩 입력받기 --> 숫자가 두자리일수도 있으므로 bad
    metrix.append(list(map(int, input().split())))
    for j in range(9) :       
        if(metrix[i][j] > max_v) : 
            max_v = metrix[i][j] 
            ans = (i, j)

print(max_v)            
print(ans[0]+1, ans[1]+1)        
        