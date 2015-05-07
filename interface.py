import mystery_word as mw

import os


def main():

    words = import_words('/usr/share/dict/words')
    loop(words)

    while play_again():
        loop(words)

    os.system('clear')


def loop(words):
    
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

        if mw.is_word_complete(word,correct_guess):
            you_win(word)
            break

        os.system('clear')
        print("Incorrect Guesses ({}, 8 max): [ {} ]".format(len(guesses),
            " ".join(guesses).upper()))
        print(mw.display_word(word,correct_guess))


def you_lose(word):
    os.system('clear')
    print("You did not guess the word!")
    print("The word was: {}".format(word))


def you_win(word):
    os.system('clear')
    print("You guessed the word!\nCongratulations!")
    print("It was {}".format(word))


def play_again():
    yes_no = input("Would you like to play again? [Y]es [n]o : ")

    if len(yes_no)>1 or yes_no.lower() not in 'yn':
        return play_again()

    if yes_no == 'y':
        os.system('clear')
        return True
    else:
        os.system('clear')
        return False


def ask_difficulty(words):
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
    print("The number of letters in your word is: {}".format(len(word)))


def welcome():
    print("Welcome to the Mystery Word game!")


def guess():

    this_guess = input("Type \"quit\" to exit. Your Guess: ")

    if len(this_guess)>1 or not this_guess.isalpha():
        if this_guess.lower() == 'quit':
            return 'quit'

        print("Not a letter. Guess again:")
        return guess()

    return this_guess


def import_words(path):
    text = ''
    with open(path, 'r') as file:
        text = file.readlines()

    return clean_text(text)


def clean_text(text):
    return [line.strip().lower() for line in text]

if __name__ == '__main__':
    main()
