### Playing with the insert function in Python
### Inspired by LRM1's christmas food exhange, decided to create a generator to help pair up participants without repeating the pairings!

## Title
print('Welcome to Christmas Santa Generator!')
print('Working version: 16052022_v1, by @QYGoh\n')

## getting total number of participants
number = int(input('Insert total number of participants:\n'))

## creating a dictionary to capture different variables
# code credit @https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop
d = {}
for n in range(number):
    d["Name{0}".format(n + 1)] = str(
        input("\nInsert Participant{0}'s Name:\n".format(
            n + 1)))  #did a x+1 because of 0 indexing in python

folks = list(d.values())  # saving the user inputs into a list of names

## creating the logic to pair up all participants without repeating the pairings...
# code credit @#code credit @ https://stackoverflow.com/questions/66588001/random-pairs-without-repeats-in-python-numpy-or-itertools
import numpy as np
# creating a function 
def santa_magic(names_of_people):
    shuffled = np.random.permutation(names_of_people)
    pairs_or_triplets = []
    for names in np.array_split(shuffled, len(shuffled) / 2):
        print(names)

## The final outcome
print("\nOne moment\nSanta is performing the magic now...\nAnd the pairings are:\n")
santa_magic(folks) #if the number of participants is odd, there will be a group of 3 in the pairings
