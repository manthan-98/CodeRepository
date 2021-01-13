list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['g', 'h', 'i', 'j']
list1.extend(list2)
letter = input('type a letter to add\n')
positoin = int(input('what position you wanna add\n'))+ 1
if letter in list1:
    print('letter is already in the list')
else:
    list1.insert(positoin, letter)
print(list1)