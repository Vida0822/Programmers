K = int(input())

ans = []
for _ in range(K):
    ord = int(input())
    if ord == 0 :
        ans.pop()
    else:
        ans.append(ord)

if ans :
    print(sum(ans))
else:
    print(0)