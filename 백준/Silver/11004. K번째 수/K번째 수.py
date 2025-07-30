"""
풀이 시간 : 1분 
"""
N , K = map(int, input().split())
A = sorted(list(map(int, input().split())))

print(A[K-1])
