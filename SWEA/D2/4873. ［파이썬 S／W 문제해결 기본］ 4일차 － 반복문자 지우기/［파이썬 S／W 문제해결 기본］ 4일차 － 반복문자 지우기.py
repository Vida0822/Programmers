import math

T = int(input())

for t in range(1, T+1):

    st = input()
    stack = []
    for s in st :
        if s in stack and s == stack[-1] :
            stack.pop()
        else :
            stack.append(s)

    print(f'#{t} {len(stack)}')
