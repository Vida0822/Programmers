for T in range(1, 11):
    L = int(input())
    buildings = list(map(int, input().split()))
 
    result = 0
    for i in range(2, L-2):
        h = buildings[i] - max(buildings[i-2:i]+buildings[i+1:i+3])
        result += h if h > 0 else 0
 
    print(f'#{T} {result}')