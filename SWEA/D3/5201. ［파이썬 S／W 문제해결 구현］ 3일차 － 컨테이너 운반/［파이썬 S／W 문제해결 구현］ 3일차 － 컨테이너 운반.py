"""
접근
: 무거운 짐일수록 최대한 적재용량이 큰 트럭에 싣는다
"""
 
TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
 
    W = sorted(list(map(int, input().split())), reverse=True)
    T = sorted(list(map(int, input().split())), reverse=True)
 
    ANS = 0
    nxt = 0
    test = []
    for i in range(min(N, M)):
        for j in range(nxt, M):
            if W[i] <= T[j]:
                ANS += W[i]
                nxt = j+1
                break
 
    print(f'#{tc} {ANS}')