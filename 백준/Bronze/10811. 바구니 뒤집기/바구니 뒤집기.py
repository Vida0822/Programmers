N, M = map(int, input().split())
bags = [i for i in range(0, N+1)]

for _ in range(M): 
    i, j = map(int, input().split()) 
    
    # 슬라이싱 역순 
    # bags[i:j+1] = bags[i:j+1:-1]  --> 역순일 때는 start > end 여야함!! (뒤에서 앞으로 개념)
    # bags[i:j+1] = bags[j+1:i:-1] 
    bags[i:j+1] = bags[i:j+1][::-1]

print(*bags[1:])
   