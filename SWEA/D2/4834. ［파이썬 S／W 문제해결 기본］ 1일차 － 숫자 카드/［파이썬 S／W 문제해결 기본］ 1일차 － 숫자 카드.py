T = int(input())
 
for t in range(1, T+1):
    N = int(input())
    cards = input()
 
    result = (-1, -1)
    for j in range(0, 10):
        cnt = cards.count(str(j))
        if result[1] <= cnt:
            result = (j, cnt)
 
    print(f'#{t} {result[0]} {result[1]}')
