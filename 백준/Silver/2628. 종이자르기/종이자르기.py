"""
풀이 시간 : 20분
- 구상 10분, 구현 5분, 디버깅 5분
- 종이를 자른다는 아이디어 자체가 코드로 구상하기 어려웠다 ㅠ

조건
- 종이조각 길이 1 ~ 100cm
- 세부 조각 길이 = abs(점선 번호 - 경계선)

접근
- 완전 탐색 : 경계선 간의 거리를 각각 구하고, 그 경계선 간의 모든 조합을 완전 탐색해 곱한 후 최대값 갱신
- 경계선 정보를 입력받고 정렬하는게 핵심
"""

N, M = map(int, input().split())
K = int(input())

# 1. 점선 정보 입력 받기
row = [0, M] # refactoring : 정렬할거기 때문에 처음부터 받아도 상관 X
col = [0, N]
for _ in range(K):
    ord, idx = map(int, input().split())
    if ord == 0:
        row.append(idx)
    else:
        col.append(idx)
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

