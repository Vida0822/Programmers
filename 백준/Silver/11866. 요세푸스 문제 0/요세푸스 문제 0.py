N, K = map(int, input().split())
q = [i for i in range(1, N+1)]

i = 0
L = len(q)
ans = []
while q :
    i = (i+(K-1))%L
    # 규칙성 발견 어렵, 변화하는 각 단계별 큐 양상 + 인덱스 같이 체크해야함 (다음에도 이런 손코딩하기)
    L -= 1
    ans.append(q.pop(i))
    # print(q.pop(i))

print('<', end='')
print(*ans, sep= ', ', end='')
print('>', end='')

