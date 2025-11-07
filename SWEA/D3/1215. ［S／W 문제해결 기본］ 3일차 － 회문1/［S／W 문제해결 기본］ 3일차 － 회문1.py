T = 10
for t in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(8)]
 
    res = 0
    for i in range(8) :
        for j in range(8) :
 
            # 가로
            if j+N <= 8:
                # word =[arr[i][j:j+N]]  --> for문 대신
                for k in range(N//2) :
                    if arr[i][j+k] != arr[i][j+N-k-1]:
                        break
                else:
                    res += 1
 
 
            # 세로
            if i+N <= 8:
                # word = [arr[i + k][j] for k in range(N)] --> for문 대신 (행의 특정열만 가져오는 함수 기억**) 
                for k in range(N//2) :
                    if arr[i+k][j] != arr[i+N-k-1][j]:
                        break
                else:
                    res += 1
 
    print(f'#{t} {res}')