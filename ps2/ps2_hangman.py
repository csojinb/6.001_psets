# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Loads word list and greets player
def hangman_start():
    wordlist = load_words()
    thick_section_break()
    print ('Welcome to virtual hangman!'
            ' (no stick people will be harmed in this game)')
    print ""
    thick_section_break()
    return wordlist

def game_start(guesses):
    """
    Starts a new game of hangman. Selects a word and prints the starting board.
    """
    word = choose_word(wordlist)
    word_length = len(word)
    print 'I\'m thinking of a word that is',str(word_length),'letters long.'

    available_letters = 'abcdefghijklmnopqrstuvwxyz'

    return (word, initialize_incomplete_word(word), available_letters)

    # thin_section_break()

## Style Stuff
def thick_section_break():
    print "="*80
    print ""

def thin_section_break():
    print "_"*80
    print ""
##

def print_current_board():
    print_spaced(incomplete_word)
    print ""
    print "Available letters:",available_letters
    if guesses == 1:
        print "You have 1 guess remaining."
    else:
        print "You have", guesses, "guesses remaining."


def check_for_letter(word, letter):
    """
    Checks the input word for instances of the input letter.

    Returns a list of indices. If the letter does not occur,
    returns an empty list.
    """
    indices = []
    prev_index = 0
    counter = 0

    while counter <= len(word):
        index = word[prev_index:].find(letter)

        if index == -1:
            break

        index = index + prev_index
        indices.append(index)

        prev_index = index + 1
        counter += 1

    return indices

def update_available_letters(available_letters, letter):
    """
    Removes already-guessed letter from string of remaining letters.
    Returns updated string.
    """
    letters_list = list(available_letters)

    if letters_list.count(letter) == 0:
        return available_letters

    else:
        letters_list.remove(letter)

        return "".join(letters_list)

print update_available_letters('abcdefg','c')


def fill_in_letters(incomplete_word, letter, indices):
    """
    Takes the list of indices output by check_for_letter and fills them
    into incomplete_word (input as a string, with spaces between 
    letters/underscores).

    Returns updated incomplete word.
    """
    incomplete_word = list(incomplete_word)

    for index in indices:
        incomplete_word[index] = letter

    return "".join(incomplete_word)


def initialize_incomplete_word(word):
    """
    Takes the hangman word and outputs the blank output for the
    beginning of the game.
    """
    return ("_" * len(word))

def print_spaced(incomplete_word):
    """
    Takes the incomplete word and prints it with spaces between characters.
    """
    print " ".join(list(incomplete_word))

def is_alpha(string):
    """
    Assumes input string.
    If all characters are alphabet letters, returns True.
    """
    string = string.lower()

    for char in string:
        if char in 'abcdefghijklmnopqrstuvwxyz':
            continue
        else:
            return False

    return True

# def guess_letter():
    

# x = fill_in_letters(initialize_incomplete_word('apple'), 'p', [1,2])
# print x
# print_spaced_incomplete_word(x)

# print check_for_letter('applepie','e')
guesses = 8

wordlist = hangman_start()
word, incomplete_word, available_letters = game_start(guesses)
print_current_board()

while guesses >= 0:
    
    guess = raw_input("Choose a letter or solve the puzzle:").lower()

    # single-letter guesses
    if len(guess) == 1 and is_alpha(guess) == True:
        if available_letters.find(guess) == -1:
            print "That letter is not available."
            continue

        indices = check_for_letter(word, guess)

        if indices == []:
            print 'I\'m sorry, there are no %s\'s in this word.' % (guess)
        else:
            print 'Hurray! You got one!'

            incomplete_word = fill_in_letters(incomplete_word, guess, indices)

            ### add solve check!!!
            if '_' not in incomplete_word:
                print 'Congratulations, you successfully completed the word!'
                solved = True
                print_spaced(incomplete_word)
                break
        
        available_letters = update_available_letters(available_letters, guess)

        print_current_board()
        guesses -= 1

    # treat multi-letter guesses as attempts to solve
    elif is_alpha(guess) == True: 
        if guess == word:
            print 'Congratulations, you correctly solved the word!'
            solved = True
            print_spaced(incomplete_word)
            break
        else:
            print 'I\'m sorry, that is not the correct word.'

    # non-alpha guesses
    else:
        print 'Invalid entry. Please enter only alphabetic characters.'

