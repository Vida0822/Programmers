for T in range(1, 11):
    r = int(input())
    buildings = list(map(int, input().split()))
 
    # O(RxN)  : N x R <= 100 x 1000
    for i in range(r): # O(R) 
        M, m = max(buildings) , min(buildings) # O(2N)
        if M - m <= 1:
            break
        M_idx = buildings.index(M)  # O(N)
        m_idx = buildings.index(m)  # O(N)
 
        buildings[M_idx] -= 1 
        buildings[m_idx] += 1
 
    print(f'#{T} {max(buildings) - min(buildings)}')