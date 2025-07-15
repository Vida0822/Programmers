nums = list() 
for _ in range(9) : 
    nums.append(int(input()))

# print(max_val=max(nums)) --> X : print() 안에서 대입 연산 불가 
# print(nums.find(max_val)) --> X : 리스트에는 find()없음! 대신 index()!!  

max_val = max(nums)
print(max_val)
print(nums.index(max_val)+1)