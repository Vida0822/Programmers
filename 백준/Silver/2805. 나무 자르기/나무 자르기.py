def cut(m, H):
    sm = 0
    for h in H:
        if h > m :
            sm += (h-m)
    return sm

N, M = map(int, input().split())
H = list(map(int, input().split()))
# H.sort() --> 정렬 필요 없음 : 탐색 대상이 나무 배열 자체가 아닌 자르는 상한선이기 때문

# 이진탐색
s, e, ans = 0, max(H), 0
while s <= e:
    m = (s+e)//2

    if M <= cut(m, H):
        ans = m
        s = m+1
    else:
        e = m-1

print(ans)