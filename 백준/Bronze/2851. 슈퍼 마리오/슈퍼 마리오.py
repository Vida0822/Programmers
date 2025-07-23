# 최대한 100
mus = [int(input()) for _ in range(10)]

result = 0
for m in mus :
    if result + m > 100:
        result = result+m if 100-result >= (result+m)-100 else result
        break
    else:
        result += m

print(result)