def check():
    for lst in v[1:]:
        if lst[1:].count(0) >= 1:
            print(lst)
            return False
    else:
        return True


v = [[0]*7 for _ in range(7)] # 패딩

# 첫 시작점
sj, si = input()
si, sj = int(si), ord(sj) - ord('A')+1
v[si][sj] = 1

res = True
bi, bj = si, sj
for _ in range(35):
    cj, ci = input()
    ci, cj = int(ci),  ord(cj) - ord('A')+1

    di, dj = abs(bi-ci), abs(bj-cj)
    if v[ci][cj] or (di, dj) not in ((2, 1), (1, 2)) :
        res = False
        break

    v[ci][cj] = 1
    bi, bj = ci, cj

if res and check() and (si, sj) in ((ci+2, cj+1), (ci+1, cj+2),(ci-2, cj+1),(ci-1, cj+2),(ci+2, cj-1),(ci+1, cj-2),(ci-2, cj-1),(ci-1, cj-2)) :
    print('Valid')
else:
    print('Invalid')
#
# for vv in v:
#     print(*vv)
