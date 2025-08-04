"""
풀이 시간 : 10분 (구상 5분, 구현 5분)
- 가장 위에있는 그릇과 같다면 굳이 접시를 넣지 않고 시간만 계산한다.
- 다르면 그릇을 넣는다.

=> O(N) 
"""
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

