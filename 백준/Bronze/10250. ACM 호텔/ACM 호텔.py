T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    h = N % H if N%H!=0 else N%H+H
    w = N // H + 1 if N%H!=0 else N//H

    print(h, '%02d' % w, sep='')
