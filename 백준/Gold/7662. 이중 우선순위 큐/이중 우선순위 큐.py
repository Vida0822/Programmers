from heapq import heappush, heappop

TC = int(input())
for i in range(TC):
    K = int(input())
    h_min = []
    h_max = []
    cnt = {}
    for _ in range(K):
        com, val = input().split()
        val = int(val)

        if com == 'I':
            heappush(h_min, val)
            heappush(h_max, -val)
            cnt[val] = cnt.get(val, 0) + 1
        else:
            if val == -1 :
                while h_min:
                    v = heappop(h_min)
                    if v in cnt and cnt[v] > 0 : # 이 조건때문에 음수값은 되지 않음
                        cnt[v] -= 1
                        break
            else:
                while h_max:
                    v = -heappop(h_max)
                    if v in cnt and cnt[v] > 0:
                        cnt[v] -= 1
                        break

    # 유효X 값 제거 (bad code..시간초과될수도..?)
    while h_min and (cnt[h_min[0]] == 0):
        heappop(h_min)
    while h_max and (cnt[-h_max[0]] == 0):
        heappop(h_max)

    if h_max and h_min  :
        ans_max, ans_min = -heappop(h_max), heappop(h_min)
        if ans_max - ans_min >= 0:
            print(ans_max, ans_min)
        else :
            print('EMPTY')
    else:
        print('EMPTY')
