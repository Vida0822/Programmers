T = int(input()) 

for t in range(1, T+1) :
    A, B = map(int, input().split()) 
    print('Case #',t,": ",A+B,sep='') # 공백 제거 : 구분자를 ''(null)로 지정한다 ex. sep ='_' 