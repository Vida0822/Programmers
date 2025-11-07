def solve(st) :
    stack = []
    for c in st:
        if c == '(' or c == '{' :
            stack.append(c)
        elif c == ')' :
            if stack and stack[-1] == '(' :
                stack.pop()
            else :
                return 0
        elif c == '}' :
            if stack and stack[-1] == '{' :
                stack.pop()
            else :
                return 0
            
    if not stack :
        return 1
    else :
        return 0

T = int(input())
for t in range(1, T+1):
    st = input()
    print(f'#{t} {solve(st)}')
