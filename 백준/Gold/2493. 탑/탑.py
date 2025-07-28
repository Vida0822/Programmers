N = int(input())
lst = list(map(int, input().split()))
stack = []
ans = []
for i in range(N):
    while stack and stack[-1][1] < lst[i]:
        stack.pop()
    if not stack :
        ans.append(0)
    else :
        ans.append(stack[-1][0]+1)
    stack.append((i, lst[i]))
print(*ans)