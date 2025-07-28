mandart = [input().split() for _ in range(9)]

drs = [-1, 1, 0, 0, 1, 1, -1, -1]
dcs = [0, 0, 1, -1, 1, -1, 1, -1]


mid_goals = [(1, 1), (1, 4), (1, 7),
            (4, 1), (4, 7),
            (7, 1), (7, 4), (7, 7)]


mapping = {}

for r, c in mid_goals:
    k = mandart[r][c]
    mapping[k] = []
    for i in range(8):
        nr, nc = r + drs[i], c + dcs[i]
        mapping[k].append(mandart[nr][nc])

for i, k in enumerate(sorted(mapping.keys()), start=1):
    print(f'#{i}. {k}')

    mapping[k].sort()
    for j in range(1, 9):
        print(f'#{i}-{j}. {mapping[k][j-1]}')