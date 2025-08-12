"""
강사님 코드
: dictionary 를 사용하지 않고 메뉴번호 최대개수만큼 리스트 생성 후 look up
"""

from heapq import heappush, heappop

N, M = map(int, input().split())
# [1] 우선순위큐(메뉴번호별) 생성 후 고객 번호 push

hq = [[] for _ in range(200_001)] # 메뉴 최대개수

# 1. 각 초밥 종류 별 원하는 손님 저장 (heapq) : 가장 작은 손님번호가 우선하게 됨
for i in range(N) :
    types = list(map(int, input().split()))
    for n in types[1:]:
        heappush(hq[n], i)  # 메뉴번호 n의 큐에 고객번호 i추가

# print(A)

# 2. 만들어진 초밥 종류별 1순위 손님 반환
lst = list(map(int, input().split()))
ANS = [0]*N
for menu in lst:
    if hq[menu]: # debug: index error (입력할때는 요소값이 있었더라도 pop한 후 빈 리스트가 되었을 수 있다)
        ANS[heappop(hq[menu])] += 1

print(*ANS)

