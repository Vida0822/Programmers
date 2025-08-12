"""
2. heapq로 활용 : 남는 컴퓨터있는지 순차탐색하는 부분 수정
"""

from heapq import heappush, heappop

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: x[0])

hq = [] # 사용 가능한 컴퓨터 번호
busy = [] # 사용중인 컴퓨터 : (끝나는시간, 컴퓨터번호) 
ans = [] # 각 컴퓨터의 사용 횟수

for s, e in lst:
    # print(hq)

    # [1] 반환 가능한 컴퓨터 있는지 확인
    while busy and busy[0][0] < s :
        heappush(hq, heappop(busy)[1])

    # [2] 컴퓨터가 있으면 반환
    if hq:
        com = heappop(hq)
        ans[com] += 1

    # [3] 컴퓨터가 없으면 추가
    else:
        com = len(ans)
        ans.append(1)

    heappush(busy, [e, com])

print(len(ans))
print(*ans)
