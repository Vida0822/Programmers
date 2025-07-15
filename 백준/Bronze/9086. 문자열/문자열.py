T = int(input()) 

for _ in range(T) : 
    # st = input().split('')
    # 문자열 자체를 배열처럼 indexing 할 수 있기때문에 굳이 split X 
    st = input()
    print(st[0],st[len(st)-1],sep='')
    
    