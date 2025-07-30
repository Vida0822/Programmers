"""
풀이 시간 : 15분 (구상&구현 : 5분, 디버깅 : 10분)

[구상]
완전 탐색 가능 (색종이 칠하기 : O(10x10x100) + 좌표 중 '1' count : O(100x100)
1) 색종이 칠하기  : si(입력2) ~ si+10 ,  sj(입력1)~sj+10
2) 개수 cnt : arr[i][j] == 1

=> refactoring : 개수를 색종이 칠하면서 count 가능

[디버깅]
좌표에 대입할 때 '=' 써야하는데 계속 '=='를 씀 ㅠ 
"""
N = int(input())

arr = [[0]*100 for _ in range(100)]
cnt = 0
for _ in range(N) :
    sj,  si = map(int, input().split())

    for i in range(si, si+10) : # si ~ si+9
        for j in range(sj, sj+10):
            if arr[i][j] == 0: # 만약 칠해져있지 않다면
#                arr[i][j] == 1 # 이거 계속 실수 ㅠㅠ
                arr[i][j] = 1 # 새롭게 칠하고
                cnt += 1 # 검은 영역 개수 count
print(cnt)



