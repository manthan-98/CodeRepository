num = int(input('Please enter a number\n>'))
for number in range(num+1):
    power = len(str(number))
    list1 = list(map(int,str(number)))
    k = 0
    for i in list1:
        k += i**power
    if k == number:
        print(f'{number} is amstrong')
    else:
        print(f'{number} is not amstrong')