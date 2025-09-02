import sys
input = sys.stdin.readline

def check():
    '''
    각 세로선의 j 좌표가 바뀌지 않고 모두 내려가는지 확인하는 함수

    :return: True/False
    '''
    for j in range(N): # O(N*H)
        cur = j

        for i in range(H):
            if cur > 0 and arr[i][cur-1]:
                cur -= 1
            elif arr[i][cur] :
                cur += 1
        if j != cur :
            return False
    return True



def dfs(n, si, sj):
    '''

    :param n: 지금까지 놓은 new 가로선 개수
    :param si, sj: 이전 검사 위치 (놓았을수도, 안놓았을수도 있음)
    :return: X -> ANS 값 갱신
    '''
    global ANS

    # 가지치기
    if n >= ANS or n > 3:
        return

    # [0] 종료 조건
    if check():
        if n < ANS :
            ANS = n
        return

    # [1] 재귀 호출
    for i in range(si, H):
        for j in range(N-1):
            if i == si and j < sj :
                continue
            if arr[i][j] or arr[i][j+1] :
                continue
            if j > 0 and arr[i][j-1]:
                continue
            arr[i][j] = 1
            dfs(n+1, i, j+2)
            arr[i][j] = 0


# [0] 준비
N, M, H = map(int, input().split())
arr = [[0]*N for _ in range(H)]
# arr[i][j] : j와 j+1열을 잇는 가로선 (오른쪽으로 나있다)
# 'b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다는 의미' --> 문제를 그대로 구현하자...

for _ in range(M):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1 # 기존에 있는 가로 사다리 :


# [1] 실행
# 1. 사다리 놓기
ANS = 4
dfs(0, 0, 0)

# [2] 정답
print(ANS if ANS < 4 else -1)
