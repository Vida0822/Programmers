SC = int(input()) # input() : error --> input() 으로 받으면 python 은 String으로 취급

if 90 <= SC and SC <= 100 : 
    print('A')
elif 80 <= SC and SC < 90 : 
    print('B')
elif 70 <= SC and SC < 80 : 
    print('C')
elif 60 <= SC and SC < 70 : 
    print('D')
else : 
    print('F')