N = int(input())
lst = [i for i in range(1, N+1)]
cards = list(map(int, input().split()))

for i in range(1, N):
    card = cards[i]
    lst.insert(i-card, lst.pop(i))

print(*lst)
