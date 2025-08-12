from heapq import heappush, heappop

N = int(input())
lst = [int(input()) for _ in range(N)] # 입력을 반복문마다 받는 것보타 리스트에 모아 처리하는것이 유리
hq = []

for n in lst :
    if n > 0 :
        heappush(hq, -n) # 음수로 받으면 큰 값이 가장 작은 값이 되어 힙에 저장됨 
    else:
        if hq :
            print(-heappop(hq)) # 꺼내서 다시 양수 변환
        else:
            print(0)
