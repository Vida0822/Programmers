def find(n) :
    if n != P[n]:
        P[n] = find(P[n])
    return P[n]

def union(a, b):
#        P[b] = find(P[a]) --> 디버깅 : b의 '대표자'의 부모를 a의 대표자로
    P[find(b)] = find(a)


# [0] parent 배열 준비
TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    P = [0]+[i for i in range(1, N+1)] # 자기 자신이 부모인 부모 배열

    # [1] 주문서 실행
    ords = list(map(int, input().split()))
    a = b = 0
    for i in range(M*2):
        if i%2 == 0:
            a = ords[i]
        else :
            b = ords[i]
            union(a, b)
            a = b = 0

    # [2] 정답 출력 : 그룹의 개수
    ans = 0
    # ans = set() # debug: 종료 시점에 P배열 각각이 루트 노드로 업데이트가 안되어있을 수 있다
    # print(P) # [0, 1, 2, 2, 7, 4, 4, 7] : 4번이 7번의 그룹으로 들어갔지만 그 자식들은 아직 변화 X (다음 조회에서 갱신됨)
    for i in range(1, N+1):
        if i == P[i] : # 부모가 자기 자신, 즉 루트인 노드개수가 그룹의 개수
            ans += 1

    print(f'#{tc} {ans}')


