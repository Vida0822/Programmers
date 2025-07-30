N = int(input())
A = {input() for _ in range(N)}
print(*sorted(A , key=lambda a : (len(a),a)), sep = '\n')