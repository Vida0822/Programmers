while True : 
    st = input() 
    if st == '0' : 
        break 
    N = len(st)
    for i in range(N//2) : 
        if st[i] != st[N-i-1] : 
            print('no')
            break 
    else :
        print('yes')
            
    