def preord(c):
    if c in tree:
        return c+preord(tree[c][0])+preord(tree[c][1])
    else:
        return ''

def inord(c):
    if c in tree:
        return inord(tree[c][0])+c+inord(tree[c][1])
    else:
        return ''

def postord(c):
    if c in tree:
        return postord(tree[c][0])+postord(tree[c][1])+c
    else:
        return ''


# 1. 트리 만들기
N = int(input())
tree = {}

for i in range(1, N+1):
    inpt = input().split()
    tree[inpt[0]] = []
    tree[inpt[0]].append(inpt[1] if inpt[1] != '.' else '')
    tree[inpt[0]].append(inpt[2] if inpt[2] != '.' else '')

# 2. 순회 및 출력하기
s = list(tree.keys())
print(preord(s[0]))
print(inord(s[0]))
print(postord(s[0]))
