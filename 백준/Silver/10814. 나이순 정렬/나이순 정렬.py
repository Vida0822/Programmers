N = int(input())
lst = [tuple((i, *input().split())) for i in range(N)]
# for _ in range(N) :
#    t = enumerate(tuple(input().split()))  - enumerate() 안에는 반복가능한 iterable이 와야함

lst.sort(key=lambda x : (int(x[1]), x[0]))

for l in lst :
    print(l[1], l[2])