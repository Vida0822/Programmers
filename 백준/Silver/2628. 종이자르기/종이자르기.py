"""
조건
- 종이조각 길이 1 ~ 100cm
- 세부 조각 길이 = abs(점선 번호 - 경계선)
"""
N, M = map(int, input().split())
K = int(input())

# 1. 점선 정보 입력 받기
row = [0]
col = [0]
for _ in range(K):
    ord, idx = map(int, input().split())
    if ord == 0:
        row.append(idx)
    else:
        col.append(idx)
row.append(M)
col.append(N)

row.sort()
col.sort()

ans = 0
# 2. 경계선 간의 거리 구하고
for i in range(len(row)-1):
    for j in range(len(col)-1):
        di = row[i+1] - row[i]
        dj = col[j+1] - col[j]

        # 3. 곱해서 넓이 구하기 -> 최대값 갱신
        ans = max(ans, di*dj)

# 4. 답 출력 
print(ans)

