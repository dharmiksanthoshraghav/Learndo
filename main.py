import csv
from random import randint as rand

intset =[]
set1 = []
set2 = []
x = True

file = input('Enter the file name: ')
print('Type exit to exit\n')
with open(file,'r') as f:
    reader = csv.reader(f)
    for row in reader:
        intset.append(row)

for elem in intset:
    set1.append(elem[0])

for elem in intset:
    set2.append(elem[1])

while x:
    if len(set1) == 0:
        print('Congrats, You have completed the set')
        break

    r = rand(0,len(set1))

    if r == len(set1):
        r = r-1

    y = input(set1[r]+': ')

    if y == set2[r]:
        print('Correct!')
        set1.pop(r)
        set2.pop(r)

    elif y == 'exit':
        x = False
    else:
        print('Wrong!')
    print(' ')