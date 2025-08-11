
def check(num):
    for comm in command:
        ask, st, bl = comm
        ask = str(ask)
        # print(num, ask)

        for i in range(3):
            if ask[i] == num[i]:
                st -= 1
            elif ask[i] in num :
                bl -= 1
            # else :
            #     pass
        # print(st, bl)
        if not (st == 0 and bl == 0) :
            return False

    else:
        return True



def dfs(n, num):  # num : str
    global ANS

    # [0] 종료 조건
    if n == 3 :
        if check(num):
            ANS += 1
        return

    # [1] 재귀 호출
    for j in range(1, 10):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, num+str(j))
            v[j] = 0

N = int(input())
command = [list(map(int, input().split())) for _ in range(N)]

v = [0]*10
ANS = 0
dfs(0, '')
print(ANS)




