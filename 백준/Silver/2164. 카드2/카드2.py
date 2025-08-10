
# 1차 시도 : 일반 Queue 사용 --> 시간초과
# N = int(input())
# q = [i for i in range(1, N+1)]

# while len(q) > 1:
#     q.pop(0)  # 리스트 -> 남은 모든 요소를 앞으로 한칸씩 당겨야함 : O(N)
#     q.append(q.pop(0))  # O(N)  => O(N^2) 

# print(q.pop())

# 2차 시도 : deque 사용  --> 통과 
from collections import deque

N = int(input())
q = deque([i for i in range(1, N+1)]) # O(N)

while len(q) > 1 : 
    q.popleft()   #  O(1) : 내부적으로 이중 연결리스트기에 특정 요소의 삽입, 삭제가 다른 요소에 영향을 주지 X 
    q.append(q.popleft()) # O(N)

print(q.pop())