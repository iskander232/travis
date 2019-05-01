from pytest import *
from enceriptor import *
from for_test import *
from random import *


def test_caesar():
    for i in range(1000):
        s = ''
        for j in range(100):
            s += choice(alf)
        l = randint(0, 26)
        x = give_caesar('encode', s, l)
        y = give_caesar('decode', x, l)
        assert y == s


def test_vigenere():
    for i in range(1000):
        s = ''
        s1 = randint(1, 100)
        for j in range(s1):
            s += choice(alf)
        l = ''
        for j in range(s1):
            l += choice(string.ascii_lowercase)
        x = give_vigenere('encode', s, l)
        y = give_vigenere('decode', x, l)
        assert y == s
