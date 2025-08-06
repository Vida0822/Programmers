T = int(input())
 
for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
 
    # Sliding Window 알고리즘
    sum_v = max_v = min_v = sum(lst[:M])
    for i in range(1, N-M+1):
        sum_v = sum_v -lst[i-1] + lst[i+M-1] # 0 빼고 4 더하고
 
        max_v = max(max_v, sum_v)
        min_v = min(min_v, sum_v)
 
    print(f'#{t} {max_v-min_v}')