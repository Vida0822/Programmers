N = int(input())
A = list(map(int, input().split()))
# print(A)

stack = []
memo = [-1]*N
for i in range(N-1, -1, -1) :

    while stack:
        if A[i] < stack[-1]:
            memo[i] = stack[-1]
            stack.append(A[i])
            break
        else:
            stack.pop()
    else :
        stack.append(A[i])

print(*memo)
