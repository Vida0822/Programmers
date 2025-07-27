import math 

A, B, V = map(int, input().split()) 

# Ax-B(x-1) >= V 
# print(math.ceil(V-B/A-B)) --> 오류 발생 : B/A가 먼저 계산되기 때문
print(math.ceil((V-B)/(A-B)))