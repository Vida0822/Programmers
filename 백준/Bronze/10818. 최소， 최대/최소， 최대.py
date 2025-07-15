N = int(input())
nums = map(int, input().split())

# 1. 직접 구현 
max, min = -1000001 , 1000001
for num in nums : 
    if num < min :
        min = num 
    if num > max : 
        max = num 
print(min, max)
        
