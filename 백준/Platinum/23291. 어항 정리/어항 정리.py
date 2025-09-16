# [0]
N, K = map(int, input().split())
arr = list(map(int, input().split()))
# 순차적으로 단계가 진행되기 때문에 굳이 1차원, 2차원 형태에 따라 변수 다르게 쓰지 말고 이걸로 계속 처리해도 괜찮
# (근데 헷갈리긴 할듯? 그냥 이런 방법이 있구나~만 알고 넘어가기)

# [1]
def adjust(arr):
    '''
    인접한 두 어항의 값 차이를 조정
    :param arr:
    :return:
    '''

    # 전형적인 크기가 각 depth 별 크기가 다른 배열에 대한 완전탐색 기법! 알고가자!!
    # => for 문 범위 & oob 체크 부분
    narr = [x[:] for x in arr]  # '동시에 발생하는 진행이다': narr 필요
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # 인접 4방향, 범위내, ***** 값이 큰 경우 진행 (i, j > ni, nj) *****
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
                ni, nj = i+di, j+dj
                if 0 <= ni < len(arr) and 0 <= nj < len(arr[ni]) and arr[i][j] > arr[ni][nj]:
                    d = (arr[i][j] - arr[ni][nj])//5 # 체크는 arr에서
                    if d > 0 :
                        narr[i][j] -= d  # 반영은 narr 에
                        narr[ni][nj] += d
    return narr


def flatten(arr):
    narr = []
    for j in range(len(arr[-1])) :  # 가장 긴 아래행(-1) 길이만큼 j 조회
        for i in range(len(arr)-1, -1, -1):
            if j < len(arr[i]) :  # 존재하는 범위내라면
                narr.append(arr[i][j])
    return narr


ANS = 0
while max(arr)-min(arr) > K : # 간단한 종료 조건은 그냥 while문 조건으로 넣어도 괜찮!
    # [1] 가장 적은 어항들에 물고기 한마리 추가
    mn = min(arr)
    for i in range(len(arr)):
        if arr[i] == mn:
            arr[i] += 1


    # [2] 공중부양 1: 2개 이상 쌓인 부양 후 시계방향 90도 회전
    #       => 올리는건 new 행으로 앞에 넣어주고, 기존에 있던 건 아래 행으로 넣어주기

    # 1. 일단 첫칸에 하나 쌓은 2차원 리스트 만들어주기
    arr = [[arr[0]]] + [arr[1:]]
    while True :
        # 2. 새로 쌓아야하는 부분 폭 구해서 잘라오기
        w = len(arr[-2])  # 바닥 바로 위의 칸, 즉 세로로 2칸 이상 쌓인 칸의 폭
        arr1 = [lst[:w] for lst in arr] # 그 폭만큼 arr에서 추출

        # 종료 조건 : 올릴게 밑변보다 더 짧아서 더 이상 올릴 수 없음
        if len(arr) > len(arr[-1])-w: # len(arr): 높이 vs len(arr[-1])-w = 밑변-윗변(높이 2이상인 칸 수)
            break

        # 3. 회전 하기
        # arr2 = list(map(list, zip(*arr1)))[::-1] # 미친 지금까지 시계/반시계 회전 리스트 슬라이싱 반대로 알고 있었음 ㄷㄷ
        arr2 = list(map(list, zip(*arr1[::-1])))# 시계 방향 90도? : 전치행렬을 만들고 '행' 역조회

        # 3. 합치기
        arr = arr2 + [arr[-1][w:]]
    debug = 1

    # [3] 물고기 수 조절
    narr = adjust(arr)
    debug = 2

    # [4] 평탄화 : 왼쪽바닥부터 위로 순서대로 바닥에 놓기
    arr = flatten(narr)
    debug = 3

    # [5] 공중 부양 2 x 2번
    M = len(arr)//2
    narr = [arr[:M][::-1]]+[arr[M:]]

    M = M//2
    arr1 = [lst[:M] for lst in narr]   # 왼쪽절반 공중 부양
    arr = [lst[::-1] for lst in arr1[::-1]] # 180도 회전 = 상하반전+좌우반전
    arr += [lst[M:] for lst in narr]

    # [6] 물고기 수 조절 + 평탄화
    narr = adjust(arr)
    arr = flatten(narr)
    
    # 정답 처리
    ANS += 1


# [2]
print(ANS)