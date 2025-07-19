while True : 
    s = input() 
    if s =='.' : 
        break 
        
    stack = []
    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')' : 
            if not stack or stack[-1] != '(' : 
                stack.append('no') 
                break 
            stack.pop()
        elif c == ']' : 
            if not stack or stack[-1] != '[' : 
                stack.append('no') 
                break 
            stack.pop()
    
    print('yes' if not stack else 'no' )
