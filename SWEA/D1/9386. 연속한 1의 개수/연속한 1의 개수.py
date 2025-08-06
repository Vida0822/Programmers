T = int(input())
 
for t in range(1, T+1):
    N = int(input())
    st = input()
 
    res = cnt = 0
    for s in st:
        if s == '1':
            cnt += 1
        else:
            res = max(res, cnt)
            cnt = 0
    else:
        res = max(res, cnt)
 
    print(f'#{t} {res}')