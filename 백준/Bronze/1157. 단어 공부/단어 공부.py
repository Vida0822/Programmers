word = input()
chars = dict()

max = 0 
for w in word : 
    w = w.upper()
    chars[w] = chars.get(w,0) + 1 
    
    if chars[w] > max : 
        max = chars[w]  

ans = list()
for key, val in chars.items() : 
    if val == max : 
        ans.append(key)

if len(ans) == 1 : 
    print(*ans)
else : 
    print('?')
        
        
    
