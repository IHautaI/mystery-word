import demon

import os
import random


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
    """

    welcome()
    word_list = []
    word_length = ask_difficulty(max(map(len, words)))

    while not word_list:
        word_length = random.choice(word_length)
        word_list = [item for item in words if len(item) == word_length]

    guesses = []
    correct_guess = []

    number_of_letters(word_length)
    word = '_'*word_length

    while True:
        if len(guesses) > 7:
            os.system('clear')
            print('Incorrect guesses: {}'.format(guesses))
            you_lose(random.choice(word_list))
            break

        this_guess = guess()

        while this_guess in guesses or this_guess in correct_guess:
            print("You already guessed {}!".format(this_guess.upper()))
            this_guess = guess()

        guesses.append(this_guess)

        if this_guess == 'quit':
            os.system('clear')
            break

        new_word, word_list = demon.check_families(guesses, word_list, word)

        if new_word != word:
            correct_guess.append(guesses.pop())
            word = new_word

        if not demon.pull_indices(word, '_'):
            you_win(word)
            break

        os.system('clear')
        print("Incorrect Guesses ({}, 8 max): [ {} ]".format(len(guesses),
              " ".join(guesses).upper()))

        print(display(word))


def display(word):
    """
    adds spaces between letters/underscores
    in word and returns it
    """
    letters = [letter for letter in word]
    return " ".join(letters)


def you_lose(word):
    print("You did not guess the word!")
    print("The word was: {}".format(word))


def you_win(word):
    os.system('clear')
    print("You guessed the word!\nCongratulations!")
    print("It was {}".format(word))


def play_again():
    yes_no = input("Would you like to play again? [Y]es [n]o : ")

    if len(yes_no) > 1 or yes_no.lower() not in 'yn':
        return play_again()

    if yes_no == 'y':
        os.system('clear')
        return True
    else:
        os.system('clear')
        return False


def ask_difficulty(words_max):
    diff = input("What difficulty? [E]asy [m]edium [h]ard : ")
    size = []
    diff = diff.lower()

    if diff not in 'emh':
        return ask_difficulty(words_max)
    os.system('clear')

    if diff == 'e':
        size = [4, 5, 6]
    elif diff == 'm':
        size = [6, 7, 8]
    else:
        size = range(8, words_max)

    return size


def number_of_letters(word_len):
    print("The number of letters in your word is: {}".format(word_len))


def welcome():
    print("Welcome to the Mystery Word game!")


def guess():

    this_guess = input("Type \"quit\" to exit. Your Guess: ")

    if len(this_guess) > 1 or not this_guess.isalpha():
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
