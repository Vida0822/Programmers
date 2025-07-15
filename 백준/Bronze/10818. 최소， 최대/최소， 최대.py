N = int(input())
nums = list(map(int, input().split())) # map 객체는 indexing이 안되는거 명심 !! (단순히 iterator로 순차반환만)
# O(N)
# 1. 직접 구현 
# max_val, min_val = -1000001 , 1000001
# max_val = min_val = nums[0]  # 초기값을 첫 입력값으로 지정해도 괜찮
# for num in nums : 
#    if num < min_val :
#        min_val = num 
#    if num > max_val : 
#        max_val = num 
#print(min_val, max_val)

# 2. max(), min() 사용 
print(min(nums), max(nums))
