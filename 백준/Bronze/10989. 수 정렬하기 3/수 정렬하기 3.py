import sys

N = int(sys.stdin.readline()) # input()보다 속도 up
memo = [0] * 10001

# lst = [int(input()) for _ in range(N)]
# for l in lst:
#    memo[l] += 1
for _ in range(N) :
    memo[int(sys.stdin.readline())] += 1 # 입력받는 즉시 개수 memo

for i in range(10001):
    if memo[i] != 0 :
        for j in range(memo[i]) : 
            print(i)

