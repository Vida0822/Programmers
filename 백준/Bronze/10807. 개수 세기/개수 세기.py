# python list() : 여러 데이터를 한번에 저장 가능 (동적, 정적 배열 모두 이거 사용)
# 순차 저장, 다른 종류 데이터, 인덱스 접근 
 
N = int(input()) 
nums = map(int, input().split())
v = int(input()) 

count = 0 
for num in nums :
    if num == v : 
        count += 1 
print(count)    