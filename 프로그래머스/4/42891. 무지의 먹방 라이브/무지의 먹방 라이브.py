import heapq 
def solution(food_times, k):
    # k = 2,000,000 --> 매우 큰 숫자 : 선형 탐색 시 시간 초과 
    # 1. 가장 작은 남은 시간 가진 음식 pick 
    # 2. 해당 음식 남은 시간 * 남은 음식 갯수를 장애 시간에서 빼줌 
    # 3. 그 뺀 값이 0보다 작아지는 순간 남은 k를 음식갯수로 나눈 나머지 번째 음식 번호 --> 그 time에 먹을 음식 
    N = len(food_times)
    
    # 우선순위 큐 
    q = []
    for i in range(N) : 
        heapq.heappush(q, (food_times[i], i+1))

    turn = 0  
    while q:         
        now = q[0][0] - turn 
        if k-now*len(q) < 0 : 
            idx = k % len(q)
            result = sorted(q, key=lambda x: x[1])
            return result[idx][1]

        k -= now*len(q) 
        e = heapq.heappop(q) 
        turn += now
        
    return -1
