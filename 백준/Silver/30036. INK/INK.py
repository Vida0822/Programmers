def move(com, ci, cj) : 
    dirs = {'U':(-1, 0), 'D':(1, 0) , 'L':(0, -1) , 'R': (0, 1)}
    ni, nj = ci + dirs[com][0], cj + dirs[com][1]
    if 0 <= ni < N and 0 <= nj < N and adj[ni][nj] == '.':
        return ni, nj 
    else :
        return ci, cj

def charge(m) :
    return m+1

def jump(ci, cj, m, jp):
    L = len(INK_color)
    for di in range(-m, m+1) : 
        for dj in range(-m, m+1) :
            ni, nj = ci+di, cj+dj 
            if not (0 <= ni < N and 0 <= nj < N ): 
                continue 
            if abs(ci-ni) + abs(cj-nj) > m : 
                continue 
            if adj[ci+di][cj+dj] != '.' : 
                adj[ci+di][cj+dj] = INK_color[jp%L]
    
        
    
# 그래프 만들기 
I, N, K = map(int, input().split()) 
INK_color = input()
adj = [list(input()) for _ in range(N)] 

# 시작 위치 찾기 
for i in range(N):
    for j in range(N): 
        if adj[i][j] == '@' : 
            adj[i][j] = '.'
            ci, cj = i, j 


# 커맨드 실행하기 
m = 0
jp = 0 
command = input()
for com in command: 
    if com in ('U', 'D', 'L', 'R'): 
        ci, cj = move(com, ci, cj) 
    elif com == 'j' :
        m = charge(m)
    else :  # jump
        jump(ci, cj, m, jp)
        jp += 1
        m = 0 

# 최종 스테이지 출력 
adj[ci][cj] = '@'
for a in adj : 
    print(''.join(a)) 
    
    
        
    
        
    
