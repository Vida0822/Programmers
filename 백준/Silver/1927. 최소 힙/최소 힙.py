from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
hq = []

for n in lst :
    if n > 0 :
        heappush(hq, n)
    else:
        if hq :
            print(heappop(hq))
        else:
            print(0)
