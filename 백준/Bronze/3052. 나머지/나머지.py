# {dictionary}
# 중복X key와 value, index 지정 가능, 순ㅅ 유지 
# nums = dict()
# for _ in range(10) :
    
    # 1. 해당 key 가 딕셔너리에 있는지 조사
#    if t in nums : 
#        nums[t] = nums[t] + 1
#    else :
#        nums[t] = 1
    
    # 2. get() 사용
#     t = int(input())%42
#    nums[t] = nums.get(t,0)+1   
    # dict.get(key, default) ** 

# print(len(nums))  

# {set}
# 중복X key만, index 지정 불가, 순서 X  
# 각각의 카운트가 필요없는 서로 다른 나머지의 개수만 구하려면 key값만 중복 없이 존재하는 set 사용! 
mods = set()
for _ in range(10):
    t = int(input())%42 
    mods.add(t)
    
print(len(mods))  