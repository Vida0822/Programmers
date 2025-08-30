"""
조건
- 카드 : 1 ~ 2N

접근 방법
1. 2명이 N장씩
2. 교대로 카드 1장 제출  -> main
- 가진 것 중 가장 작은 것
- 놓쳐진 카드X -> 원하는 카드
- 카드O -> 마지막 카드보다 큰 숫자
- 낼 카드 X -> 상대 차례 넘어감 (카드 못냄)
3. 종료 : 카드 한쪽이라도 X
 -> 상대방 카드 수 = 내 점수 -> score()

[접근 방법]
- list -> 정렬

"""
from collections import deque

def find(top, cards):
    '''

    :param top: 가장 위에 있는 카드
    :param cards: A or B
    :return: top 보다 큰 카드의 인덱스 반환
    '''
    for i in range(len(cards)):
        if top < cards[i]:
            return i
    return -1

# [0] 준비
# O(N log N)
N = int(input())
A = sorted([int(input()) for _ in range(N)]) # 상근
B = sorted([b for b in range(1, 2*N+1) if b not in A])# 근상
turn_map = {0:A, 1:B}
# debug = 0

# [1] 실행
# O(N^2)
game = []
turn = 0
while True : # O(N^2) = O(10^4) : ok
    # 0. 종료 조건
    if not A or not B:
        ANS = (len(B), len(A))
        break

    # 1. 게임 진행
    # 놓여진 카드가 없다면
    cards = turn_map[turn] # A or B
    if not game:
        game.append(cards.pop(0))
        # debug = 1

    # 놓여진 카드가 있다면
    else:
        top = game[-1]
        card_idx = find(top, cards) # O(N)
        # 마지막 카드보다 크다면
        if card_idx >= 0 :
            game.append(cards.pop(card_idx))
            # debug = 2
        # 작다면
        else:
            game = []
            # debug = 3

    turn = (turn+1)%2


# [2] 정답
print(*ANS, sep='\n')

