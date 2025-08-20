def check_hap(com):
    # (['SQUARE', 'YELLOW', 'GRAY'], ['SQUARE', 'BLUE', 'GRAY'], ['TRIANGLE', 'BLUE', 'WHITE'])
    shape = set()
    color = set()
    back = set()

    for i in range(3):
        shape.add(com[i][0])
        color.add(com[i][1])
        back.add(com[i][2])

    if len(shape) == 2 or len(color) == 2 or len(back) == 2:
        return False
    else:
        return True


# 1. 카드 입력 받기
cards = [list(input().split()) for _ in range(9)]

# 2. 조합 구하기
from itertools import combinations
combs = combinations(cards, 3)

# 3. 합인 조합만 모아두기
haps = []
for com in combs:
    if check_hap(com):
        haps.append(list(com))

# 4. Command 실행하기
K = int(input())
ANS = 0
flag = True
for _ in range(K):
    order = input()
    if order[0] == 'H' :
        order = order.split()
        com = order[0]
        fst, scd, trd = sorted([int(order[1]), int(order[2]), int(order[3])])

        comb = [cards[fst-1]]+[cards[scd-1]]+[cards[trd-1]]
        if check_hap(comb) and comb in haps:
            haps.remove(comb)
            ANS += 1
        else:
            ANS -= 1
    elif order[0] == 'G':
        if not haps and flag:
            ANS += 3
            flag = False
        else:
            ANS -= 1
    # if ANS < 0:
    #     ANS = 0
print(ANS)
