def solve() :
    st = input()

    idx = -1
    sm = 0
    for i in range(len(st)-1) :
        if st[i] == '*' :
            idx = i
        elif i%2==0 :
            sm += int(st[i])
        else :
            sm += int(st[i])*3

    m = int(st[-1])
    for i in range(0, 10):
        if idx % 2 == 0 :
            res = (sm + i + m)%10
        else :
            res = (sm + 3*i + m )%10

        if res == 0 :
            return i

print(solve())