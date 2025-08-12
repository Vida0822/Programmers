from heapq import heappush, heappop

N = int(input())
lst = [int(input()) for _ in range(N)] # 입력을 반복문마다 받는 것보타 리스트에 모아 처리하는것이 유리
hq = []

for n in lst :
    if n != 0:
        heappush(hq, (n*(-1 if n < 0 else 1), n))
    else:
        if hq:
            print(heappop(hq)[1])
        else:
            print(0)
