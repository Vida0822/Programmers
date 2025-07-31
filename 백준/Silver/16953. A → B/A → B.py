
# 1. 초기 필요한 자료형 선언
A, B = map(int, input().split())
q = []
V = []

# 2. 시작
q.append((A, 0)) # data, depth,

# 2. 그래프 만들면서 탐색 (depth 자체가 최단 거리)
# depth_min = [[A]]
while q :
    data, depth = q.pop(0)

    # 종료 조건 1. B를 찾음
    if data == B :
        print(depth+1)
        break

    # 자식 노드 추가
    left, right = data * 2, int(str(data) + '1')
    if left <= B :
        q.append((left, depth + 1))
    if right <= B :
        q.append((right, depth + 1))

    # if len(depth_min) <= depth+1 :
    #     depth_min.append([B+1])
    # depth_min[depth+1][0] = min(left, depth_min[depth+1][0])

else:
    print(-1)
