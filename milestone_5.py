import random

word_list = ['mango', 'orange', 'banana', 'apple', 'melon']
print(word_list)

#word = random.choice(word_list)
#print(word)

class Hangman:
    
    '''
    This class contains the code to Hangman game.
    
    Attributes:
        word_list: List of words from which the code randomly selects.
        num_lives: Initial number of lives/attempts.       
    '''
    
    def __init__(self, word_list, num_lives = 5):
        
        '''
        This function initialises the arguments in the class.
        '''
        
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
        
        #print(self.word)

        
    def check_guess(self, guess):
        
        '''
        This function checks if the randomly selected word contains the guessed letter.
        '''
        
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for index in range(len(self.word)):
                if guess == self.word[index]: self.word_guessed[index] = guess
            self.num_letters -= 1
            print(self.word_guessed)
            return True
        else:
            self.num_lives -= 1
            print(f'Sorry, the letter {guess} is not in the word')
            print(f'You have {self.num_lives} lives left.')
                
    def ask_for_input(self):
        
        '''
        This function takes the user input and makes sure that it is a single
        alphabet character.
        '''
        
        
        #while True:
        guess = input('Please enter a single letter: ')
                
        while (guess.isalpha() != True) or (len(guess) != 1):
            guess = input('Invalid letter. Please, enter a single alphabetical character. ')
            
        if guess in self.list_of_guesses:
            print('You already tried that letter!')
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess) 
                #print(self.list_of_guesses)

def play_game(word_list):
    
    '''
    This function creates an instance of the class Hangman.
    It also keeps check on the number of lives and unique letters remaining.
    By doing so it implements the conditions for winning or losing the game.
    '''
    
    num_lives = 5
    game = Hangman(word_list, num_lives)
    print (game.num_letters)
    
    while game.num_lives != 0:
        
        if game.num_letters > 0:
            game.ask_for_input()
            print(game.num_letters)
        else:
            print('Congratulations. You won the game!')
            break
    else:
        print('You lost!')
    
play_game(word_list)
            


#print(my_instance.word)
#my_instance.ask_for_input()

#
#print(my_instance.word_guessed)
#print(my_instance.num_lives)





        
#ask_for_input()
