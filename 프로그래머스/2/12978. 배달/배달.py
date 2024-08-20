import heapq

def solution(N, road, K):
    # 양방향 그래프 
    # 가중치 o 
    # 시작 노드 : 1
    # 각 노드 최단 거리들 중 K 이하 최단거리 가진 ㅏㅁ을 갯수 return 
    # road (a,b,c) : a에서 b까지 c 비용 소요 
    
    # 그래프 생성 
    graph = [[] for _ in range(N+1)]
    INF = 1000000
    # distances = [INF] * N+1 # Can only concatenate list (not "int") to list : 리스트 + int라서 생기는 에러 
    distances = [INF] * (N+1)
    
    for i in road : 
        graph[i[0]].append((i[2],i[1]))
        graph[i[1]].append((i[2],i[0])) # 양방향 그래프는 양쪽에 넣어줘야함!
    
    q = []
    distances[1] = 0
    heapq.heappush(q, (0,1))
    
    while q :
        dist, now = heapq.heappop(q)
        
        if distances[now] < dist : 
            continue 
        
        for next in graph[now] : 
            cost = dist + next[0]
            if cost < distances[next[1]] : 
                distances[next[1]] = cost
                heapq.heappush(q,(cost, next[1]))
    
    answer = 0
    for i in range(1, N+1) :
        print(distances[i])
        if distances[i] <= K : 
            answer += 1 
    return answer 