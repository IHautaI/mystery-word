from mystery_word import *

import os


def main():

    words = import_words('/usr/share/dict/words')
    welcome()

    word_list = ask_difficulty(words)
    guesses = 0

    def loop():
        while entry != 'q':
            word = random_word(word_list)
            number_of_letters(word)
            guess = guess()

            if guess == 'quit':
                entry = 'q'


    loop()


    while play_again():
        loop()



def play_again():
    yes_no = input("Would you like to play again? [Y]es [n]o : ")

    if len(yes_no)>1 or yes_no.lower() not in 'yn':
        return play_again()

    if yes_no == 'y':
        return True
    else:
        return False



def ask_difficulty(words):
    diff = input("What difficulty? [E]asy [m]edium [h]ard : ")
    word_list = []
    diff = diff.lower()

    if diff not in 'emh':
        ask_difficulty(words)
    os.system('clear')

    if diff = 'e':
        word_list = easy_words(words)
    elif diff = 'm'
        word_list = medium_words(words)
    else:
        word_list = hard_words(words)

    return word_list


def number_of_letters(word):
    print("The number of letters in your word is: " + len(word))


def welcome():
    print("Welcome to the Mystery Word game!")


def guess():

    guess = input("Your Guess: ")

    if len(guess)>1 or not guess.isalpha():
        if guess.lower() == 'quit':
            return 'quit'

        print("Not a letter. Type Quit to exit.\nGuess again:")
        guess()

    return guess


def import_words(path):
    text = ''
    with open(path, 'r') as file:
        text = file.readlines()

    return clean_text(text)


def clean_text(text):
    return [line.strip().lower() for line in text]

if __name__ == '__main__':
    main()
