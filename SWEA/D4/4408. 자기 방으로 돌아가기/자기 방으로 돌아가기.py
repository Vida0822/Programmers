import math

T = int(input())

for t in range(1, T+1):

    N = int(input())
    cnt = [0]*201 # 1~200열의 방문수를 표시  --> 해당 방문수 중 최대값이 총 방문수 (열방문수가 겹친 개수만큼은 group이 필요하기 때문)

    for i in range(N) :
        start, end = map(int, input().split())
        start, end = math.ceil(start/2), math.ceil(end/2) # 각 방번호에 대해 1~200열로 나눔

        # start < end
        if start <= end :
            for j in range(start, end+1) :
                cnt[j] += 1

        else : # start > end
            for j in range(start, end-1, -1) :
                cnt[j] += 1

    print(f'#{t} {max(cnt)}')