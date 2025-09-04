N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0
for a in A: # O(10^7)
    ans += 1
    a -= B
    if a > 0 :
        ans += a//C
        if a % C != 0:
            ans += 1
print(ans)

# for i in range(5):
#     print(int((1000000-5)/7+0.5))