TC = int(input())


def put(lst, v):
    '''
    행/역행 단위로 경사로 설치 시도하는 함수

    :param arr: 경사로 설치할 행
    :return:
    - boolean / 높이차이가 나지만 경사로를 설치해 활주로 설치 조건 만족 여부
    '''

    h = lst[0]
    x = 1
    for j in range(1, N):
        if h == lst[j]:
            x += 1
        elif h > lst[j]:
            h = lst[j]
            x = 1
            continue  # 반대 방향에서 검사
        elif h < lst[j]:
            # 조건 확인
            if lst[j] - h > 1:
                return False
            if x < X:
                return False
            # 슬라이싱 디버깅....
            # if lst[j-1-X:j-1] != [0]*X: # DEBUG!!! map이랑 v배열 계속 헷갈림
            # if v[j-1-X:j-1] != 0: # DEBUG!!! map이랑 v배열 계속 헷갈림
            debug = 1
            # for jj in range(j - 1, j - X - 1, -1):
            #     if v[jj] == 1:
            #         return False
            #     v[jj] = 1
            # v[j-X:j-1] = [1] * X -> DEBUG!! 계속 v 배열 길이가 1씩 늘어난다..왜지?
            # => 슬라이싱은 :v 값 '전(-1)'까지 포함!!!
            
            if v[j-X:j] != [0]*X:
                return False
            v[j-X:j] = [1]*X
            h = lst[j]
            x = 1
    return True


for tc in range(1, TC + 1):
    ANS = 0
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    t_arr = list(map(list, zip(*arr)))
    debug = 0
    for i in range(N):
        # 행/역행
        lst = arr[i]
        v = [0] * N
        if put(lst, v) and put(lst[::-1], v[::-1]):
            ANS += 1

        # 열/ 역렬
        lst = t_arr[i]
        v = [0] * N
        if put(lst, v) and put(lst[::-1], v[::-1]):
            ANS += 1

    print(f'#{tc} {ANS}')