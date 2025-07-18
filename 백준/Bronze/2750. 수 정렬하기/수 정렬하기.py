N = int(input()) 

nums = []
for i in range(N) : 
    nums.append(int(input()))

# Bubble sort : 이웃끼리 비교 
for i in range(N-1, 0 , -1) : 
    for j in range(i) : 
        if nums[j] > nums[j+1] : 
            nums[j], nums[j+1] = nums[j+1], nums[j]
            
for n in nums : 
    print(n)