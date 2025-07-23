L, N = [int(input()) for _ in range(2)]

cakes = [0 for _ in range(L+1)]

res1 = (0, 0)
res2 = []
for i in range(1, N+1):
    start, end = map(int, input().split())

    if end-start > res1[1]:
        res1 = (i, end-start)

    count = 0
    for j in range(start, end+1) :
        if cakes[j] == 0:
            cakes[j] = i
            count += 1

    res2.append((i, count))

print(res1[0],  max(res2, key=lambda x: (x[1], -x[0]))[0], sep='\n')