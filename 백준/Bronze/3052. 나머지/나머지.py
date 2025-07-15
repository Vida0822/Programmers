nums = dict()
for _ in range(10) :
    t = int(input())%42
    nums[t] = nums.get(t,0)+1   
    
print(len(nums))    