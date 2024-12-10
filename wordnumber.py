user=int(input('Enter a value:  '))
for i in range(user+1):
    if i%20==0:
        print('TWIST')
    elif i%15==0:
        pass
    elif i%5==0:
        print('FIZZ')
    elif i%3==0:
        print('BUZZ')
    else:
        print(i)