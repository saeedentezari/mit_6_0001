# Problem Set 2, hangman.py
# Writer: Saeed Entezari
# -----------------------------------
# Hangman Game
# -----------------------------------
import random
import string

####################################################################
# Loading words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Read and return a list of valid words from a file: words.txt
      Words are strings of lowercase letters.
    returns: a (list) of words (strings)
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

####################################################################
# Helper functions for hangman()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # It can be done simply by next line
    # return set(secret_word) <= set(letters_guessed)
    # but let's form a loop in order to be clear
    nmatch = 0
    for let in secret_word:
      if let in letters_guessed:
        nmatch += 1
    return nmatch == len(secret_word)

def get_guessed_word(secret_word, letters_guessed):
    '''
    Check which letters of secret_word is revealed so far by letters_guessed
      and returns revealed word in structure of that
      guessed letters will show up and
      unguessed will be hided by underscores (_)
    secret_word (string): the word the user is guessing
    letters_guessed (list of letters): which letters have been guessed so far by the user
    returns: revealed_word (string): a string of revealed letters and hided ones by underscore
    '''
    revealed_word = str()
    for let in secret_word:
      if let in letters_guessed:
        revealed_word += let + " "
      else:
        revealed_word += "_ "
    return revealed_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed (list of letters): which letters have been guessed so far by the user
    returns: string of letters which have not been guessed yet and are available for guessing
    '''
    # the complementary of two lists could be done simply by the statement in the next line
    # available_letters = list(set(alphabet) - set(letters_guessed))
    alphabet = list(string.ascii_lowercase)
    available_letters = list()
    for let in alphabet:
      if let not in letters_guessed:
        available_letters += let
    return ''.join(available_letters)

def warning(warnings_remaining, guesses_remaining):
      '''
      check if no warnings remaining, penalize the user by
        reducing guesses remaining by one.
        also print out what happens in each case.
      
      Returns: tuple(warnings_remaining(int), guesses_remaining(int))
      '''
      if warnings_remaining == 0:
          guesses_remaining -= 1
          print('You now have no warnings left so you lose one guess: ')
      else:
          warnings_remaining -= 1
          print(f"You have {warnings_remaining} warnings left: ")
      return warnings_remaining, guesses_remaining

####################################################################
# Hangman interactive game

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with double the length of the word as number of guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    '''

    print('----------------')
    print('Welcome to the game Hangman!')
    print('Rules:')
    print('\t- You can only guess a letter at a time.')
    print('\t- By each invalid input your warnings remaining decrease by one.')
    print('\t- If you have no warnings left, you lose one guess.')
    print('\t- You have double the length of the word as number of guesses.')
    print('\t- Double penalize if your guess is a vowel.')
    print('\t- Guess the whole word befor you ran out of guesses, otherwise you lose.')
    print('----------------')
    print("Let's play the game!")
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print('----------------')

    # guesses_remaining = 2 * len(secret_word)
    # warnings_remaining = 3
    remainings = {'guesses': 2 * len(secret_word), 'warnings': 3}
    letters_guessed = []

    def warning():
      '''
      check if no warnings remaining, penalize the user by
        reducing guesses remaining by one.
        also print out what happens in each case.
      
      This function defined in hangman environment, so its parent is hangman,
      and it changes remainings dictionary which lives in hangman's scope.
      '''
      if remainings['warnings'] == 0:
          remainings['guesses'] -= 1
          print('You now have no warnings left so you lose one guess: ')
      else:
          remainings['warnings'] -= 1
          print(f"You have {remainings['warnings']} warnings left: ")

    while not is_word_guessed(secret_word, letters_guessed) and remainings['guesses'] > 0:

        print(f"You have {remainings['guesses']} guesses and {remainings['warnings']} warnings left")
        print(f'Available letters: {get_available_letters(letters_guessed)}')
        guess = input('Please guess a letter: ')

        # check guess validation and decide whether it's correct/penalty/warning
        if guess.isalpha() and len(guess) == 1: # guess is a valid character

            guess = guess.lower()
            # notice: first check repetitive rather than correctness
            # because otherwise the correct guess never would be repetitive
            if guess in letters_guessed:  # repetitive guess
                # warning
                print("Oops! You've already guessed that letter.", end=' ')
                warning()
            elif guess in secret_word:  # guess is correct
                print('Good guess:')
                # no penalty or warning
                # just add correct guess to letters_guessed
                letters_guessed += guess
            else: # guess is incorrect
                # decide how to penalize
                if guess in vowels:
                    # double penalize
                    print('That letter (vowel) is not in my word, double penalize:')
                    remainings['guesses'] -= 2
                else:
                    # single penalize
                    print('That letter (consonant) is not in my word, single penalize:')
                    remainings['guesses'] -= 1
                # add incorrect guess to letters_guessed
                letters_guessed += guess

        else: # guess in invalid
            print('Oops! That is not a valid letter.', end=' ')
            warning()
        
        print(get_guessed_word(secret_word, letters_guessed))
        print('----------------')
    
    # game termination
    if is_word_guessed(secret_word, letters_guessed): # won
        print('Congratulation, you won!')
        print(f'Your score = (# guesses remaining) * (# unique letters of {secret_word}) =', end=' ')
        print(f"{remainings['guesses'] * len(set(secret_word))}")
    else: # lost
        print(f'Sorry, you ran out of gusses. The word was "{secret_word}"')

####################################################################
# Hangman with "hints"

def match_with_gaps(my_word, other_word):
    '''
    check if my_word which is unrevealed word like "t _ _ t "
      matches with other_word, in places of revealed letters.
    my_word (string): string with characters and underscores,
      both followed by space
    other_word (string): a regular English word
    returns: boolean, True if match, otherwise False
    '''
    # prepare my_word by cutting spaces
    # "t _ _ t" -> "t__t"
    my_word = ''.join(my_word.split())
    # first of all, length should be the same
    if len(my_word) != len(other_word):
        return False
    else: # lengths match
        # iterate through indeces and check if letters match
        for i in range(len(my_word)):
            # don't check hidden letters in my_word
            if my_word[i] == "_":
              continue
            # if any letter doesn't match, so two words can't match
            if my_word[i] != other_word[i]:
                return False
        return True # if the programm reach here, two words should match
            
def show_possible_matches(my_word):
    '''
    print out which words are possible matches of unrevealed my_word.
    my_word (string): of the form letters and underscores followed by space.
      for example, "t _ _ t ".
    '''
    print('Possible word matches are:')
    for word in wordlist: # wordlist would be a variable in main scope
        if match_with_gaps(my_word, word):
            print(word, end=' ')
    print('\n----------------')

def hangman_runner(guess, secret_word, letters_guessed, warnings_remaining, guesses_remaining):
    '''
    run hangman one step further.
      parameters indicates the state of the game in place.
    
    guess (string): string that user entered
    secret_word (string): word to be guessed
    letters_guessed (list of characters): letters user guessed so far
    warnings_remainin (int), guesses_remaining (int)

    return: updated values for letters_guessed, warning_remaining, guesses_remaining
    '''
    # check guess validation and decide whether its correct/penalty/warning
    if guess.isalpha() and len(guess) == 1: # guess is a valid character

        guess = guess.lower()
        # notice: first check repetitive rather than correctness
        # because otherwise the correct guess never would be repetitive
        if guess in letters_guessed:  # repetitive guess
            # warning
            print("Oops! You've already guessed that letter.", end=' ')
            warnings_remaining, guesses_remaining = warning(warnings_remaining, guesses_remaining)
        elif guess in secret_word:  # guess is correct
            print('Good guess:')
            # no penalty or warning
            # just add correct guess to letters_guessed
            letters_guessed += guess
        else: # guess is incorrect
            # decide how to penalize
            if guess in vowels:
                # double penalize
                print('That letter (vowel) is not in my word, double penalize:')
                guesses_remaining -= 2
            else:
                # single penalize
                print('That letter (consonant) is not in my word, single penalize:')
                guesses_remaining -= 1
            # add incorrect guess to letters_guessed
            letters_guessed += guess

    else: # guess in invalid
        print('Oops! That is not a valid letter.', end=' ')
        warnings_remaining, guesses_remaining = warning(warnings_remaining, guesses_remaining)
    
    print(get_guessed_word(secret_word, letters_guessed))
    print('----------------')

    return letters_guessed, guesses_remaining, warnings_remaining

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with double the length of the word as number of guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * NEW: If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    '''

    print('----------------')
    print('Welcome to the game Hangman!')
    print('Rules:')
    print('\t- You can only guess a letter at a time.')
    print('\t- By each invalid input your warnings remaining decrease by one.')
    print('\t- If you have no warnings left, you lose one guess.')
    print('\t- You have double the length of the word as number of guesses.')
    print('\t- Double penalize if your guess is a vowel.')
    print('\t- Guess the whole word befor you ran out of guesses, otherwise you lose.')
    print('Help:')
    print('\tYou can call help by entering "*" as guess letter!')
    print('\tIt shows you possible word matches by your guessed word so far.')
    print('----------------')
    print("Let's play the game!")
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print('----------------')

    guesses_remaining = 2 * len(secret_word)
    warnings_remaining = 3
    letters_guessed = []

    while not is_word_guessed(secret_word, letters_guessed) and guesses_remaining > 0:

        print(f'You have {guesses_remaining} guesses and {warnings_remaining} warnings left')
        print(f'Available letters: {get_available_letters(letters_guessed)}')
        guess = input('Please guess a letter: ')

        if guess == "*":  # user asked for hint
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            show_possible_matches(guessed_word)
        else: # continue the game
          letters_guessed, guesses_remaining, warnings_remaining = hangman_runner(guess, secret_word, letters_guessed, warnings_remaining, guesses_remaining)
    
    # game termination
    if is_word_guessed(secret_word, letters_guessed): # won
        print('Congratulation, you won!')
        print(f'Your score = (# guesses remaining) * (# unique letters of {secret_word}) =', end=' ')
        print(f'{guesses_remaining * len(set(secret_word))}')
    else: # lost
        print(f'Sorry, you ran out of gusses. The word was "{secret_word}"')

####################################################################
# Main

if __name__ == "__main__":

    vowels = set('aoieu')
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    # secret_word = 'tart'
    # hangman(secret_word)
    hangman_with_hints(secret_word)