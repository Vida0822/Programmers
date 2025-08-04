def find_t(arr, t):
    for ci in range(5):
        for cj in range(5):
            if arr[ci][cj] == t:
                return ci, cj
    return -1, -1

def solve():
    arr = [list(map(int, input().split())) for _ in range(5)]

    cnt = 0
    for i in range(5):
        nums = list(map(int, input().split()))
        for j in range(5):
            ci, cj = find_t(arr, nums[j])
            arr[ci][cj] = -1

            for di in range(5):
                if arr[di][cj] != -1 :
                    break
            else :
                cnt += 1

            for dj in range(5):
                if arr[ci][dj] != -1 :
                    break
            else :
                cnt += 1

            if ci == cj :
                for d in range(5):
                    if arr[d][d] != -1 :
                        break
                else :
                    cnt += 1

            if ci == 4-cj :
                for d in range(5):
                    if arr[4-d][d] != -1 :
                        break
                else:
                    cnt += 1

            if cnt >= 3:
                return i*5+(j+1)

print(solve())



