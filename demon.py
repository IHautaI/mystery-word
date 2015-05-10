import re
import random


def demonize(families, guesses):
    """
    picks whether or not a
    guess will be correct
    based on number of guesses wrong
    and current word families
    """

    if len(guesses) == 8:
        fam = [(key, value) for key, value in families.items()
               if not contains(key, guesses)]
        if fam:
            return max(fam, key=lambda x: len(x[1]))

        return random.choice([(key, value) for key, value in families.items()
                              if contains(key, guesses)])

    else:
        rand_key = random.choice(list(families.keys()))

        key_list = [keys for keys in families.keys()]
        key_list = sorted(key_list, key=lambda x: len(pull_indices(x, '_')),
                          reverse=True)

        length = max([len(key_list)//2, 1])

        key = random.choice(key_list[:length])
        key = random.choice([key, rand_key])

        return key, families[key]


def check_families(guesses, word_list, word):
    """
    filters word_list and sorts into families
    based on matches to word with the guess
    replacing any combination of '_'s,
    then evaluates which family is best
    and returns the matching new word and the
    corresponding word family
    """

    families = {}
    guess = guesses[-1]
    words = [item for item in word_list if contains(item, [guess]) and
             not contains(item, guesses[:-1])]

    if words:  # if there are any matches with this guess, partition
        for item in words:

            result = None
            indices = pull_indices(item, guess)
            search_term = replace(word, indices, guess)

            if search_term not in families.keys():
                result = filter_list(words, search_term, guess)

            if result:
                families[search_term] = result

        new_list = [item for item in word_list if not contains(item, guesses)]

        if new_list:
            families[word] = new_list

        return demonize(families, guesses)

    else:
        return word, [item for item in word_list
                      if not contains(item, guesses)]


def contains(item, guesses):
    """
    Returns True if item contains any guess from guesses
    """

    return_list = []
    if guesses:
        for letter in guesses:
            return_list.extend(re.findall(r'{}'.format(letter), item))

    return return_list != []


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
