N, K = map(int, input().split())
q = [str(i) for i in range(1, N+1)]

i = 0
L = len(q)
ans = []
"""
O(N) = O(1000): 한번 반복돌때마다 숫자하나씩 빼고, 그 숫자가 없어질때까지 반복 
=> 완탐은 비효율적 (특정 인덱스에서 i+K전까지 지나가서 i+K번째 pop) 
"""
while q :
    i = (i+(K-1))%L
    # 규칙성 발견 어렵, 변화하는 각 단계별 큐 양상 + 인덱스 같이 체크해야함 (다음에도 이런 손코딩하기)
    L -= 1
    ans.append(q.pop(i))
    # print(q.pop(i))

# Refactoring : join()
# print('<', end='')
# print(*ans, sep= ', ', end='')
# print('>', end='')
print('<'+', '.join(ans)+'>')




