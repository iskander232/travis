import pytest
from enceriptor import *
from for_test import *


def test_caesar():
    x = give_caesar('encode', 'abacaba', 1)
    y = give_caesar('decode', x, 1)
    assert y == 'abacaba'


def test_files():
    write('x', 'abacaba')
    x = read('x')
    assert x == 'abacaba'


def test_caesar_bad1():
    with pytest.raises(IndexError):
        give_caesar('encode', 'abacaba', 10000)


def test_caesar_bad2():
    with pytest.raises(TypeError):
        give_caesar('encode', 'abacaba', 'aa')


def test_find_bad():
    with pytest.raises(NameError):
        give_caesar('dfdsfaf', 'abacaba', 1)


def test_read_bad():
    with pytest.raises(FileNotFoundError):
        read('xxx')
