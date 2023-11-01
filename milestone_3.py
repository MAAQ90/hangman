import random

word_list = ['mango', 'orange', 'banana', 'apple', 'melon']
print(word_list)

word = random.choice(word_list)
print(word)



def ask_for_input():
    guess = input('Please enter a single letter: ')
    while (guess.isalpha() != True) or (len(guess) != 1):
        guess = input('Invalid letter. Please, enter a single alphabetical character. ')
    check_guess(guess)


def check_guess(guess):
    if guess in word:
        print(f'\nGood guess! {guess} is in the word.')
    else:
        print(f'\nSorry, {guess} is not in the word. Try again.')
        
ask_for_input()