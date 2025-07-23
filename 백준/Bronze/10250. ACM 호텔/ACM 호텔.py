T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    
    # h, w : 변수 의미 파악이 어려움, 도메인에 맞는 변수명 사용 better 
    floor = N%H 
    room = N//H +1 
    
    if floor==0 : 
        floor = H 
        room -= 1 

#    print(h, '%02d' % w, sep='') --> 이 형태보다는 f-string 사용하는게 현대적
    print(f'{floor}{room:02}') # f{변수:형식지정자}  
    