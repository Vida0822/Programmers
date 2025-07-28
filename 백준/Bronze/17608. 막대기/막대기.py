N = int(input())

stack = []
for i in range(N) :
    num = int(input())
#    if stack and stack[-1] <= num :# 연속으로 작은 값이 나올경우 다 빼줘야하는데 한번만 뺌...
    while stack and stack[-1] <= num:
        stack.pop()
    stack.append(num)

print(len(stack))