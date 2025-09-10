N, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
M = N//2

# [0] pos[] : 1차원 리스트에서 pos 참조하여 달팽이 읽기/쓰기
di, dj = [0, 1, 0, -1], [-1, 0, 1, 0]
cnt_mx, cnt, flag = 1, 0, 0
ci, cj, dr = M, M, 0
pos = []

for t in range(N*N-1):
    cnt += 1
    ci, cj = ci+di[dr], cj+dj[dr]
    pos.append((ci, cj))  # 2차원(달팽이) <-> 1차원
    if cnt == cnt_mx: # 방향 변경
        cnt = 0
        dr = (dr+1)%4
        if flag == 0:
            flag = 1
        else:
            flag = 0 # 두번에 한번씩 길이 증가
            cnt_mx += 1
debug = 0

# [1]
def bomb(lst):
    global ans
    nlst = []  # return
    lst.append(-1) # 패딩
    i = 0
    while i < len(lst)-1 :
        j = i+1
        while lst[i] == lst[j] :
            j += 1
        if 4 <= (j-i) : # 폭발
            ans += lst[i]*(j-i)  # 점수 추가
        else:
            nlst += [lst[i]]*(j-i) # 남은 구슬 리스트에 반영
        i = j
    lst.pop()
    return nlst

di  = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]
ans = 0
for _ in range(C) : # 명령 개수만큼 d, s
    d, s = map(int, input().split())

    # [1] d 방향으로 s만큼 뻗어가면서 arr을 0으로 변경
    for mul in range(1, s+1):
        arr[M+di[d]*mul][M+dj[d]*mul] = 0

    lst = []  # 0이 아닌 실제 구슬만 담기
    for (i, j) in pos:
        if arr[i][j] > 0:
            lst.append(arr[i][j])

    # [2] 연속 4개이상 폭발시키고, 더 이상 폭발하지 않을때까지 반복
    while True:
        tlst = bomb(lst) # 폭팔 후 나머지 반환
        if len(tlst) == len(lst) :  # 더 이상 폭발 X
            break
        lst = tlst

    # [3] 구슬을 개수+번호로 변환
    lst = [] # 변환시킨 구슬을 넣어줄 list
    tlst.append(-1)
    # 마지막 데이터 처리를 위해 패딩 추가 -> 연속값 check& 처리에서 유용
    #   : 마지막 연속 데이터들을 조건 분기 없이 처리해주고 싶을 때
    i = 0
    while i < len(tlst)-1:
        j = i+1
        while tlst[i] == tlst[j] : # 같은동안 증가
            j += 1
        lst += [(j-i), tlst[i]] # 개수 + 번호를 추가
        i = j

    # [3-2] 1차원 -> 2차원 배열에 복사
    arr = [[0]*N for _ in range(N)]  # 값이 지저분하게 남아있으므로 새로 만들기
    for i in range(0, min(len(pos), len(lst))): # 2차원 배열 최대 크기만큼만
        arr[pos[i][0]][pos[i][1]] = lst[i]

# [2]
print(ans)

