H, M = map(int, input().split())
# 분기 point 1 : M에서 45를 뺀게 음수면 시간을 조정
# 분기 point 2 : H에서 1을 뺀게 음수면 23시로 조정
if M >= 45 : 
    # print(H+" "+(M-45)) : python은 int와 String간 직접 덧샘 허용 X (!= java)
    print(H, M-45)  # ***** python의 print()에서는 인자를 쉼표로 나열하면 자동으로 띄어쓰기******
else :
    if H < 1 : 
        print(23, 60+M-45)
    else :
        print(H-1, 60+M-45) 