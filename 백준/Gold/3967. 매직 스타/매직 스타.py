def check():
    test = []
    for line in lines:
        sm = 0
        for idx in line:
            sm += ord(alpha[idx]) - ord('A') + 1
        if sm != 26:
            return False
    else:
        return True

def dfs(n, cnt):
    global ans
    
    # 가지치기
    if l-n-cnt > len(not_used):
        return

    # [0] 종료 조건
    if n == 12:
        if check():
            ans = alpha[:]
        return

    # [1] 재귀 호출
    if alpha[n] != 'x':
        dfs(n + 1, cnt)
    else:
        als = sorted(not_used)
        for c in als:
            if ord(ans[n]) > ord(c):
                not_used.remove(c)
                alpha[n] = c
                dfs(n + 1, cnt + 1)
                not_used.add(c)
                alpha[n] = 'x'


# [0] 필요한 자료형
# 매직스타 요소가 위치한 좌표
stars = [(0, 4), (1, 1), (1, 3), (1, 5), (1, 7), (2, 2),
         (2, 6), (3, 1), (3, 3), (3, 5), (3, 7), (4, 4)]

# 검사할 라인
lines = [(0, 2, 5, 7), (0, 3, 6, 10), (7, 8, 9, 10),
         (1, 2, 3, 4), (1, 5, 8, 11), (4, 6, 9, 11)]

# 각 위치별 대입된 알파벳 (backtrack 대상)
alpha = ['x'] * 12

# 사용/사용X 알파벳
not_used = set(chr(i) for i in range(ord('A'), ord('L') + 1))

# ※ 코드 -> 문자 : str()가 아니라 chr()
# used = set()


# [1] 초기 상태
l = 12
arr = [list(input()) for _ in range(5)]
for k in range(12):
    i, j = stars[k]
    if arr[i][j] != 'x':
        alpha[k] = arr[i][j]
        not_used.remove(arr[i][j])
        l -= 1
        # used.add(arr[i][j])

# [2] Backtrack
ans = ['Z'] * 12
dfs(0, 0)

arr = [['.']*9 for _ in range(5)]
for k in range(len(stars)):
    i, j = stars[k]
    arr[i][j] = ans[k]

for a in arr :
    print(*a, sep='')
