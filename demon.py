import re
import random


def demonize(families, num):
    """
    picks whether or not a
    guess will be correct
    based on number of guesses wrong
    and current word families
    """

    if num == 7:
        fam = [(key, value) for key, value in families.items()]
        return max(fam, key=lambda x: len(x[1]))

    else:
        key = random.choice(list(families.keys()))
        return key, families[key]


def check_families(guess, word_list, word, num):
    """
    filters word_list and sorts into families
    based on matches to word with the guess
    replacing any combination of '_'s,
    then evaluates which family is best
    and returns the matching new word
    """

    families = {}
    words = [item for item in word_list if contains(item, guess)]

    if words:
        for item in words:

            indices = pull_indices(item, guess)
            search_term = replace(word, indices, guess)
            result = filter_list(words, search_term, guess)

            if result:
                families[search_term] = result

                for entry in result:
                    words.remove(entry)

        if families:
            word, fam = demonize(families, num)
        else:
            fam = words

    else:
        return word, word_list

    return word, fam


def contains(item, guess):
    """
    Returns True if item contains guess
    """
    return re.findall(r'{}'.format(guess), item) != []


def pull_indices(word, letter):
    """
    finds the underscores in word
    and returns their indices as
    a list
    """

    index_list = []
    for index, let in enumerate(word):
        if let == letter:
            index_list.append(index)

    return index_list


def replace(word, indices, letter):
    """
    replaces the letters in the word
    at the index specified
    with the given letter
    """
    if indices:
        return_word = ''
        for index, this_letter in enumerate(word):
            if index in indices:
                return_word += letter
            else:
                return_word += this_letter
        word = return_word

    return word


def filter_list(word_list, word, repl=None):
    """
    takes word and finds
    all matching words in word_list
    with [^{repl}] subbed
    for the '_' entries where needed
    """

    if repl is not None:
        repl = '[^{}]'.format(repl)
        repl_index = pull_indices(word, '_')
        word = replace(word, repl_index, repl)

    return [entry for entry in word_list if
            re.match(r'{}'.format(word), entry)]
