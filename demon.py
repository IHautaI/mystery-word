import re
import itertools
import random

def demonize(families, num):
    """
    picks whether or not a
    guess will be correct
    based on number of guesses wrong
    and current word families
    """
    if num == 7:
        return max(families, key=lambda x: len(x[1]))
    else:
        return random.choice(families)



def check_families(guess, word_list, word, num):
    """
    filters word_list and sorts into families
    based on matches to word with the guess
    replacing any combination of '_'s,
    then evaluates which family is best
    and returns the matching new word
    """

    families = []
    indices = pull_indices(word) # index of '_'s in list
    combos = searcher(indices) # list of combinations of indices
    print('number of combinations: {}'.format(len(combos)))
    for combo in combos:

        term = replace(word, combo, guess)
        result = filter_list(word_list, term, guess)
        if result:
            families.append((term, result))

    if families:
        word, fam = demonize(families, num)
    else:
        fam = word_list

    return word, fam


def searcher(index_list):
    """
    Calculates all combinations from
    input list
    """
    return_list = []
    for num in range(0, len(index_list)+1):
        item = map(list, itertools.combinations(index_list, num))
        return_list.extend(list(item))

    return return_list

def pull_indices(word):
    """
    finds the underscores in word
    and returns their indices as
    a list
    """
    index_list = []
    for index,letter in enumerate(word):
        if letter == '_':
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
        for index,this_letter in enumerate(word):
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

    if repl != None:
        repl = '[^{}]'.format(repl)
        repl_index = pull_indices(word)
        letters = replace(word, repl_index, repl)

    return [entry for entry in word_list if re.match(r'{}'.format(word), entry)]
