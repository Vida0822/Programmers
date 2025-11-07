T = 10
for t in range(1, T+1):
    N, st = input().split()

    stack = []
    for c in st :
        if stack and c == stack[-1] :
            stack.pop()
        else:
            stack.append(c)

    res = ''.join(stack)
    print(f'#{t} {res}')