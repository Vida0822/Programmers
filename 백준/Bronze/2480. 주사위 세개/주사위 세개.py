A, B, C = map(int, input().split()) 
GET = 0

# 3개 
if A == B and B == C : 
    GET = 10000 + A*1000 
# 2개 
elif A == B or A == C :
    GET = 1000 + A*100
elif B == C :
    GET = 1000 + B*100

# 1개 
else : 
    GET = max(A,B,C)*100

print(GET)
    