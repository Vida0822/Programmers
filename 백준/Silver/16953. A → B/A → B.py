"""
강사님 코드
"""
from collections import deque

def bfs(s, e) :
    q = deque() # 시간 up !
#    v = [0]*(e+1) -- > 메모리 초과
#    v = []  # 리스트 방문 표시(동적), 체크 O(N) --> 시간 초과
    v = set() # set 방문 표시, 체크 O(1)

    # 초기값
    q.append((s, 1))
    v.add(s) # set으로 방문 표시

    while q:
        c, dist = q.popleft()
        if c == e :
            return dist 

        for n in ((c*2, c*10+1)) :
            # 범위내 미방문 (조건)
            if n <= e and n not in v: # visited 확인 : O(N) => set 사용
                # v[n] = v[c]+1
                q.append((n, dist+1))
                v.add(n)
    else :
        return -1

A, B = map(int, input().split())
print(bfs(A, B))