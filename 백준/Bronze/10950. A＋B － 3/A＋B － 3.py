T = int(input()) 

for t in range(T) : # range(1, T) : 1부터 T미만의 숫자를 포함하는 'range 객체'를 만들어주는것(=list) 
    A, B = map(int, input().split()) 
    print(A+B)