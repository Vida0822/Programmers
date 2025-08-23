N, M = map(int, input().split())
A = {input() for _ in range(N)}
B = {input() for _ in range(M)}

# print(type(A.intersection(B))) # set
ans = sorted(A.intersection(B))
print(len(ans))
print(*ans, sep = '\n')
# 오호... set도 정렬이 되긴하네
# for a in A:  --> 얘도 됨!
#     print(a)
# for i in range(len(A)):  --> 얘는 안됨!
#     print(A[i])