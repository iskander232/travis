import pytest
from  enceriptor import *
def test1():
    x = encode_from_caesar('encode', 'abacaba', 1)
    y = encode_from_caesar('decode', x, 1)
    assert y == 'abacaba'
