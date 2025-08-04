T = int(input())

for _ in range(T): 
    N = int(input())
    parent = [0]*(N+1) 

    # 각 노드의 부모 노드 저장 
    for _ in range(N-1):
        p, c = map(int, input().split())
        parent[c] = p 

    # 목표 노드 저장
    o1, o2 = map(int, input().split())
    o1_parents, o2_parents = [o1], [o2]
    
    # 목표 노드들의 조상 노드들 저장 (부모~root)
    while parent[o1]: # parent 배열 타고가는 형태의 문제 종종 나옴 --> root 노드 : 0
        o1_parents.append(parent[o1]) 
        o1 = parent[o1]

    while parent[o2]: 
        o2_parents.append(parent[o2])
        o2 = parent[o2]

    # 두 부모노드들의 레벨 
    o1_level = len(o1_parents)-1 
    o2_level = len(o2_parents)-1

    # 두 노드의 조상 노드가 다를 때까지 루트 노드에서 내려감 
    while o1_parents[o1_level] == o2_parents[o2_level]: # 다를 때까지 반복 
        o1_level-=1
        o2_level-=1 

    # 달라진다면, 이전 레벨의 노드가 공통 조상 노드
    print(o1_parents[o1_level+1])
        