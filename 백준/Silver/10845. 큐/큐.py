n = int(input())
q = []

for _ in range(n):
    command = list(input().split())
    if command[0] == 'push':
        q.append(command[1])
    elif command[0] == 'pop':
        if len(q) > 0 :
            tmp = q.pop(0)
            print(tmp)
        else : print(-1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if len(q) > 0: print(0)
        else : print(1)
    elif command[0] == 'front':
        if len(q) > 0: print(q[0])
        else : print(-1)
    elif command[0] == 'back':
        if len(q) > 0: print(q[-1])
        else: print(-1)