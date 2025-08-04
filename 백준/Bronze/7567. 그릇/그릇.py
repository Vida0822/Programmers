S = input()
stack = []

ans = 0
for s in S:
    if not stack or s != stack[-1]:
        ans += 10
        stack.append(s)
    else:
        ans += 5

print(ans)

