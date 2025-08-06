"""
구상 : 10분
"""
 
def solve() :
    arr = [list(map(int, input().split())) for _ in range(9)]
 
    rect = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
 
    for i in range(0, 9) :
 
        memo = [0] * 10
        r, c = 0, i
        while 0 <= r < 9 and 0 <= c < 9 :
            if memo[arr[r][c]] == 1 :
                return 0
            else:
                memo[arr[r][c]] += 1
            r += 1
 
        memo = [0] * 10
        r , c = i, 0
        while 0 <= r < 9 and 0 <= c < 9 :
            if memo[arr[r][c]] == 1 :
                return 0
            else:
                memo[arr[r][c]] += 1
            c += 1
 
        memo = [0] * 10
        for r in range(rect[i][0], rect[i][0]+3) :
            for c in range(rect[i][1], rect[i][1]+3) :
                if memo[arr[r][c]] == 1:
                    return 0
                else:
                    memo[arr[r][c]] = 1
               # ele = plane[3*(b//3)+r][3*(b%3)+c]
    else :
        return 1
 
T = int(input())
for t in range(1, T+1) :
    print(f'#{t} {solve()}')