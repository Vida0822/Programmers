words = [[0]*15 for _ in range(5)]

for i in range(5): 
    word = input() 
    for j in range(len(word)) : 
        words[i][j] = word[j] 
    
for i in range(15) :
    flag = False 
    for j in range(5) : 
        if words[j][i] != 0 : 
            print(words[j][i], end='') 
            flag = True              
    if not flag : 
        break     
    
    
    

    