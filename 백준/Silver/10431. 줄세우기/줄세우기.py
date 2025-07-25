T = int(input())

for t in range(1, T+1):
    stu = list(map(int, input().split()))
    N = stu.pop(0)

    res = 0
    for i in range(len(stu)-1):
        for j in range(i+1,len(stu)) :
            if stu[i] > stu[j] :
                stu[i] , stu[j] = stu[j], stu[i]
                res += 1

    print(f'{t} {res}')


