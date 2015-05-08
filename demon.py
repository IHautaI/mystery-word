# recursive search to get all possibilities
# from replacing _'s with guess, multiple allowed
# use filter_list here to make the families
# then evaluate which to use and
# return corresponding word
def check_families(guess, word_list, word):
    families = []
    indices = pull_indices(word)
    combos = searcher(0,indices)

    return word


def searcher(index,index_list):
    """
    recursively calculates combinations of items
    from index_list and returns them as a list
    """
    return_list = []

    if index == 0:
        return_list.append(index_list)
        if len(index_list) > index+1:
            return_list.extend(searcher(0,index_list[index+1:]))
    else:
        if len(index_list) > index + 1:
            return_list.append(index_list[:index]+index_list[index+1:])
        else:
            if len(index_list) == index:
                return_list.append(index_list[:index])
            return_list.append([index_list[0]])

    if len(index_list) > index + 1:
        return_list.extend(searcher(index+1,index_list))

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


def replace(word,indices,letter):
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


# Tested
def filter_list(word_list, word):
    word_list = word_list[:]

    letters = [letter for letter in word]
    for index in range(len(letters)):
        if letters[index] == '_':
            letters[index] = '\w'

    letters = ''.join(letters)

    for word in word_list:
        if not re.match(r'{}'.format(letters), word):
            word_list.remove(word)

    return word_list