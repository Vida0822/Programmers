def solve() :
    N = int(input())
    find = [int(input()) for _ in range(N)]

    stack = []
    idx = 0
    ans = []
    for e in find:
        while not stack or stack[-1] < e:
            idx += 1
            stack.append(idx)
            ans.append('+')

        while stack and stack[-1] >= e:
            ans.append('-')
            if stack.pop() == e :
                break
        else :
            return []

    return ans

ans = solve()
print('\n'.join(ans) if ans else 'NO')

