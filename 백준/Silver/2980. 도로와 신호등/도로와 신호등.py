N, L = map(int, input().split())
adj = [[] for _ in range(N)]

c = 0
t = 0
for i in range(N) :
    D, R, G = map(int, input().split())
    t += (D - c)
    if R >= t :
        t += (R-t)
    elif t > R :
        t += R-t%(R+G) if R-t%(R+G) > 0 else 0
    c = D
t += L-c

print(t)
