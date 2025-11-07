# 클래스를 그냥 list로
from collections import defaultdict
 
# 시작 ----------------------------------------
T = int(input())
delta = [(0, 1), (0, -1), (-1, 0), (1, 0)] # (조심) 상 하 좌 우, 시키는 대로
 
for test_case in range(1, T + 1):
 
    # 입력 --------------------------------
    N = int(input())                # 원자들의 수
 
    atom_dict = defaultdict(list)   # 원자의 위치-클래스
    for _ in range(N):
        x, y, d, K = map(int, input().split())
        atom_dict[(2*x, 2*y)].append([d, K]) #
 
    # 처리 --------------------------------------
    ans = 0
    for _ in range(2001*2): # 가장 멀리 떨어져 있던 애들이 만난 시간은 2000초. 좌상단, 우 하단에서 좌하단으로.
        # [1] 원자 이동
        new_atom_dict = defaultdict(list)
        for key in atom_dict:
            for d, k in atom_dict[key]:
                dx, dy = delta[d]
                new_atom_dict[(key[0] + dx, key[1] + dy)].append([d, k])  # 이동 후 새 arr에 자기 넣음
        atom_dict = new_atom_dict
 
        # [2] 원자 충돌
        for key in atom_dict:
            if len(atom_dict[key]) >= 2: # 충돌
                for d, k in atom_dict[key]:
                    ans += k # 에너지 방출 후 끝
                atom_dict[key] = [] # 없어짐
 
    print(f'#{test_case} {ans}')