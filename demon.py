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
    #choice = random.choice([True, False])

    if num == 7:
        return max(families, key=lambda x: len(x[1]))
    else:
        return random.choice(families)

        #return max(families[:-1], key=lambda x: len(x[1]))


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

    for combo in combos:

        term = replace(word, combo, guess)

        if filter_list(word_list, term, guess):
            families.append((term, filter_list(word_list, term, guess)))

    #families.append((word,word_list))
    #families = sorted(families, key=lambda x: len(x[1]), reverse = True)

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
    for num in range(1, len(index_list)+1):
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
    return_word = ''
    for index,this_letter in enumerate(word):
        if index in indices:
            return_word += letter
        else:
            return_word += this_letter

    return return_word


def match(entry,letters):
    """
    matches letters in entry
    """
    return re.match(r'{}'.format(letters), entry)


def filter_list(word_list, word, repl=None):
    """
    takes word and finds
    all matching words in word_list
    with [^{repl}] subbed
    for the '_' entries where needed
    """
    letters = [letter for letter in word]

    if repl != None:
        repl = '[^{}]'.format(repl)
        repl_index = []
        for index, letter in enumerate(letters):

            if letter == '_':
                repl_index.append(index)

    letters = ''.join(letters)
    if repl != None:
        letters = replace(word, repl_index, repl)

    return [entry for entry in word_list if match(entry,letters)]
