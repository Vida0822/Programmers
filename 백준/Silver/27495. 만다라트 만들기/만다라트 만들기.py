arr = [input().split() for _ in range(9)]

# O(3^2)
dic = {}
for i in range(3, 6):
    for j in range(3, 6):
        if i == 4 and j == 4 :
            continue
        dic[arr[i][j]] = []

# O(N^2*N log N)  --> O(N^3)
dir = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1), (1, -1), (1, 0), (1, 1) ]
for i in range(9) :
    for j in range(9) :

        if 3 <= i < 6 and 3 <= j < 6 :
            continue

        if arr[i][j] in dic :
            for dx, dy in dir :
                if 0 <= i+dx < 9 and 0 <= j+dy < 9:
                    dic[arr[i][j]].append(arr[i+dx][j+dy])
            dic[arr[i][j]] = sorted(dic[arr[i][j]])

# O(N log N)
# dic.sort() --> 파이썬은 sort() X => sorted 사용
dic = dict(sorted(dic.items(), key=lambda x : (x[0], x[1])))


k_idx = 1   # dictionary 에서는 dic[1] 식으로 인덱스 접근이 안된다
for key, value in dic.items() :
    print(f'#{k_idx}. {key}')

    v_idx = 1
    for v in value :
        print(f'#{k_idx}-{v_idx}. {v}')
        v_idx += 1
    k_idx += 1


