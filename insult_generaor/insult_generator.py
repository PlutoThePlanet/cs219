from random import choice
import time

#lists
adjectives = ['wet', 'big', 'dumb', 'stinky', 'lazy']
nouns = ['turnip', 'dog', 'goat', 'monke', 'booger']

#functions
def printInsult (name, age):
    print(name + ', you are a ' + str(age) + ' ' + choice(adjectives) + ' ' + choice(nouns))
    

#program
name = input('What is your name? ')
if name == 'paige':
    print('ඞ ඞ ඞ')
    quit()

age = int(input('How old are you? '))
if (age < 16):
    age = 'young'
else:
    age = 'old'

option = 5
while option != 0:
    option = int(input('1: print insults at your demand\n2: print insults endlessly\n0: exit\n'))
    if(option == 1):
        printInsult(name, age)
        cont = input('Can you handle more (y/n)')
        while cont != 'n':
            printInsult(name, age)
            cont = input('Can you handle more (y/n)')
        quit()
    elif(option == 2):
        while option == 2:
            printInsult(name, age)
            time.sleep(3)
    elif(option == 0):
        quit()
    else:
        print('not an option, try again\n')
