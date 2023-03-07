# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Saeed Entezari

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10,
    '*': 0,
}

###############################################################
# Helper code
###############################################################

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

###############################################################
# Problem #1: Scoring a word
###############################################################

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    Wildcard has no score in first component, but will be accounted in second component.

    word: string
    n: int >= 0: length of the hand at the point word has given.
    returns: int >= 0
    """
    wordlower = word.lower()

    first_component = 0
    for let in wordlower:
        first_component += SCRABBLE_LETTER_VALUES[let]

    wordlen = len(wordlower)
    second_component = 7 * wordlen - 3 * (n - wordlen)
    second_component = max(1, second_component)

    score = first_component * second_component
    return score

###############################################################
# Problem #2: Dealing with hands
###############################################################

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    Wildcard will be shown.

    hand: dictionary (string -> int)
    """
    
    for letter, repeat in hand.items():
        for j in range(repeat):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    Each hand dealed should have exactly one wildcard "*".

    n: int >= 1
    returns: dictionary (string -> int)
    """
    
    hand={'*': 1}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

###############################################################
# Problem #2: Update a Hand by Removing Letters
###############################################################
 
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    No matter word whether word is valid.

    Has no side effects: does not modify hand.

    Input word might have uppercase letters.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    wordlower = word.lower()
    newhand = hand.copy()

    for letter in wordlower:
        if letter in newhand:
            newhand[letter] -= 1
            if newhand[letter] == 0:
                del newhand[letter]
    
    return newhand

###############################################################
# Problem #3: Test word validity
###############################################################

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    Wildcard can be used as a vowel in the word.
    For example:
    'c*ws' is a valid word (cows),
    and you saved 'o' letter if you had it,
    or you can use hidden 'o' if you have not.
    And '*ows' is not a valid word.
    Because there is no word made of a vowel in place of '*'.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    wordLower = word.lower().strip()
    handCopy = hand.copy()
    # all letters should be in the hand
    for letter in wordLower:
        if letter not in handCopy:
            return False    # if any letter is not in the hand, returns False
        handCopy[letter] -= 1
        if handCopy[letter] == 0:
            del handCopy[letter]
    # now all letters are in the hand, then check the appearance of word in the word_list

    # all vowels can be replaced by '*' (wildcard)
    # notice that split and rejoin a string that has no '*', makes no changes in the end
    splitWord = wordLower.split('*')
    for vowel in VOWELS:
        rejoinWord = vowel.join(splitWord)  # substitute a vowel in place of '*', if any
        if rejoinWord in word_list:
            return True     # if any possibility is in the word_list, returns True
    
    # by reaching this line, the word was entirely in the hand but not in the word_list
    return False

# word_list = load_words()
# hand = get_frequency_dict('*cowsz')
# word = '*ows'
# print(is_valid_word(word, hand, word_list))

###############################################################
# Problem #5: Playing a hand
###############################################################

def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handLen = 0
    for n in hand.values():
        handLen += n
    return handLen

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    print('---------------------------------------------------------------')
    # keep track of the total score
    total_score = 0
    # while still have any letter in the hand
    while calculate_handlen(hand) > 0:
        # display hand
        print('Current Hand: ')
        display_hand(hand)
        # ask user for input
        word = input('Enter a word or "!!" to indicate that you are finished: ')
        # if '!!' given:
        if word == '!!':
            # terminate the game
            break
        # validation
        # if invalid:
        if not is_valid_word(word, hand, word_list):
            # print wrong word message
            print('This is not a valid word. Please choose another word.')
        # if valid:
        else:
            # total score += valid word score
            hand_len = calculate_handlen(hand)
            word_score = get_word_score(word, hand_len)
            total_score += word_score
            # print word score and total score
            print(f'"{word}" earned {word_score} points. Total: {total_score} points.')
        # update hand
        hand = update_hand(hand, word)
        print('---------------------------------------------------------------')
    # game is over (user entered '!!' or ran out of letters)
    # if user ran out of letters was the case
    if calculate_handlen(hand) == 0:
        # let the user know
        print('You ran out of letters.', end=' ')
    # tell the user how many points they scored
    print(f'Your Total Score of the hand: {total_score}')
    print('---------------------------------------------------------------')
    # return total score
    return total_score

# word_list = load_words()
# hand = get_frequency_dict('*cows')
# play_hand(hand, word_list)

###############################################################
# Problem #6: Playing a game
###############################################################

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    # make sure letter is lowercase
    letter = letter.lower()
    # create a copy of the hand to avoid mutating the hand
    new_hand = hand.copy()
    # if letter not in the hand
    if letter not in hand:
        # return the same hand
        return hand
    # by here, letter should be in the hand

    # choose random letter from alphabet except letters which are already in the hand
    ## construct alphabet except letters already in hand
    choosable_letters = [let for let in string.ascii_lowercase if let not in hand.keys()]
    ## random choice
    ### if there is no choosable letters, in the rare case of the hand has all letters
    if len(choosable_letters) == 0:
        ### no changes can be made
        return hand
    ### choose the new letter
    new_letter = random.choice(choosable_letters)

    # substitue that random choosen letter in place of letter to be replaced
    ## add new letter to the hand
    new_hand[new_letter] = hand[letter]
    ## delete old letter from the hand
    del new_hand[letter]

    # return substitued hand
    return new_hand

# hand = get_frequency_dict('coo')
# print(hand)
# print(substitute_hand(hand, 'o'))

def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    # start of the game
    print('###############################################################')
    # ask the user total number of hands
    tot_nhands = int(input('Enter total number of hands you want to play: '))
    
    # initializations
    total_score = 0
    subed = False
    replayed = False

    # loop for hands
    for ith_hand in range(tot_nhands):

        # deal hand and display it to user
        print('New hand dealed: ', end='')
        hand = deal_hand(HAND_SIZE)
        display_hand(hand)

        # ask the user if want to substitute one letter in the hand
        if not subed:
            sub = input('Would you like to substitute a letter? ')
            if sub == 'yes':
                sub_letter = input('Which letter would you like to replace? ')
                hand = substitute_hand(hand, sub_letter)
                subed = True

        # play hand
        hand_score = play_hand(hand, word_list)

        # ask the user for replay the hand
        if not replayed:
            replay = input('Would you like to replay the hand? ')
            if replay == 'yes':
                # play hand again
                rep_hand_score = play_hand(hand, word_list)
                hand_score = max(hand_score, rep_hand_score)
                replayed = True

        # accumulate score of the hand to total score of the game
        total_score += hand_score
    
    # end of the game
    print('###############################################################')
    # display and return total score of the game
    print('Total score over all hands:', total_score)

    return total_score


if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)