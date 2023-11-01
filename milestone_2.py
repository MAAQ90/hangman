import random

word_list = ['mango', 'orange', 'banana', 'apple', 'melon']
print(type(word_list), ": ", word_list)

word = random.choice(word_list)
print(word)

guess = input('Please enter a single letter: ')

while (guess.isalpha() != True) or (len(guess) != 1):
    guess = input('Oops! That is not a valid input. Please retry: ')
else:
    print('\nGood guess!')
    