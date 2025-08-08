def cut(m, H):
    sm = 0
    for h in H:
        if h > m :
            sm += (h-m)
    return sm

N, M = map(int, input().split())
H = list(map(int, input().split()))

# 이진탐색
H.sort() # 정렬,,,계속 까먹음 ㅠㅠ
s, e, ans = 0, H[-1], H[-1]
while s <= e:
    m = (s+e)//2

    if M <= cut(m, H):
        ans = m
        s = m+1
    else:
        e = m-1

print(ans)