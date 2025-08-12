"""
접근
: 이용시간이 짧은 화물차부터 배치한다.
"""

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    A = []
    for _ in range(N):
        s, e = map(int, input().split())
        A.append((s, e, e-s))

    # 1. 정렬
    A.sort(key=lambda a:a[2])

    # 2. 하나씩 읽으면서 배치 가능하면 배치
    v = [0]*24
    ANS = 0
    for a in A :
        s, e, t = a
        if v[s:e] == [0]*(e-s) :
            ANS += 1
            v[s:e] = [1]*(e-s)

    # 3. 정답 출력
    print(f'#{tc} {ANS}')