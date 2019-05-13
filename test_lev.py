import pytest
from lev import Levenshtein

def test_matrix():
    l = Levenshtein('non','no')
    l.build_matrix()

    assert l.distance_matrix == [[0 for x in range(3)] for x in range(4)]

def test_function():
    l = Levenshtein('non','no')
    l.build_matrix()


    distance = l.compute()
    assert distance == 1
