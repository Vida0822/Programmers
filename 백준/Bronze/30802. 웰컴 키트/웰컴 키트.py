import math 

N = int(input()) 
lst = list(map(int, input().split()))
T, P = map(int, input().split())

#t_muk = 0
#for l in lst : 
#    t_muk += math.ceil(l/T)
#print(t_muk)

# math.ceil(): 가장 가까운 정수로 up (정수 그 자체인 경우 올림X)
#     ex. math.ceil(0) --> 0 
print(sum(math.ceil(l/T) for l in lst))
print(N//P, N%P)