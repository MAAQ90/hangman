import random

word_list = ['mango', 'orange', 'banana', 'apple', 'melon']
print(word_list)

#word = random.choice(word_list)
#print(word)

class Hangman:
    
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = {self.word}
        self.num_lives = num_lives
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
                
    def ask_for_input(self):
        while True:
            guess = input('Please enter a single letter: ')
                
            if (guess.isalpha() != True) or (len(guess) != 1):
                guess = input('Invalid letter. Please, enter a single alphabetical character. ')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(self.list_of_guesses)

my_instance = Hangman(word_list, 5)
print(my_instance.word)
my_instance.ask_for_input()

#
#print(my_instance.word_guessed)
#print(my_instance.num_lives)





        
#ask_for_input()