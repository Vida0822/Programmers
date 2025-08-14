"""
1차 시도 : BFS => N < 5000 : 5000개의 수를 Queue에 넣으니 메모리 초과
2차 시도 : 그리디
"""

N = int(input())

for i in range(N//5, -1, -1):
    if (N-i*5)%3 == 0 :
        ANS = i+((N-i*5)//3)
        break
else:
    ANS = -1
print(ANS)
