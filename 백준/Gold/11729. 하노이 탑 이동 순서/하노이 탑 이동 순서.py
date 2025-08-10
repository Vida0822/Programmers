"""
느낀점 : '재귀함수==특정 기능을 하는 라이브러리 함수 임이 잘 느껴지는 문제 


재귀함수: hanoi(n, start, end, temp) 
-> 내부 동작을 생각하지말고, 기능 그 자체를 생각
: 1~n개의 원반을 시작점(start)에서 목표지점(end)으로 옮겨주는 함수 (중간기둥은 temp를 이용)

1. 원반이 한개면 
=> 바로 목표지점으로 옮겨준다
2. 원반이 여러개면 
    1) 내 위에 있는 애들을 중간 기둥으로 모두 옮겨준다 : 재귀호출 hanoi(n-1, start, temp, end)
        --> 어떻게 옮기는지는 생각 X, 그냥 호출하면 자동으로 옮겨주는 라이브러리 함수라고 생각! 
    2) 가장 밑에있는 나(n)을 바로 목표지점으로 옮겨준다 
    3) 중간 기둥으로 옮겼던 원반들을 목표지점을 옮겨준다 : 재귀호출 hanoi(n-1, temp, end, start)  
        --> 어떻게 옮기는지는 생각 X, 그냥 호출하면 자동으로 옮겨줌

"중간 기둥에 숫자가 작은<큰 원반 순으로 쌓이는건 걱정하지 않아도 돼? (재귀함수간 충돌 걱정)" 
--> 이미 재귀함수 자체가 규칙에 맞게 start->end로 옮기는 함수 (크기순 지키면서)
--> 크기순 누적 보장됨
"""

cnt = 0 
ans = []
def doHanoi(n, start, end, temp) :
    global cnt
    
    # [0] 종료조건 
    if n ==1 : # 다 옮기고 원반이 하나 남았을 때  
        cnt += 1 
        ans.append((start, end)) 
        return 

    # [1] 재귀호출
    # 내 위의 원반 (n-1개) --> temp로 이동
    doHanoi(n-1, start, temp, end) 
    
    # 가장 아래에 있는 원반 --> end로 이동
    cnt += 1 
    ans.append((start, end))
    
    # 중간층에 있던 원반 --> end로 이동 
    doHanoi(n-1, temp, end, start)
    
    
N = int(input())

doHanoi(N, 1, 3, 2)

print(cnt)
for a in ans:
    print(*a)