"""
1차 시도 : 시간 초과
2차 시도 :  memo 사용 -> 통과 16688 ms
- memo[s] : s에서 출발했을 때 해킹할 수 있는 컴퓨터의 개수 (실제 요소가 아닌 개수만 반환하면 되니까)


"""
import sys
input = sys.stdin.readline
from collections import deque

def bfs(s) :
    # [0] 필요한 자료형 준비
    v = [0]*(N+1)
    cnt = 0
    q = deque()

    # [1] 시작 위치 반영
    v[s] = 1
    cnt += 1
    q.append(s)

    while q :
        c = q.popleft()

        for n in adj[c] :
            if v[n] == 0 :
                # if memo[n] != 0 :  # 해당 요소를 출발 요소로 이전 bfs에서 구한적이 있다면
                #     cnt += memo[n] # 방문 없이 해당 값 cnt에 반영
                #     # cnt += memo[s] # debug : s -> n
                #     continue
                # 없다면 인접 요소 정상 방문
                v[n] = 1
                cnt += 1
                q.append(n)

    # 결과를 memo에 저장
  #  memo[s] = cnt
    return cnt


# 1. 그래프 만들기
N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
# memo = [0]*(N+1)

for _ in range(M) :
    A, B = map(int, input().split())
    adj[B].append(A) # 단방향그래프

ans = [0]
cnt = 0
for i in range(1, N+1):
    # if memo[i] != 0 : # 이미 이전 bfs에서 구한 적이 있다면
    #     com = memo[i] # bfs 수행 X
    # else : # 없다면
    #     com = bfs(i) # 정상 탐색
    t = bfs(i)
    if cnt < t : # 최대 개수보다 구한 개수가 더 많다면
        ans = [i] # 최대값 & 컴퓨터 inx 갱신
        cnt = t
    elif cnt == t : # 같다면
        ans.append(i) # 답 배열에 추가

# print(*sorted(ans))
print(*ans)
