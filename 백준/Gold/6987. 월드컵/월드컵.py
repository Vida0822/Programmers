from itertools import combinations

def dfs(n, target) :

    # [0] 종료 조건
    if n == 15:
        # 정답 확인
        scr = []
        for i in range(6):
            scr.append(win_cnt[i])
            scr.append(same_cnt[i])
            scr.append(lose_cnt[i])

        if scr == target:
            ans[-1] = 1
        return

    # [1] 재귀 호출
    match = matches[n]
    a, b = match[0], match[1]

    # 가지치기
    # : 기자의 예측치와 대조...
    if win_cnt[a] + 1 <= target[a*3] and lose_cnt[b] + 1 <= target[b*3+2]:
        win_cnt[a] += 1
        lose_cnt[b] += 1
        dfs(n+1, target)
        win_cnt[a] -= 1
        lose_cnt[b] -= 1

    if win_cnt[b] + 1 <= target[b * 3] and lose_cnt[a] + 1 <= target[a * 3 + 2]:
        win_cnt[b] += 1
        lose_cnt[a] += 1
        dfs(n + 1, target)
        win_cnt[b] -= 1
        lose_cnt[a] -= 1

    if same_cnt[a] + 1 <= target[a*3+ 1 ] and same_cnt[b] + 1 <= target[b*3 + 1]:
        same_cnt[a] += 1
        same_cnt[b] += 1
        dfs(n+1, target)
        same_cnt[a] -= 1
        same_cnt[b] -= 1


res = [list(map(int, input().split())) for _ in range(4)]

matches = list(combinations(range(6), 2))
win_cnt = [0] * 6
lose_cnt = [0] * 6
same_cnt = [0] * 6

ans = []
for r in res:
    ans.append(0)
    dfs(0, r)

print(*ans)