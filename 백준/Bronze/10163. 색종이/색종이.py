N = int(input())

arr = [[-1]*1002 for _ in range(1002)] # O(1000^2)
count = [0]*(N+1) # Memoization

# Brute Force
# O(N) x O(1000^2) = 100000000 (1억)
for i in range(1, N+1):
    x1, y1, dx, dy = map(int, input().split()) # (1,4) +3, +5

    for x in range(x1, x1+dx) :
        for y in range(y1, y1+dy) :
            if arr[x][y] != -1 :  # 이미 색종이가 놓여져 있었다면
                count[arr[x][y]] -= 1  # 이전 색종이는 덮이므로 개수 -1
            arr[x][y] = i # 색종이 덮고
            count[i] += 1 # 새로운 색종이 번호 write

for cnt in count[1:]:
    print(cnt)
