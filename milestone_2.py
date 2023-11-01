import random

word_list = ['mango', 'orange', 'banana', 'apple', 'melon']
print(type(word_list), ": ", word_list)

word = random.choice(word_list)
#print(word)

guess = input('Please enter a single letter: ')

print('\nGood guess!') if len(guess) == 1 else print('\nOops! That is not a valid input.')
    