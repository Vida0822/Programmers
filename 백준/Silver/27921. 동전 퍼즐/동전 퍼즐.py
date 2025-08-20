H1, W1 = map(int, input().split())
BF = [list(input()) for _ in range(H1)]
H2, W2 = map(int, input().split())
AF = [list(input()) for _ in range(H2)]

coin = 0
for a in AF :
 #   print(a.count('0'))
    coin += a.count('O')
# print(coin)

mx = 0
for ci in range(-H1, H2+H1):
    for cj in range(-W1, W2+W1):
        cnt = 0
        for di in range(H1):
            for dj in range(W1):
                ni, nj = ci+di, cj+dj

                if not (0 <= ni < H2 and 0 <= nj < W2):
                    continue
                if BF[di][dj] == AF[ni][nj] and AF[ni][nj] == 'O':
                    cnt += 1
        mx = max(mx, cnt)
        # print(mx)
print(coin-mx)