"""
괜히 효율성 높인다고 생략하지 말고,
O(N) 여러번으로 처리가능하면 나눠서 반복 계산 (실수 방지)
"""
import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort() # O(NlogN )

# 1. 산술평균
print(round(sum(lst)/N))

# 2. 중앙값
print(lst[N//2])

# 3. 최빈값

cnt_mx = 0
dic = dict()
for l in lst: # O(N)
    dic[l] = dic.get(l, 0)+1
mx = max(dic.values())
mx_dic = []
for i in dic:
    if mx==dic[i]:
        mx_dic.append(i)
print(mx_dic[1] if len(mx_dic) > 1 else mx_dic[0])

#4. 범위
print(max(lst)-min(lst))