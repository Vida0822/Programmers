word = input().upper()
chars = dict()

max = 0 
for w in word : 
    w = w
    chars[w] = chars.get(w,0) + 1 
    
    if chars[w] > max : 
        max = chars[w]  

ans = list()
for key, val in chars.items() : 
    if val == max : 
        ans.append(key)
# for c in chars.items() :  --> indexing 도 가능! 
#    if c[1] == max : 
#         ans.append(c[0])

# 축약 
# ans = [k for k, v in chars.items() if v == max]


if len(ans) == 1 : 
    print(*ans)
else : 
    print('?')
    
# 축약 
# print(ans[0] if len(ans) == 1 else '?')
    
        
    
