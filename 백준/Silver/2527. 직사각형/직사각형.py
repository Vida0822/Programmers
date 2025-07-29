"""
구상 & 코드 : 40분
디버깅 : 50분 ㅠㅠ
"""
for _ in range(4) :
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    # 점
    if (p1==x2 and q1 == y2) or (p1 == x2 and y1 == q2) or (x1 == p2 and q1 == y2) or (x1 == p2 and q2 == y1) :
        print('c')
    # 선분
    elif (((p1 == x2 or x1 == p2) and (y1 <= q2 < q1 or y1 <= y2 < q1 or y2 <= y1 < q2 or y2 <= q1 <q2 ))
        or (y2 == q1 or y1 == q2) and (x1 <= x2 < p1 or x1 <= p2 < p1 or x2 <= x1 < p2  or x2 <= p1< p2 )):
        print('b')
    # 공통 X
    elif p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1 :
        print('d')
    else :
        print('a')