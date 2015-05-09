from demon import *

import random
import nose


def test_searcher():
    for _ in range(10):
        num = random.randint(0, 20)
        assert len(searcher([i for i in range(num)])) == 2**num


def test_pull_indices():
    assert pull_indices('hello') == []
    assert pull_indices('cthu_u') == [4]
    assert pull_indices('he_l_') == [2, 4]
    assert pull_indices('______') == [0, 1, 2, 3, 4, 5]


def test_replace():
    assert replace('he__o', [2, 3], 'l') == 'hello'
    assert replace('_ello', [0], 'h') == 'hello'
    assert replace('_ell_', [4], 'o') == '_ello'


def test_filter_list():
    word_list = ['hello', 'greet', 'brown', 'hellc', 'hellb']
    word = 'baths'
    repl = None
    assert filter_list(word_list, word, repl) == []

    word = 'hello'
    assert filter_list(word_list, word, repl) == ['hello']

    word = 'hell_'
    repl = 'o'
    assert filter_list(word_list, word, repl) == ['hellc', 'hellb']

    repl = 'k'
    assert filter_list(word_list, word, repl) == ['hello', 'hellc', 'hellb']


def test_check_families():
    a = ['hello', 'hellb', 'ehleb', 'kohls', 'retuh']
    assert check_families('h', a, '_____', 7) == \
        ('h____', ['hello', 'hellb'])


if __name__ == '__main__':
    nose.main()
