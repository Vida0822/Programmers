"""
풀이 시간 : 10분 (구상 & 구현 : 5분, 디버깅 : 5분)

[구성]
1) set : 단어들이 중복되면 안되기 때문에 set에 받아줌
2) key : 해당 단어들을 길이순, 사전순으로 정렬 (lambda 이용)

[디버깅]
- 문제 또 제대로 안읽고... 중복 없다는 거 못봄 ㅠ
- set 자료형에는 sort() 없음 --> sorted()로 받아주고 다뤄야함
"""

N = int(input())
A = {input() for _ in range(N)} # 중복 없이 단어 받아줌 
print(*sorted(A , key=lambda a : (len(a),a)), sep = '\n') # 1순위 : 길이, 2순위 : 사전으로 정렬