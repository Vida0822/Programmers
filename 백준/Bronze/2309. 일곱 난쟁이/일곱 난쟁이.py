kids = [int(input()) for _ in range(9)]
kids.sort()

# 9명의 키 총합 
sum_k = sum(kids)

# 포함되지 않는 2명을 구하고
flag = False
for i in range(0, 8) :

    # 경우를 찾으면 로직 종료
    if flag:
        break
    for j in range(i, 9) :
        
        # 만약 그 두명을 뺀 나머지가 100과 같으면 
        if sum_k - (kids[i]+kids[j]) == 100:
            
            # 남은 인원 출력
            for k in range(0, 9):
                if k != i and k != j:
                    print(kids[k])

            # 외부 반복문 탈출 위해 flag 변경
            flag = True
            break
#            print(kids[k] for k in range(0, 9) if k != i and k != j)
#           --> <generator object <genexpr> at 0x00000201EA76FED0>
#           반복문을 돌면서 나온 kids[k] 결과값들 --> generator 가 됨 --> 그대로 print시 주소 출력