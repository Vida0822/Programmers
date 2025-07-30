N = int(input())
A = set(map(int, input().split()))
X = int(input())

ans = 0
for a in A:
    b = X-a

    if a != b and  b in A:
        ans += 1

print(ans//2)