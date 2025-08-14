
# 1. 저장 --> O(N)
N = int(input())
lst = list(map(int, input().split()))
dic = dict()
for l in lst :
    dic[l] = dic.get(l, 0) + 1

# 2. 탐색 --> O(N)
M = int(input())
lst2 = list(map(int, input().split()))
ans = []
for i in range(M):
    targ = lst2[i]
    ans.append(dic.get(targ, 0))

print(*ans)

