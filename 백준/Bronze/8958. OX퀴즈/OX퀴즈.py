T = int(input())

for _ in range(T):
    st = input()

    res = cnt = 0
    for s in st:
        if s =='X' : # and cnt != 0: --> 이렇게하면 문자가 'X'라도 cnt가 0인 경우 else 문으로 분기 -> cnt++
            res += sum([i for i in range(1, cnt+1)])
            cnt = 0
        else:
            cnt += 1
    else:
        res += sum([i for i in range(1, cnt + 1)])
    print(res)
