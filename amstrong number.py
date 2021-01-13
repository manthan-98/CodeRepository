num = input('Please enter a number\n>')
int_num = int(num)
power = len(num)
number = list(map(int,num))
k = 0
for i in number:
    k += i**power
if k == int_num:
        print('amstrong')
else:
    print('not amstrong')