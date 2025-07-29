N = int(input())
# set 활용
A = {*map(int, input().split())}  # '*' 안붙이면 그냥 map의 주소가 나옴

M = int(input())
# B = [list(map(int, input().split()))] --> 리스트를 한번 더 묶은거임 : list(), []
B = list(map(int, input().split()))

for b in B :
    if b in A :
        print(1)
    else :
        print(0)


