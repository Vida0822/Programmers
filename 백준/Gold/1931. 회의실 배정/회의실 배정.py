N = int(input())
times = [tuple(map(int, input().split())) for _ in range(N)]
times.sort(key=lambda t: (t[1], t[0]))

ANS = 0
bf = -1
for s, e in times:
    if s < bf:
        continue
    else: # s >= bf
        ANS += 1
        bf = e
        # print(s,e)
print(ANS)

