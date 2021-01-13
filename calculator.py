a = int(input('a = '))
b = int(input('b = '))
c = input('operantion\n>')
if c =='+':
    answer = a+b
    print(f'{a}+{b} = {answer}')
elif c == '-':
    answer = a-b
    ans = b-a
    print(f'{a}-{b} = {answer} and\n {b}-{a} = {ans}')
elif c == '/':
    answer = a/b
    ans = b/a
    print(f'{a}/{b} = {answer} and\n {b}/{a} = {ans}')
elif c == '*':
    answer = a*b
    print(f'{a}*{b} = {answer}')
elif c == '%':
    answer = a%b
    ans = b%a
    print(f'{a}%{b} = {answer} and\n {b}%{a} = {ans}')
else:
    print('🤔‍')