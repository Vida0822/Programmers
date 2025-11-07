def make_square(si, sj, d1, d2, arr):
    '''
    마름모 만드는 함수
    :param si, sj: 마름모 시작점 (맨 위점)
    :param d1, d2: 각 왼, 오른변 갈 범위
    :return: 포함된 디저트 개수
    '''
    types = set()
    types.add(arr[si][sj])
    test = [[0]*len(arr) for _ in range(len(arr))]
    test[si][sj] = 'M'
    ej = sj
    for i in range(si+1, si+d1+d2+1):
        if i <= si+d1 :
            sj -= 1
        else:
            sj += 1
        if i <= si+d2:
            ej += 1
        else:
            ej -= 1
        # print(i, ej)
        test[i][sj] = 'M'
        test[i][ej] = 'M'
        t1 = arr[i][sj]
        t2 = arr[i][ej]

        if i != si+d1+d2 and t1 == t2:
            return -1

        if t1 in types or t2 in types:
            return -1
        else:
            types.add(t1)
            types.add(t2)

    return len(types)


def solve():
    # [0]
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # [1]
    mx = -1
    for si in range(0, N-2):
        for sj in range(1, N-1):
            for d1 in range(1, N):
                if si+d1 > N-1 or sj-d1 < 0 :
                    continue
                for d2 in range(1, N):
                    if si+d1+d2 > N-1 or sj+d2 > N-1:
                        continue
                    debug = 0
                    ret = make_square(si, sj, d1, d2, arr)
                    if ret == -1 :
                        continue
                    mx = max(mx, ret)

    # [2] ANS
    return mx


TC = int(input())
for tc in range(1, TC+1):
    if tc == 3 :
        debug = 0
    ANS = solve()
    print(f'#{tc} {ANS}')