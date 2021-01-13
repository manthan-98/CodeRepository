import random
print('''
Welcome
you have to guess a number between 1 to 10
you have 2 chances''')
answer = random.randint(1,10)
if answer <= 5:
    print('Hint 💡 : Number is less than 6')
    guess = int(input('guess a number between 0 and 5\n>'))
else:
    print('Hint 💡 : Number is greater than 5')
    guess = int(input('guess a number between 6 and 10\n>'))
if answer == guess:
    print('Correct guess')
elif answer%2 == 0:
    print('Hint 💡 : it is a even number')
    guess = int(input('>'))
    if guess == answer:
        print('correct guess')
    else:
        print('you lost')
        print(f'The answer is {answer}')
else:
    print('Hint 💡 : it is a odd number')
    guess = int(input('>'))
    if guess == answer:
        print('YOU WON')
    else:
        print('YOU LOST')
        print(f'The number is {answer}')