L = int(input()) 
st = input() 

H = sum([(ord(st[i])+1-ord('a'))*(31**i) for i in range(L)]) % 1234567891 
print(H)