"""
풀이 시간 : 10분 (구상 : 5분, 디버그 : 5분)

[구상]
N = 100000로 크기 때문에 O(N) 또는 O(N log N)의 로직 필요
=> set 사용 : A 가 서로 다른 자연수이기 때문에

1) A의 요소 중 a를 순차적으로 탐색하면서
2) 찾고자 하는 수 X에서 (X-a)를 구하면 합하면 X가 되는 자연수 쌍
3) X-a가 A에 있으면 자연수 쌍이 있는 것 --> cnt += 1
4) cnt // 2 : 중복 검사 (2번) 

"""
N = int(input())
A = set(map(int, input().split()))
X = int(input())

ans = 0
for a in A:
    b = X-a

    if a != b and b in A:
        ans += 1

print(ans//2)
