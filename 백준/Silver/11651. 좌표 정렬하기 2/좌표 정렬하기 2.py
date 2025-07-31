N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
# print(lst)

# print(sorted(lst, key=lambda x, y : (y, x)))
# 'lambda x, y'의 의미 : 인자를 2개 받는 함수
#  ㄴ but lst에서 전달하는 요소는 (x,y)로 하나의 튜플임 (자동으로 언패킹X)
#  => 요소를 하나씩 받아 정렬하는 단일 인자함수여야함!!
lst.sort(key=lambda t : (t[1], t[0]))
for t in lst :
    print(t[0], t[1])