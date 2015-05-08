import re
import itertools

# recursive search to get all possibilities
# from replacing _'s with guess, multiple allowed
# use filter_list here to make the families
# then evaluate which to use and
# return corresponding word
def check_families(guess, word_list, word):
    """
    filters word_list and sorts into families
    based on matches to word with the guess
    replacing any combination of '_'s,
    then evaluates which family is best
    and returns the matching new word
    """
    families = []
    indices = pull_indices(word) 
    combos = searcher(indices)

    for combo in combos:

        term = replace(word, combo, guess)

        if filter_list(word_list, term, guess):
            families.append((term, filter_list(word_list, term, guess)))

    families.append((word, word_list))
    families = sorted(families, key=lambda x: len(x[1]), reverse = True)
    word, fam = families[1]

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


def filter_list(word_list, word, repl=None):
    """
    takes word and finds
    all matching words in word_list
    with wildcard letters subbed
    for the '_' entries
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

    remove_list = []
    for entry in word_list:
        if not re.match(r'{}'.format(letters), entry):
            remove_list.append(entry)

    word_list = [entry for entry in word_list if entry not in remove_list]

    return word_list
