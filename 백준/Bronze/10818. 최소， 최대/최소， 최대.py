N = int(input())
nums = list(map(int, input().split()))
# ※1. map 객체는 indexing이 안되는거 명심 !! (단순히 iterator로 순차반환만)
# ※2. Iterator는 실행(순차 반환)할 때 소비(요소 삭제)되어 재사용 불가능 --> list로 변환해 여러번 참조하도록

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
# max(iterable) - iterable : 리스트, 문자열, 튜플, map 객체
print(min(nums), max(nums))
