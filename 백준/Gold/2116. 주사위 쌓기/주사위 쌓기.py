def score(dice, d_idx, u_idx):
    scr = 0
    for j in range(0, 6):  # idx
        if j in (d_idx, u_idx):
            continue
        scr = max(scr, dice[j])
    return scr

def nxt(d_idx, u_idx):
    scr = 0
    for i in range(1, len(dices)):
        # 이전 주사위의 위에 적한 번호 있는 인덱스 찾기
        dice = dices[i]
        d_idx = dice.index(dices[i-1][u_idx])
        u_idx = other[d_idx]

        scr += score(dice, d_idx, u_idx)
    return scr


K = int(input())
dices = []
for _ in range(K) :
    dices.append(list(map(int, input().split())))

ANS = 0
other = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}

for i in range(len(dices[0])):
    d_idx = i
    u_idx = other[i]

    scr = score(dices[0], d_idx, u_idx) + nxt(d_idx, u_idx)
    ANS = max(ANS, scr)

print(ANS)