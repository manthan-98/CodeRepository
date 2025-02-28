import random
dice = random.randint(1,6)
print(dice)
i = 0
while i<1:
    roll = input('Do you like to roll the dice again\n For YES type Y\n For NO tpye N\n>').upper()
    if roll == 'Y':
        dice = random.randint(1, 6)
        print(dice)
    elif roll !='Y' and roll !='N':
        print('Not Valid')
    elif roll == 'N':
        break
    else:
        i += 1
        
