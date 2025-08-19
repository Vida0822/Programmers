N, r, c = map(int, input().split())

def recur(n, r, c): # r행 c열까지의 cnt 를 구하는 함수 (재귀함수는 이렇게 기능 써놓고 시작)

    # [0] 종료 조건
    if n == 0:
        return 0

    # [1] 재귀 호출
    return 2*(r%2)+c%2 + 4*recur(n-1, r//2, c//2)

print(recur(N, r, c))