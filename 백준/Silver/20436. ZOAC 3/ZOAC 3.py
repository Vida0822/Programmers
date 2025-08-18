# t = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
#         ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ' '],
#         ['z', 'x', 'c', 'v', 'b', 'n', 'm', ' ', ' ', ' ']]
keyb = {'q': (0, 0, 0), 'w': (0, 1, 0), 'e': (0, 2, 0), 'r': (0, 3, 0), 't': (0, 4, 0), 'y': (0, 5, 1), 'u': (0, 6, 1), 'i': (0, 7, 1), 'o': (0, 8, 1), 'p': (0, 9, 1),
       'a': (1, 0, 0), 's': (1, 1, 0), 'd': (1, 2, 0), 'f': (1, 3, 0), 'g': (1, 4, 0), 'h': (1, 5, 1), 'j': (1, 6, 1), 'k': (1, 7, 1), 'l': (1, 8, 1),
       'z': (2, 0, 0), 'x': (2, 1, 0), 'c': (2, 2, 0), 'v': (2, 3, 0), 'b': (2, 4, 1), 'n': (2, 5, 1), 'm': (2, 6, 1)
       }

# 시작점 찾기
left, right = input().split()
li, lj = keyb[left][0] , keyb[left][1],
ri, rj = keyb[right][0], keyb[right][1]

# 입력하기
command = input()
ans = 0
for c in command:
    ni, nj, nw = keyb[c]

    if nw == 0 : # 자음
        ans += (abs(ni-li)+abs(nj-lj)+1)
        li, lj = ni, nj
    else :
        ans += (abs(ni - ri) + abs(nj - rj) + 1)
        ri, rj = ni, nj

print(ans)
