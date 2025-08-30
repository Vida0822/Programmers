'''
조건
- 3x3
- 1초당 연산

- R : N <= M
- C : M > M

'''


def sort_lst(lst):
    '''
    문제 규칙에 따라 리스트를 정렬하는 함수

    :param lst: 정렬할 행 또는 열
    :return: 정렬된 행 또는 열
    '''
    v = dict()
    for a in lst : # O(N)
        v[a] = v.get(a, 0)+1

    num_set = list(v.items())
    num_set.sort(key=lambda x: (x[1], x[0]))

    ret = []
    for n, c in num_set:
        if n == 0 :
            continue
        ret.extend((n, c))
    debug = 1
    return ret
    # print(num_set)



def rotate(new_A):
    '''
    C연산을 했을 때 행기준으로 채워준 배열을 좌 90도 돌리기
    :param new_A:
    :return:
    '''

    # 1행을 뽑아서 1열로 넣어주기
    rot_A = [[0]*M for _ in range(N)]
    for j in range(M):
        lst = new_A[j]
        for i in range(N):
            if i >= len(lst): # 아직 0을 안채워줬기 때문에 실제 N보다 더 작을 수 있다.
                rot_A[i][j] = 0
            else:
                rot_A[i][j] = lst[i]
    debug =1
    return rot_A

# [0] 시뮬 준비
r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
# A = [[1]*105 for _ in range(105)]
N, M = 3, 3

# for a in A:
#     print(*a)
# [1] 시뮬 실행
time = 0
while True:
    # 종료 조건
    if time > 100 : # 수정
        break
    if 0 <= r-1 < N and 0 <= c-1 < M and A[r-1][c-1] == k:
        break
    new_A = [] # 수정 염두

    # R 연산
    if N >= M :
        new_M = 0
        for i in range(N):
            # 0. 행 추출
            lst = A[i]

            # 1. 규칙 따라 정렬
            lst = sort_lst(lst)

            # 2. 정렬된 lst 모으고
            new_A.append(lst)

            # 3. N, M 값 갱신
            new_M = max(new_M, len(lst))
        M = min(new_M, 100)
    # C 연산
    else :
        new_N = 0
        for j in range(M) :

            # 0. 열 추출
            lst = []
            for i in range(N) :
                lst.append(A[i][j])

            # 1. 규칙 따라 정렬
            lst = sort_lst(lst)

            # 2. 정렬된 lst 알맞게 배치
            new_A.append(lst)

            # 3. N, M 값 갱신
            new_N = max(new_N, len(lst))

        # 4. 행<-> 열 치환
        N = min(new_N, 100)
        new_A = rotate(new_A)

    # 4. 새로운 A 배열 생성
    for i in range(N) :
        lst = new_A[i]
        if len(lst) < M :
            lst.extend([0]*(M-len(lst)))
    A = new_A
    time += 1

# [2] 시뮬 정답
print(time if time <= 100 else -1)