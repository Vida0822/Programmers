import math 

N = int(input()) 
lst = list(map(int, input().split()))
T, P = map(int, input().split())

#t_muk = 0
#for l in lst : 
#    t_muk += math.ceil(l/T)
#print(t_muk)
print(sum(math.ceil(l/T) for l in lst))
print(N//P, N%P)