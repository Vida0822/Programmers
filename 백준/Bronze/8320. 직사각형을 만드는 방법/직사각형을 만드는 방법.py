n = int(input())

count = 0
for i in range(1, n+1) :
    for w in range(1, i+1) :
        h = i//w
        if i%w == 0 and w >= h:
            count += 1

print(count)