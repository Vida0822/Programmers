# 가운데 문자 기준으로 나누어서

S = input() 

# 1. pointer로 각각 검사 
ans = 1 
for i in range(len(S)):
    if S[i] != S[len(S)-1-i]:
        ans = 0 
        break

print(ans)
       