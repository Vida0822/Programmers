
for k in range(3) :
    st = input()

    if st != 'Fizz' and st != 'Buzz' and st != 'FizzBuzz':
        i = int(st) + 3-k

    else :
        continue

if i%3==0 and i%5==0 :
    print('FizzBuzz')
elif i%3==0 :
    print('Fizz')
elif i%5==0 :
    print('Buzz')
else :
    print(i)


