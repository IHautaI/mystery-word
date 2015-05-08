import mystery_word as mw

import os


def main():
    """
    Runs the main loop named loop
    and calls play_again to ask
    if you want to play again
    """
    words = import_words('/usr/share/dict/words')
    loop(words)

    while play_again():
        loop(words)

    os.system('clear')


def loop(words):
    """
    The main loop
    displays information to the user
    and processes input from the user
    """
    os.system('clear')
    welcome()

    word_list = ask_difficulty(words)
    word = mw.random_word(word_list)
    guesses = []
    correct_guess = []

    number_of_letters(word)

    while True:
        if len(guesses) > 7:
            you_lose(word)
            break

        this_guess = guess()
        while this_guess in guesses or this_guess in correct_guess:
            print("You already guessed {}!".format(this_guess.upper()))
            this_guess = guess()

        guesses.append(this_guess)

        if this_guess == 'quit':
            os.system('clear')
            break

        if guesses[-1] in word:
            correct_guess.append(guesses.pop())

        if mw.is_word_complete(word, correct_guess):
            you_win(word)
            break

        os.system('clear')
        print("Incorrect Guesses ({}, 8 max): [ {} ]".format(len(guesses),
              " ".join(guesses).upper()))
        print(mw.display_word(word, correct_guess))


def you_lose(word):
    """
    Displays a lost game message
    """
    os.system('clear')
    print("You did not guess the word!")
    print("The word was: {}".format(word))


def you_win(word):
    """
    Displays a won game message
    """
    os.system('clear')
    print("You guessed the word!\nCongratulations!")
    print("It was {}".format(word))


def play_again():
    """
    Asks if player wants to play again
    and returns True if they do
    False otherwise
    """
    yes_no = input("Would you like to play again? [Y]es [n]o : ")

    if len(yes_no) > 1 or yes_no.lower() not in 'yn':
        return play_again()

    if yes_no == 'y':
        os.system('clear')
        return True
    else:
        os.system('clear')
        return False


def ask_difficulty(words):
    """
    Asks the player what difficulty
    and sets the difficulty based
    on their choice (if valid)
    """
    diff = input("What difficulty? [E]asy [m]edium [h]ard : ")
    word_list = []
    diff = diff.lower()

    if diff not in 'emh':
        return ask_difficulty(words)
    os.system('clear')

    if diff == 'e':
        word_list = mw.easy_words(words)
    elif diff == 'm':
        word_list = mw.medium_words(words)
    else:
        word_list = mw.hard_words(words)

    return word_list


def number_of_letters(word):
    """
    Displays the length of the word
    """
    print("The number of letters in your word is: {}".format(len(word)))


def welcome():
    """
    Welcomes the player to the game
    """
    print("Welcome to the Mystery Word game!")


def guess():
    """
    Takes player input of a single letter
    or 'quit'
    and returns the guess if valid, repeats
    if not, and quits the main loop if 'quit'
    """

    this_guess = input("Type \"quit\" to exit. Your Guess: ")

    if len(this_guess) > 1 or not this_guess.isalpha():
        if this_guess.lower() == 'quit':
            return 'quit'

        print("Not a letter. Guess again:")
        return guess()

    return this_guess


def import_words(path):
    """
    Imports the list of words from the
    specified path
    requires one word per line
    """

    text = ''
    with open(path, 'r') as file:
        text = file.readlines()

    return clean_text(text)


def clean_text(text):
    """
    Strips the text, lowercases it
    and returns it in list form
    """
    return [line.strip().lower() for line in text]

if __name__ == '__main__':
    main()
