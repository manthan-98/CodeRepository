row1 = ['a','b','c']
row2 = ['d','e','f']
row3 = ['g','h','i']
matrix = [row1,row2,row3]
print(f'{row1}\n{row2}\n{row3}\n')
position = (input('Type row and column\n'))
row = int(position[0])
column = int(position[1])
new = input('any symbol\n>')
matrix[row-1][column-1] = new
print(f'{row1}\n{row2}\n{row3}')