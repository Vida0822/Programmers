N = int(input()) 

nums = []
for i in range(N) : 
    nums.append(int(input()))

# 1. Bubble sort : 이웃끼리 비교 --> O(N^2)

                
# 2. Selection Sort : 최소값을 찾고 맨앞으로 보내기 
for i in range(N-1) :
    mindex = i  
    for j in range(i, N) : 
        if nums[j] < nums[mindex] : 
            mindex = j 
    nums[i],nums[mindex] = nums[mindex],nums[i]     


# 3. Inserstion Sort

for n in nums : 
    print(n)