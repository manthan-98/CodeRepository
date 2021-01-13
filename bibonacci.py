#bibonacci
#0 1 1 2 3 5 8 13 21 34 55 89
in_p = int(input('Enter\n>>>'))
a = 1
list1 = [0, 1]
for i in list1:
    a += i
    list1.append(a)
    if i < in_p:
        print(i)
    else:
        break