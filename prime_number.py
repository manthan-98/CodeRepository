# Prime number
n = int(input('Write any number = '))
if n > 1:
    for m in range(2, n):
        if n % m == 0:
            print('not a prime')
            break
    else:
        print('prime')
else:
    print('not a prime')