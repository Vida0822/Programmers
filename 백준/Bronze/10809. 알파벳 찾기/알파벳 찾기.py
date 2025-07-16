S = input() 
map = dict() 

for i in range(len(S)): 
    map[S[i]] = map.get(S[i], i) 

# 숫자 -> 문자 : chr() 
for j in range(97, 123) : # 소문자 ASKII CODE
    print(map.get(chr(j), -1), end=' ')

