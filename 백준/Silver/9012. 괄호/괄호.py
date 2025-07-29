def solve():
    stk = []
    st = input()

    for s in st:
        if s == '(':
            stk.append('(')
        elif s == ')':
            if not stk:
                return False
            stk.pop()
    if stk:
        return False
    return True

T = int(input())
for _ in range(T) :
    print('YES' if solve() else 'NO')