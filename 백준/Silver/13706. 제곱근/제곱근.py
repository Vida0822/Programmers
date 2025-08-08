N = int(input())

# [0] 탐색 범위 설정
s, e = 2, N//2
while s <= e:
    m = (s+e)//2

    if N == m**2:
        print(m)
        break
    elif N > m**2:
        s = m+1
    else :
        e = m-1
