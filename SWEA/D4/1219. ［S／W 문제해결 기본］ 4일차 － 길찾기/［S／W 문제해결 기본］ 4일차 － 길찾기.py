def dfs(c) :
    v[c] = 1 # 방문 표시를 dfs안에 들어가서 하고

    for n in (grp1[c], grp2[c]) :
        if n != -1 and v[n] == 0 : # 방문할 노드가 있고 방문한적이 없다면
            dfs(n)

T = 10
for _ in range(1, T+1) :
    t, E = map(int, input().split())
    # 그래프 만들기 (문제의 가이드를 따름) 
    grp1 = [-1]*101
    grp2 = [-1]*101

    lst = list(map(int, input().split()))
    s = lst[0]
    for i in range(1, len(lst)) :
        if i%2 != 0 :
            if grp1[s] == -1:
                grp1[s] = lst[i]
            else :
                grp2[s] = lst[i]
        else :
            s = lst[i]

    v = [0]*101
    dfs(0)

    print(f'#{t} {v[99]}')



