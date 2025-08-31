"""
조건
- R  <= 10^9
 -> 무조건 O(R)

 접근 방법
 - 각 테두리를 1차원 리스트로 관리

"""

from collections import deque

def make_list(A) :
    '''
    2차원 배열의 각 테두리를 1차원 리스트로 변환하는 함수
    :param A: 돌리기 전 2차원 배열
    :return: list(queue)
    '''
    A_list = []
    for k in range(K):
        q = deque()
        # →
        for j in range(k, M - 1 - k):
            q.append(A[k][j])
        # ↓
        for i in range(k, N - 1 - k):
            q.append(A[i][M - k - 1])
        # ←
        for j in range(M - k - 1, k - 1, -1):
            q.append(A[N - k - 1][j])
        # ↑
        for i in range(N - k - 2, k, -1):
            q.append(A[i][k])
        A_list.append(q)
    return A_list

def make_array(A_list):
    '''
    회전한 1차원 리스트를 다시 array 형태로 변환하는 함수
    :param A_list: 회전한 1차원 리스트
    :return: 2차원 배열
    '''
    A_array = [[0]*M for _ in range(N)]
    for k in range(K) :
        q = A_list[k]
        t = 0
        # →
        for j in range(k, M-k):
            A_array[k][j] = q[t]
            t+=1
        debug = 3
        # ↓
        for i in range(k+1, N-k) :
            A_array[i][M-1-k] = q[t]
            t+=1
        debug = 4
        # ←
        for j in range(M-2-k, k-1, -1 ) :
            A_array[N-1-k][j] = q[t]
            t += 1
        debug = 5
        # ↑
        for i in range(N-2-k, k, -1) :
            A_array[i][k] = q[t]
            t += 1
        debug = 6

    return A_array

# [0] 준비
N, M, R = map(int, input().split())
A = [list(map(int ,input().split())) for _ in range(N)]
K = min(N, M) // 2

# 각각을 1차원 리스트로 만들기
A_list = make_list(A)
debug = 0

# [1] 실행 :
# 1. R번만큼 좌 90도
for q in A_list :
    L = len(q)
    r = R % L
    q.rotate(-r)
debug = 1

# 2. 다시 2차원 배열 형태로 변환
A_array = make_array(A_list)
debug = 2

# [2] 출력
for a in A_array:
    print(*a)
