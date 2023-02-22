#import packages and modules
import csv
from random import randint as rand

#define variables
intset =[]
set1 = []
set2 = []
x = True

#ask the file name
file = input('Enter the file name: ')

#give instructions
print('Type exit to exit\n')

#import the data from the file
with open(file,'r') as f:
    reader = csv.reader(f)
    for row in reader:
        intset.append(row)

#put the data into the 
for elem in intset:
    set1.append(elem[0])
for elem in intset:
    set2.append(elem[1])

while x:
    #generate a random number to take a value
    r = rand(0,len(set1))
    if r == len(set1):
        r = r-1

    #ask the questions
    y = input(set1[r]+': ')

    #if the answer is correct appreciate the user and remove the question from list
    if y == set2[r]:
        print('Correct!')
        set1.pop(r)
        set2.pop(r)   
    #execute the exit command
    elif y == 'exit':
        x = False
    #if the answer is wrong print wrong
    else:
        print('Wrong!')
    print(' ')
    #if the questions are completed end the program
    if len(set1) == 0:
        print('Congrats, You have completed the set')
        break