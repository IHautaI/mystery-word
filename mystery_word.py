from random import choice


def easy_words(word_list):
    return [word for word in word_list if len(word) < 7 and len(word) > 3]


def medium_words(word_list):
    return [word for word in word_list if len(word) < 9 and len(word) > 5]


def hard_words(word_list):
    return [word for word in word_list if len(word) > 7]


def random_word(word_list):
    return choice(word_list)


def display_word(word, letters):

    letter_list = [letter for letter in word]

    for index in range(len(letter_list)):
        if letter_list[index] not in letters:
            letter_list[index] = '_'

    return " ".join(letter_list).upper()


def is_word_complete(word, letters):

    letter_list = [letter for letter in word if letter not in letters]

    return letter_list == []
