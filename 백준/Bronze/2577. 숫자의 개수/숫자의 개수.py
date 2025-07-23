A, B, C = [int(input()) for _ in range(3)] 

st = str(A*B*C)

for i in range(0, 10) : 
    print(st.count(str(i))) 

